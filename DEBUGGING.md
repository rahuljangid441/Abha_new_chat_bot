# Debugging Your ChatKit Deployment

## Quick Checks

### 1. Check Environment Variables in Vercel

1. Go to your Vercel project → **Settings** → **Environment Variables**
2. Verify you have:
   - ✅ `OPENAI_API_KEY` = `sk-...` (your actual key)
   - ✅ `VITE_CHATKIT_WORKFLOW_ID` = `wf-...` (your actual workflow ID)
3. Make sure they're enabled for **Production** environment
4. **Redeploy** after adding/changing variables

### 2. Check Browser Console

1. Open your deployed site
2. Press **F12** to open Developer Tools
3. Go to **Console** tab
4. Look for errors like:
   - "Set VITE_CHATKIT_WORKFLOW_ID in your .env file"
   - "Failed to create session"
   - Network errors

### 3. Check Network Requests

1. In Developer Tools, go to **Network** tab
2. Refresh the page
3. Look for a request to `/api/create-session`
4. Click on it and check:
   - **Status**: Should be 200 (not 404, 500, etc.)
   - **Response**: Should have `client_secret` (not an error)

### 4. Check Vercel Function Logs

1. Go to Vercel Dashboard → Your Project → **Deployments**
2. Click on your latest deployment
3. Go to **Functions** tab
4. Click on `api/create-session`
5. Check the **Logs** for errors

### 5. Test the API Endpoint Directly

Try calling your API directly:
```
https://your-project.vercel.app/api/create-session
```

Use a tool like:
- Postman
- curl: `curl -X POST https://your-project.vercel.app/api/create-session -H "Content-Type: application/json" -d '{"workflow":{"id":"wf-your-id"}}'`
- Browser console:
  ```javascript
  fetch('/api/create-session', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({workflow: {id: 'wf-your-workflow-id'}})
  }).then(r => r.json()).then(console.log)
  ```

## Common Errors & Solutions

### Error: "Set VITE_CHATKIT_WORKFLOW_ID in your .env file"
**Cause**: Environment variable not set or not accessible  
**Fix**: 
- Add `VITE_CHATKIT_WORKFLOW_ID` in Vercel (with `VITE_` prefix!)
- Redeploy

### Error: "Missing workflow id" (400)
**Cause**: Workflow ID not being sent or received  
**Fix**: Check that `VITE_CHATKIT_WORKFLOW_ID` is set and the frontend can access it

### Error: "Missing OPENAI_API_KEY" (500)
**Cause**: API key not set in Vercel  
**Fix**: Add `OPENAI_API_KEY` in Vercel environment variables and redeploy

### Error: 404 on `/api/create-session`
**Cause**: Function not found or routing issue  
**Fix**: 
- Check `vercel.json` rewrite rule
- Verify `api/create-session.py` exists
- Check Vercel function logs

### Error: Function timeout or 502
**Cause**: Python function error or OpenAI API issue  
**Fix**: 
- Check Vercel function logs
- Verify OpenAI API key is valid
- Check workflow ID is correct

## Still Not Working?

Share these details:
1. **Browser console errors** (screenshot or copy text)
2. **Network tab** - status code of `/api/create-session` request
3. **Vercel function logs** (from Functions tab)
4. **Environment variables** - confirm they're set (don't share the values!)
