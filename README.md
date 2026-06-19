<!-- ╔══════════════════════════════════════════════════════════════════════╗ -->
<!-- ║                          T H A R U N . a g e n t                       ║ -->
<!-- ║          README rendered as an AI agent's system definition            ║ -->
<!-- ╚══════════════════════════════════════════════════════════════════════╝ -->

<p align="center">
  <img src="./Banner.png" width="100%" alt="Tharun Guduguntla — Full Stack & AI Engineer" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1100&color=00A2FF&center=true&vCenter=true&width=720&height=45&lines=%3E+booting+tharun.agent...;%3E+loading+context%3A+2%2B+yrs+full-stack+%2B+AI;%3E+tools+ready%3A+RAG+%C2%B7+agents+%C2%B7+MCP+%C2%B7+pgvector;%3E+status%3A+online+%E2%80%94+ask+me+anything+%F0%9F%9F%A2" alt="boot sequence" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/tharun-guduguntla"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:gtharun2511@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://github.com/tharun2511"><img src="https://img.shields.io/badge/GitHub-171515?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <img src="https://komarev.com/ghpvc/?username=tharun2511&label=context+loads&color=00A2FF&style=flat-square" alt="Profile views" />
  <img src="https://img.shields.io/badge/based_in-Hyderabad_%F0%9F%87%AE%F0%9F%87%B3-1f2937?style=flat-square" alt="Location" />
</p>

---

### `> system_prompt`

```python
agent = Engineer(
    name        = "Tharun Guduguntla",
    role        = "Full Stack & AI Engineer",
    experience  = "2+ years shipping scalable web & full-stack systems",
    now         = "building production LLM features from first principles",
    superpower  = "turning fuzzy LLM ideas into reliable, evaluated systems",
)

agent.system_prompt = """
You are Tharun. You design front-to-back: clean React/Next.js UIs, typed
Node/NestJS services, and Postgres data layers — then you make them think.
You don't bolt an API onto a product and call it 'AI'. You build retrieval,
tools, and evals from the ground up, because you've seen what breaks without them.
Default to shipping. Measure before you trust. Keep learning, relentlessly.
"""
```

---

### `> render: how_i_build_llm_features()`

> Not a stock diagram — this is the retrieval + agentic pipeline I actually wire up.

```mermaid
flowchart LR
    Q([User Query]) --> EMB[Embed]
    Q --> KW[Keyword / BM25]
    EMB --> VEC[(pgvector)]
    VEC --> RRF{{Hybrid Fusion · RRF}}
    KW --> RRF
    RRF --> RANK[Cross-Encoder Re-rank]
    RANK --> CTX[[Grounded Context]]
    CTX --> LLM((LLM + Tools))
    LLM -->|function call| MCP[/Tools · MCP server/]
    MCP -->|observation| LLM
    LLM --> STREAM[[Stream · SSE]]
    STREAM --> UI([React UI])
    EVAL{{Eval Harness}} -.scores.-> LLM

    classDef ai fill:#00A2FF,stroke:#0077cc,color:#fff,stroke-width:1px;
    classDef data fill:#1f2937,stroke:#374151,color:#e5e7eb;
    classDef io fill:#111827,stroke:#00A2FF,color:#fff;
    class LLM,RANK,RRF,EMB ai;
    class VEC,MCP,EVAL data;
    class Q,UI,CTX,STREAM,KW io;
```

---

### `> agent.tools` — what I expose to the world

<table>
<tr>
<td width="50%" valign="top">

#### 🤖 `ai_engineering`
```jsonc
{
  "rag":        "embeddings + pgvector",
  "retrieval":  "hybrid search · RRF · re-rank",
  "agents":     "function-calling · ReAct loops",
  "protocol":   "MCP server (from scratch)",
  "orchestration": "LangChain · LangGraph",
  "quality":    "eval harnesses · prompt eng",
  "streaming":  "token-by-token over SSE",
  "models":     "Groq · Gemini · Llama 3.3"
}
```

</td>
<td width="50%" valign="top">

#### 🧱 `full_stack`
```jsonc
{
  "frontend":  "React · Next.js · Redux · Tailwind",
  "backend":   "Node.js · NestJS · Express",
  "api":       "REST · GraphQL · microservices",
  "data":      "PostgreSQL · MongoDB",
  "realtime":  "WebSockets · maps · live dashboards",
  "cloud":     "AWS · Docker · Linux",
  "lang":      "TypeScript · JavaScript · Python · Java",
  "roots":     "DSA · OOP · system design"
}
```

