# Fixing 404 Error on /api/create-session

## The Problem
You're getting a 404 error, which means Vercel isn't finding your Python serverless function.

## What I Fixed
1. **Removed the rewrite rule** from `vercel.json` - Vercel automatically detects Python files in the `api/` folder
2. The function should now be accessible at `/api/create-session`

## After Redeploying

### Step 1: Redeploy in Vercel
1. Go to Vercel Dashboard → Your Project
2. Go to **Deployments** tab
3. Click **"..."** on the latest deployment
4. Click **"Redeploy"**

OR push a new commit (I just pushed the fix)

### Step 2: Verify the Function Exists
1. After redeploy, go to **Deployments** → Latest deployment
2. Click **"Functions"** tab
3. You should see `api/create-session` listed
4. If you don't see it, there's a detection issue

### Step 3: Check Function Logs
1. Click on `api/create-session` function
2. Go to **Logs** tab
3. Try accessing your site and see if any errors appear

## If Still Getting 404

### Option 1: Check Root Directory
- Make sure Root Directory in Vercel is set to `./` (not `managed-chatkit`)
- Since your files are at repo root, it should be `./`

### Option 2: Verify File Structure
Your GitHub repo should have:
```
api/
  create-session.py
  requirements.txt
frontend/
  ...
vercel.json
```

### Option 3: Manual Function Check
Try accessing: `https://your-project.vercel.app/api/create-session`
- If you get a response (even an error), the function is working
- If you get 404, the function isn't being detected

## Common Causes of 404

1. **Root Directory wrong** - Should be `./` for your repo structure
2. **Function not in api/** - Must be in `api/` folder
3. **Python runtime not detected** - Check that `requirements.txt` exists in `api/`
4. **Build failed** - Check deployment logs

Let me know what you see in the Functions tab after redeploying!
