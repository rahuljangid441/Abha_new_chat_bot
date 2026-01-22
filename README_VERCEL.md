# Quick Start: Deploy to Vercel

## 🚀 Quick Deployment Steps

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push
   ```

2. **Deploy on Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New Project"
   - Import your GitHub repo
   - Set Root Directory to: `managed-chatkit` (if needed)

3. **Add Environment Variables in Vercel Dashboard:**
   ```
   OPENAI_API_KEY=sk-your-key-here
   VITE_CHATKIT_WORKFLOW_ID=wf-your-workflow-id-here
   ```
   ⚠️ **Important**: Use `VITE_CHATKIT_WORKFLOW_ID` (with `VITE_` prefix)!

4. **Deploy!** Vercel will give you a live URL.

## 📋 Required Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key
- `VITE_CHATKIT_WORKFLOW_ID` - Your workflow ID from Agent Builder

## 📖 Full Documentation

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions and troubleshooting.
