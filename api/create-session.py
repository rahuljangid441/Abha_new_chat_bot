"""Vercel serverless function for ChatKit session creation."""

from __future__ import annotations

import asyncio
import json
import os
import uuid
from typing import Any, Mapping

import httpx

DEFAULT_CHATKIT_BASE = "https://api.openai.com"
SESSION_COOKIE_NAME = "chatkit_session_id"
SESSION_COOKIE_MAX_AGE_SECONDS = 60 * 60 * 24 * 30  # 30 days


def handler(request):
    """Vercel serverless function handler."""
    # Handle CORS preflight
    if request.method == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            "body": "",
        }
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({"error": "Missing OPENAI_API_KEY environment variable"}),
        }
    
    # Parse request body
    try:
        body_str = request.body
        if isinstance(body_str, bytes):
            body_str = body_str.decode("utf-8")
        body = json.loads(body_str) if body_str else {}
    except (json.JSONDecodeError, TypeError, AttributeError):
        body = {}
    
    workflow_id = resolve_workflow_id(body)
    if not workflow_id:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({"error": "Missing workflow id"}),
        }
    
    # Get or create user ID from cookies
    cookie_header = ""
    if hasattr(request, "headers"):
        headers_dict = request.headers
        if isinstance(headers_dict, dict):
            cookie_header = headers_dict.get("cookie") or headers_dict.get("Cookie") or ""
        elif hasattr(headers_dict, "get"):
            cookie_header = headers_dict.get("cookie") or headers_dict.get("Cookie") or ""
    
    cookies = parse_cookies(cookie_header)
    user_id, cookie_value = resolve_user(cookies)
    api_base = chatkit_api_base()
    
    # Create session with OpenAI
    try:
        async def create_session():
            async with httpx.AsyncClient(base_url=api_base, timeout=10.0) as client:
                upstream = await client.post(
                    "/v1/chatkit/sessions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "OpenAI-Beta": "chatkit_beta=v1",
                        "Content-Type": "application/json",
                    },
                    json={"workflow": {"id": workflow_id}, "user": user_id},
                )
                return upstream
        
        upstream = asyncio.run(create_session())
    except Exception as error:
        headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
        if cookie_value:
            headers["Set-Cookie"] = format_cookie(cookie_value)
        return {
            "statusCode": 502,
            "headers": headers,
            "body": json.dumps({"error": f"Failed to reach ChatKit API: {str(error)}"}),
        }
    
    payload = parse_json(upstream)
    if not upstream.is_success:
        message = None
        if isinstance(payload, Mapping):
            message = payload.get("error")
        message = message or upstream.reason_phrase or "Failed to create session"
        headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
        if cookie_value:
            headers["Set-Cookie"] = format_cookie(cookie_value)
        return {
            "statusCode": upstream.status_code,
            "headers": headers,
            "body": json.dumps({"error": message}),
        }
    
    client_secret = None
    expires_after = None
    if isinstance(payload, Mapping):
        client_secret = payload.get("client_secret")
        expires_after = payload.get("expires_after")
    
    if not client_secret:
        headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }
        if cookie_value:
            headers["Set-Cookie"] = format_cookie(cookie_value)
        return {
            "statusCode": 502,
            "headers": headers,
            "body": json.dumps({"error": "Missing client secret in response"}),
        }
    
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
    }
    if cookie_value:
        headers["Set-Cookie"] = format_cookie(cookie_value)
    
    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"client_secret": client_secret, "expires_after": expires_after}),
    }


def format_cookie(cookie_value: str) -> str:
    """Format cookie for Set-Cookie header."""
    secure = is_prod()
    secure_flag = "; Secure" if secure else ""
    return f"{SESSION_COOKIE_NAME}={cookie_value}; Max-Age={SESSION_COOKIE_MAX_AGE_SECONDS}; Path=/; SameSite=Lax{secure_flag}"


def parse_cookies(cookie_string: str) -> Mapping[str, str]:
    """Parse cookie string into dictionary."""
    cookies = {}
    if not cookie_string:
        return cookies
    for item in cookie_string.split(";"):
        if "=" in item:
            key, value = item.split("=", 1)
            cookies[key.strip()] = value.strip()
    return cookies


def is_prod() -> bool:
    env = (os.getenv("ENVIRONMENT") or os.getenv("NODE_ENV") or os.getenv("VERCEL_ENV") or "").lower()
    return env == "production"


def resolve_workflow_id(body: Mapping[str, Any]) -> str | None:
    workflow = body.get("workflow", {})
    workflow_id = None
    if isinstance(workflow, Mapping):
        workflow_id = workflow.get("id")
    workflow_id = workflow_id or body.get("workflowId")
    env_workflow = os.getenv("CHATKIT_WORKFLOW_ID") or os.getenv(
        "VITE_CHATKIT_WORKFLOW_ID"
    )
    if not workflow_id and env_workflow:
        workflow_id = env_workflow
    if workflow_id and isinstance(workflow_id, str) and workflow_id.strip():
        return workflow_id.strip()
    return None


def resolve_user(cookies: Mapping[str, str]) -> tuple[str, str | None]:
    existing = cookies.get(SESSION_COOKIE_NAME)
    if existing:
        return existing, None
    user_id = str(uuid.uuid4())
    return user_id, user_id


def chatkit_api_base() -> str:
    return (
        os.getenv("CHATKIT_API_BASE")
        or os.getenv("VITE_CHATKIT_API_BASE")
        or DEFAULT_CHATKIT_BASE
    )


def parse_json(response: httpx.Response) -> Mapping[str, Any]:
    try:
        parsed = response.json()
        return parsed if isinstance(parsed, Mapping) else {}
    except (json.JSONDecodeError, httpx.DecodingError):
        return {}
