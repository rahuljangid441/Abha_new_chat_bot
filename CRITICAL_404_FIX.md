# CRITICAL: Fixing 404 Error - Function Not Found

## The Problem
Vercel is returning 404 on `/api/create-session`, which means it's not detecting your Python function.

## Most Likely Cause: Root Directory Setting

Since your GitHub repo has files at the **root level** (not in a `managed-chatkit` folder), Vercel's Root Directory **MUST** be set to `./`

### Check This First:

1. Go to **Vercel Dashboard** → Your Project → **Settings**
2. Scroll to **General** section
3. Find **Root Directory** field
4. **It MUST say `./`** (not `managed-chatkit` or anything else)
5. If it's wrong, click **Edit** and type: `./`
6. **Save** and **Redeploy**

## Verify Your File Structure

Your GitHub repo should look like this (files at root):
```
api/
  create-session.py
  requirements.txt
frontend/
  ...
vercel.json
```

NOT like this:
```
managed-chatkit/
  api/
    create-session.py
  ...
```

## After Fixing Root Directory

1. **Redeploy** your project
2. Go to **Deployments** → Latest deployment → **Functions** tab
3. You should see `api/create-session` listed
4. If you see it, the 404 should be fixed!

## If Still 404 After Root Directory Fix

### Check Function Detection:
1. In Vercel, go to **Deployments** → Latest → **Functions** tab
2. Do you see `api/create-session` listed?
   - ✅ **YES**: Function is detected, but routing might be wrong
   - ❌ **NO**: Function isn't being detected

### If Function IS Listed but Still 404:
- Check the function logs for errors
- Verify `requirements.txt` exists in `api/` folder
- Make sure `handler` function is defined correctly

### If Function is NOT Listed:
- Root directory is definitely wrong
- Or function file structure is wrong
- Or `vercel.json` configuration is wrong

## Quick Test

After fixing root directory and redeploying, test directly:
```
https://abha-new-chat-bot.vercel.app/api/create-session
```

You should get a response (even if it's an error about missing workflow ID), NOT a 404.

## Summary

**99% of 404 errors on Vercel functions are caused by wrong Root Directory setting.**

Since your files are at repo root, Root Directory MUST be `./`
