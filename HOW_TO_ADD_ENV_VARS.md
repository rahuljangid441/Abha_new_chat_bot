# How to Add Environment Variables in Vercel

## Step-by-Step Guide

### Method 1: During Project Setup (Easiest)

1. **Go to Vercel Dashboard**
   - Visit [vercel.com](https://vercel.com) and sign in

2. **Start New Project**
   - Click **"Add New Project"** button
   - Import your GitHub repository

3. **Configure Project**
   - Set Root Directory to: `managed-chatkit` (if your repo has multiple folders)
   - Scroll down to find **"Environment Variables"** section

4. **Add Your Variables**
   
   Click **"Add"** for each variable:
   
   **Variable 1:**
   - **Key:** `OPENAI_API_KEY`
   - **Value:** `sk-your-actual-api-key` (paste your full API key)
   - **Environment:** Select all (Production, Preview, Development)
   
   **Variable 2:**
   - **Key:** `VITE_CHATKIT_WORKFLOW_ID`
   - **Value:** `wf-your-workflow-id` (paste your workflow ID, it starts with `wf_`)
   - **Environment:** Select all (Production, Preview, Development)
   
   ⚠️ **CRITICAL**: The second variable MUST start with `VITE_` prefix!

5. **Deploy**
   - Click **"Deploy"** button
   - Wait for deployment to complete

---

### Method 2: Add to Existing Project

1. **Go to Your Project**
   - Open your project in Vercel dashboard
   - Click on **"Settings"** tab (top navigation)

2. **Open Environment Variables**
   - Click **"Environment Variables"** in the left sidebar

3. **Add Variables**
   - Click **"Add New"** button
   
   Add first variable:
   - **Key:** `OPENAI_API_KEY`
   - **Value:** `sk-your-actual-api-key`
   - **Environment:** Select all environments
   - Click **"Save"**
   
   Add second variable:
   - **Key:** `VITE_CHATKIT_WORKFLOW_ID`
   - **Value:** `wf-your-workflow-id`
   - **Environment:** Select all environments
   - Click **"Save"**

4. **Redeploy**
   - Go to **"Deployments"** tab
   - Click the **"..."** menu on your latest deployment
   - Click **"Redeploy"**
   - This will apply the new environment variables

---

## What Your Values Should Look Like

### Example API Key:
```
sk-proj-abc123xyz789... (your full key)
```

### Example Workflow ID:
```
wf_abc123def456ghi789 (starts with wf_)
```

---

## Verify It's Working

After deployment, check:

1. **Visit your deployed URL** (e.g., `https://your-project.vercel.app`)
2. **Open browser console** (F12 → Console tab)
3. **Look for errors** - if you see "Missing workflow id" or "Missing OPENAI_API_KEY", the variables aren't set correctly

---

## Troubleshooting

### ❌ Error: "Missing workflow id"
- Make sure you used `VITE_CHATKIT_WORKFLOW_ID` (with `VITE_` prefix)
- Redeploy after adding the variable

### ❌ Error: "Missing OPENAI_API_KEY"
- Check that the variable name is exactly `OPENAI_API_KEY`
- Make sure you selected all environments (Production, Preview, Development)
- Redeploy after adding

### ❌ Variables not updating
- Environment variables require a redeploy to take effect
- Go to Deployments → Redeploy

---

## Security Notes

✅ **DO:**
- Add variables in Vercel dashboard (they're encrypted)
- Use different keys for different environments if needed

❌ **DON'T:**
- Commit API keys to GitHub
- Share your API keys publicly
- Use the same key for multiple projects (if possible)
