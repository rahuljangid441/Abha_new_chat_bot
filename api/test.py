"""Simple test function to verify Vercel Python detection."""

def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": '{"message": "Python function is working!", "method": "' + str(request.get("method", "unknown") if isinstance(request, dict) else getattr(request, "method", "unknown")) + '"}'
    }
