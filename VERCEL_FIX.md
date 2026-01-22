# Fixing Vercel Configuration Issues

## Issue 1: Function Runtime Error ✅ FIXED
The error "Function Runtimes must have a valid version" has been fixed by removing the `functions` configuration. Vercel automatically detects Python files in the `api/` directory and uses the correct runtime.

## Issue 2: Root Directory Not Changing

Since the Root Directory dropdown doesn't show "managed-chatkit", you need to **manually type it**:

### Steps:
1. In Vercel project settings, find the **"Root Directory"** field
2. Click the **"Edit"** button next to it
3. **Type** (don't select from dropdown): `managed-chatkit`
4. Press Enter or click outside to save

The field should accept typed input even if the dropdown doesn't show it.

### Alternative: If typing doesn't work

If manually typing doesn't work, you have two options:

**Option A: Move vercel.json to repo root** (already done - there's a vercel.json at repo root)
- But you'll need to adjust the paths

**Option B: Restructure your repo** (recommended for clean setup)
- Move all files from `managed-chatkit/` to the repo root
- This way root directory stays as "./"

## Current Configuration

The `vercel.json` in `managed-chatkit/` is now fixed:
- ✅ Removed `version: 2` (deprecated)
- ✅ Removed `functions` config (Vercel auto-detects Python)
- ✅ Build and output paths are correct

## Next Steps

1. **Try typing "managed-chatkit" in Root Directory field**
2. If that works, deploy!
3. If not, let me know and we'll use Option B