</td>
</tr>
</table>

---

### `> stack.index` — the retrieval index behind those tools

<p align="center">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" />
  <br/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Redux-764ABC?style=for-the-badge&logo=redux&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" />
  <br/>
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/NestJS-E0234E?style=for-the-badge&logo=nestjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white" />
  <img src="https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white" />
  <br/>
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</p>

---

### `> agent.query(topic)` — expand a context window

<details>
<summary><b>🔎 "How do you stop a RAG app from hallucinating?"</b></summary>

<br/>

Retrieval quality first — garbage context guarantees garbage answers. I run
**hybrid search** (semantic over pgvector + keyword/BM25), fuse with **RRF**, then
**cross-encoder re-rank** the top candidates so the model only sees the strongest
evidence. Then I make the model *cite* what it used, and I wrap the whole thing in an
**eval harness** so "it feels better" becomes a number I can defend.

</details>

<details>
<summary><b>🤖 "What's the hardest part of building an agent?"</b></summary>

<br/>

Not the function calling — it's the **loop**. Deciding when to call a tool, feeding
observations back cleanly, knowing when to stop, and handling the model going off the
rails. That's why I went deep on **LangGraph** (StateGraph, persistence, human-in-the-loop)
and built an **MCP server from scratch** — to actually understand the contract between
model and tools instead of trusting a black box.

</details>

<details>
<summary><b>🧱 "Are you AI or full-stack?"</b></summary>

<br/>

Both — and that's the point. The hard part of production AI isn't the prompt; it's the
**system around it**: the typed API, the streaming UI, the data layer, the failure modes.
2+ years of shipping React/Next.js + Node/NestJS means I can take an LLM feature from
idea to a thing real users can rely on — UI to vector store and back.

</details>

---

### `> metrics.dashboard`

<p align="center">
  <img width="48%" src="https://github-readme-stats.vercel.app/api?username=tharun2511&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&include_all_commits=true" alt="GitHub Stats" />
  <img width="48%" src="https://github-readme-stats.vercel.app/api/top-langs?username=tharun2511&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="Top Languages" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=tharun2511&theme=tokyonight&hide_border=true" alt="Streak" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=tharun2511&theme=tokyo-night&hide_border=true&area=true&color=00A2FF&line=00A2FF&point=ffffff" alt="Activity Graph" />
</p>

<!-- SNAKE: requires the Platane/snk GitHub Action committing to an `output` branch.
     Workflow file: .github/workflows/snake.yml  (setup steps at the bottom of this README) -->
<p align="center">
  <img src="https://raw.githubusercontent.com/tharun2511/tharun2511/output/github-contribution-grid-snake-dark.svg" alt="Contribution snake" />
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=tharun2511&theme=tokyonight&no-frame=true&no-bg=true&margin-w=8&margin-h=8&column=7" alt="Trophies" />
</p>

---

### `> agent.status`

```diff
+ Open to:   Full Stack & AI Engineering roles · LLM product collaboration
+ Building:  RAG + agentic systems, eval-driven, shipped end to end
! Mindset:   build from first principles · measure before you trust
```

<p align="center">
  <a href="mailto:gtharun2511@gmail.com"><img src="https://img.shields.io/badge/Say_hello-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/tharun-guduguntla"><img src="https://img.shields.io/badge/Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
</p>

<p align="center">
  <sub><code>// end of context window — always building, always learning. ⭐</code></sub>
</p>

<!-- ════════════════════════ SNAKE SETUP (delete this comment after) ═════════════════════════
Create .github/workflows/snake.yml in the tharun2511/tharun2511 repo:

name: Generate Snake
on:
  schedule: [{ cron: "0 */12 * * *" }]
  workflow_dispatch:
  push: { branches: [main] }
jobs:
  generate:
    runs-on: ubuntu-latest
    permissions: { contents: write }
    steps:
      - uses: Platane/snk/svg-only@v3
        with:
          github_user_name: tharun2511
          outputs: |
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v4
        with: { target_branch: output, build_dir: dist }
        env: { GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} }
═══════════════════════════════════════════════════════════════════════════════════════════ -->
