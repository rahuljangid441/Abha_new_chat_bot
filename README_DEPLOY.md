# Quick Deployment Guide

## Environment Variables Needed

Before deploying, make sure you have:
1. **OPENAI_API_KEY** - Your OpenAI API key (starts with `sk-`)
2. **VITE_CHATKIT_WORKFLOW_ID** - Your workflow ID from Agent Builder (starts with `wf_`)

## Deploy to Vercel

### Method 1: Via Vercel Dashboard (Easiest)

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com) and click "Add New Project"
3. Import your repository
4. **Important**: Set the **Root Directory** to `managed-chatkit`
5. Add environment variables:
   - `OPENAI_API_KEY` = your API key
   - `VITE_CHATKIT_WORKFLOW_ID` = your workflow ID
6. Click Deploy

### Method 2: Via Vercel CLI

```bash
cd managed-chatkit
npm i -g vercel
vercel login
vercel
# Follow prompts and add environment variables when asked
vercel --prod  # For production
```

## After Deployment

Your app will be available at: `https://your-project-name.vercel.app`

See `DEPLOYMENT.md` for detailed instructions and troubleshooting.
