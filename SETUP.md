# Setup — your live, AI-powered GitHub profile

Your profile README is a small AI app: once a day a GitHub Action calls an LLM
(Llama 3.3 on Groq) and rewrites the "note from my AI" box. Here's how to ship it.

## What's in this folder
```
README.md                          ← your profile (copy to the tharun2511/tharun2511 repo)
scripts/update_profile.py          ← calls the LLM, swaps the AI-note section
.github/workflows/profile-update.yml ← runs it daily + on every push
```

## Steps (~5 min)

### 1. Get a free Groq API key
- Go to https://console.groq.com/keys → **Create API Key** → copy it.
- Groq's free tier is plenty for one call a day.

### 2. Put these files in your profile repo
Copy `README.md`, `scripts/`, and `.github/` into your **`tharun2511/tharun2511`**
repo (the special one whose README shows on your profile). Keep `Banner.png` next to `README.md`.

### 3. Add the key as a repo secret
In the `tharun2511/tharun2511` repo on GitHub:
- **Settings → Secrets and variables → Actions → New repository secret**
- Name: `GROQ_API_KEY`  ·  Value: *(paste your key)*

### 4. Allow Actions to commit
- **Settings → Actions → General → Workflow permissions** → select
  **"Read and write permissions"** → Save.

### 5. Run it once
- **Actions** tab → **Daily AI Profile Update** → **Run workflow**.
- It generates today's line, commits, and your profile updates within a minute.

That's it. It now refreshes every day on its own.

## Good to know
- **No key yet?** The script still works — it writes a sensible fallback line, so the
  README never looks broken. Add the key whenever you're ready.
- **Change the voice/length** of the AI line: edit the `SYSTEM` prompt in
  `scripts/update_profile.py`.
- **Change the schedule:** edit the `cron` in `.github/workflows/profile-update.yml`
  (it's `30 6 * * *` = ~12 PM IST daily).
- **Cost:** one short LLM call per day — effectively free on Groq's free tier.

## One thing worth doing (5 min, big payoff)
Your repos have **no descriptions**, which makes the Featured Projects cards (and your
whole profile) read weaker than they should. On GitHub, open each featured repo →
the ⚙️ gear next to "About" → add a one-line description. Suggested:

- **Audia-ai** — "AI app on an LLM stack: retrieval + agentic reasoning + eval harness."
- **healosbench** — "Evaluation/benchmark harness for LLM outputs — quality as a number."
- **ticket-management-platform** — "Full-stack ticketing platform (typed API + clean UI)."
- **real-time-chat-app** — "Real-time chat with live WebSockets and a dedicated backend."
