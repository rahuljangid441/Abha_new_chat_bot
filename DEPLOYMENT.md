# Deployment Guide for OpenAI ChatKit on Vercel

This guide will help you deploy your OpenAI ChatKit application to Vercel.

## Prerequisites

- ✅ OpenAI API Key
- ✅ Workflow ID from OpenAI Agent Builder (starts with `wf_`)
- ✅ GitHub account (or GitLab/Bitbucket)
- ✅ Vercel account (free tier works)

## Step 1: Prepare Your Code

1. Make sure you're in the `managed-chatkit` directory:
   ```bash
   cd managed-chatkit
   ```

2. Ensure all files are committed to git:
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   ```

## Step 2: Push to GitHub

1. Create a new repository on GitHub (if you haven't already)
2. Push your code:
   ```bash
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

## Step 3: Deploy to Vercel

### Option A: Using Vercel Dashboard (Recommended)

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click **"Add New Project"**
3. Import your GitHub repository
4. Configure the project:
   - **Framework Preset**: Other
   - **Root Directory**: `managed-chatkit` (if your repo has multiple folders)
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Output Directory**: `frontend/dist`

5. **Add Environment Variables** (IMPORTANT!):
   - `OPENAI_API_KEY` = `sk-your-actual-api-key`
   - `VITE_CHATKIT_WORKFLOW_ID` = `wf-your-workflow-id`
   
   ⚠️ **Note**: Make sure to add `VITE_CHATKIT_WORKFLOW_ID` (with `VITE_` prefix) so it's available in the frontend build.

6. Click **"Deploy"**

### Option B: Using Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Navigate to your project:
   ```bash
   cd managed-chatkit
   ```

4. Deploy:
   ```bash
   vercel
   ```

5. When prompted, add environment variables:
   - `OPENAI_API_KEY`
   - `VITE_CHATKIT_WORKFLOW_ID`

6. For production deployment:
   ```bash
   vercel --prod
   ```

## Step 4: Verify Deployment

1. After deployment completes, Vercel will provide you with a URL like:
   `https://your-project-name.vercel.app`

2. Visit the URL to test your ChatKit application

3. Open the browser console to check for any errors

## Troubleshooting

### Issue: "Missing workflow id" error

**Solution**: Make sure you've set `VITE_CHATKIT_WORKFLOW_ID` (with `VITE_` prefix) in Vercel environment variables. The `VITE_` prefix is required for Vite to expose it to the frontend.

### Issue: "Missing OPENAI_API_KEY" error

**Solution**: 
1. Go to your Vercel project settings
2. Navigate to "Environment Variables"
3. Add `OPENAI_API_KEY` with your actual API key
4. Redeploy the project

### Issue: API endpoint not found (404)

**Solution**: 
1. Check that `vercel.json` is in the `managed-chatkit` directory
2. Verify the rewrite rule points to `/api/create-session.py`
3. Make sure `api/create-session.py` exists

### Issue: Build fails

**Solution**:
1. Check the build logs in Vercel dashboard
2. Ensure Node.js version is >= 18.18 (check `frontend/package.json`)
3. Make sure all dependencies are listed in `package.json`

## Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key | `sk-...` |
| `VITE_CHATKIT_WORKFLOW_ID` | Yes | Your workflow ID from Agent Builder | `wf_...` |
| `CHATKIT_API_BASE` | No | Custom API base URL | `https://api.openai.com` |
| `VITE_CHATKIT_API_BASE` | No | Custom API base URL (frontend) | `https://api.openai.com` |

## Project Structure

```
managed-chatkit/
├── api/
│   ├── create-session.py    # Serverless function for session creation
│   └── requirements.txt      # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── ChatKitPanel.tsx
│   │   └── lib/
│   │       └── chatkitSession.ts
│   └── package.json
├── vercel.json               # Vercel configuration
└── .env.example              # Environment variables template
```

## Next Steps

- Customize the UI in `frontend/src/components/ChatKitPanel.tsx`
- Add custom styling
- Set up a custom domain in Vercel
- Monitor usage and costs in OpenAI dashboard

## Support

- [OpenAI ChatKit Documentation](https://platform.openai.com/docs/guides/chatkit)
- [Vercel Documentation](https://vercel.com/docs)
- [OpenAI Agent Builder](https://platform.openai.com/agent-builder)
