"""
Daily profile updater.

Calls an LLM (Llama 3.3 on Groq) to write a fresh one-liner for the README,
then swaps it into the AI-note section between the marker comments.

This is intentionally small and dependency-free (uses only the stdlib) so the
GitHub Action stays fast and never breaks on a missing package.

Env vars:
  GROQ_API_KEY  - required. Free key from https://console.groq.com/keys
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

README_PATH = "README.md"
START = "<!--START_SECTION:ai-note-->"
END = "<!--END_SECTION:ai-note-->"

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"

SYSTEM = (
    "You write a single short line (max ~18 words) for Tharun's GitHub profile. "
    "Tharun is a Full Stack & AI Engineer who builds RAG systems, LLM agents, and "
    "eval harnesses with React/Next.js/Node/NestJS and Python. "
    "The line should sound like a real engineer's daily thought about building AI "
    "or full-stack software - specific, a little opinionated, never corporate or "
    "hype. No hashtags, no emojis, no quotation marks. Just the sentence."
)
USER = "Write today's line."

FALLBACK = "Building AI features the honest way: measure quality before you trust it."


def generate_line() -> str:
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        print("No GROQ_API_KEY set; using fallback line.", file=sys.stderr)
        return FALLBACK

    payload = json.dumps(
        {
            "model": MODEL,
            "temperature": 0.9,
            "max_tokens": 60,
            "messages": [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": USER},
            ],
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        GROQ_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        line = data["choices"][0]["message"]["content"].strip()
        line = line.strip('"').strip()
        return line or FALLBACK
    except (urllib.error.URLError, KeyError, ValueError) as exc:
        print(f"LLM call failed ({exc}); using fallback line.", file=sys.stderr)
        return FALLBACK


def build_block(line: str) -> str:
    return (
        f"{START}\n"
        f"> _“{line}”_\n\n"
        f"<sub>\U0001f7e2 auto-generated · powered by Llama 3.3 on Groq · "
        f"updates daily via GitHub Actions</sub>\n"
        f"{END}"
    )


def main() -> int:
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    line = generate_line()
    new_block = build_block(line)

    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(readme):
        print("Marker section not found in README.md", file=sys.stderr)
        return 1

    updated = pattern.sub(lambda _: new_block, readme)

    if updated == readme:
        print("No change.")
        return 0

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"Updated AI note: {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
