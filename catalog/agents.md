# Agents

### OpenClaw
Link: https://github.com/openclaw/openclaw
Stars: ★ 395.2k
What it does: Personal AI assistant that runs on your machine and acts across your apps and chat platforms.
Use it when: You want an always-on agent that does tasks for you outside the editor.
Works with: Any OS; bring your own model
Install: `npm install -g openclaw@latest` then `openclaw onboard --install-daemon`

### Hermes Agent
Link: https://github.com/NousResearch/hermes-agent
Stars: ★ 266.1k
What it does: Nous Research's terminal agent with configurable tools and model providers that learns as you use it.
Use it when: You want an open-source CLI agent and the freedom to pick your own model.
Works with: macOS, Linux; many model providers
Install: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`

### Paperclip
Link: https://github.com/paperclipai/paperclip
Stars: ★ 117.1k
What it does: App for managing a team of AI agents at work: roles, tasks and oversight.
Use it when: You run several agents on real business work and need to organise them.
Works with: Claude Code, Codex and others
Install: `npx paperclipai@latest onboard --yes`

### OpenDesign
Link: https://github.com/nexu-io/open-design
Stars: ★ 109.5k
What it does: Collaborative AI design workspace: start from a brief and let your coding agent build prototypes, websites and motion that follow your design system. A paid cloud plan also exists.
Use it when: You want design work done by the coding agent you already use, with templates and design systems.
Works with: Claude Code, Codex and other agent CLIs it finds on your machine; macOS, Windows, Linux from source
Install: Desktop app from open-design.ai or its GitHub releases

### MiroFish
Link: https://github.com/666ghj/MiroFish
Stars: ★ 86.7k
What it does: Multi-agent simulation engine: give it seed material such as news, a policy draft or a story, and it builds a world of AI agents, runs the simulation and writes a report you can question. AGPL.
Use it when: You want to rehearse how people might react to an event, a policy or a plot. Treat the output as a simulation, not a forecast, and start with short runs: it uses a lot of LLM tokens.
Works with: Any OpenAI-compatible LLM API, Zep Cloud for memory; Docker. [MiroFish-Offline](https://github.com/nikmcfly/MiroFish-Offline) runs it on Ollama and Neo4j instead.
Install: `git clone https://github.com/666ghj/MiroFish.git`, `cp .env.example .env` and add your LLM and Zep keys, then `docker compose up -d`

### career-ops
Link: https://github.com/career-ops-hq/career-ops
Stars: ★ 84.9k
What it does: Job search agent: scans boards, scores each job against your CV, tailors resume and cover letter, tracks applications.
Use it when: You are job hunting and want your coding assistant to do the legwork. You still press Submit.
Works with: Claude Code, Codex, OpenCode
Install: `npx @santifer/career-ops init`

### Ruflo
Link: https://github.com/ruvnet/ruflo
Stars: ★ 82.4k
What it does: Agent harness for Claude Code and Codex: runs swarms of agents on one task, with plugins and an MCP server.
Use it when: You want several agents to split up and work through a big task together.
Works with: Claude Code, Codex; Node
Install: `npx ruflo@latest init` in your project, then give Claude Code a task

### AI Job Search
Link: https://github.com/ai-job-search-dev/ai-job-search
Stars: ★ 73.5k
What it does: Job application framework on Claude Code: scrapes postings, ranks the fits, tailors your CV and cover letters, and prepares interviews.
Use it when: You are job hunting and want a structured, local workflow. Keep your copy private: `/setup` writes your personal data into tracked files.
Works with: Claude Code; Python 3.10+, Bun, LaTeX
Install: Clone it into a private repo (steps in its README), then run `claude` and `/setup`

### DeepTutor
Link: https://github.com/HKUDS/DeepTutor
Stars: ★ 62.8k
What it does: Personal AI tutor: chat about your own documents, solve problems step by step, generate questions, and track what you have learned.
Use it when: You learn from papers, books or course material and want a tutor that remembers you.
Works with: Hosted and local models; desktop app (macOS, Windows), Docker or pip
Install: `docker run --rm -p 127.0.0.1:3782:3782 -v deeptutor-data:/app/data ghcr.io/hkuds/deeptutor:latest`, or the desktop app from its releases

### Multica
Link: https://github.com/multica-ai/multica
Stars: ★ 57.9k
What it does: Workspace where you assign issues to coding agents like teammates: they pick up work, report progress, raise blockers and hand it back for review. Apache-2.0 with extra terms: hosting it for others needs a paid licence, and the branding must stay.
Use it when: You run several agent CLIs and want one board to give them work and track it.
Works with: Claude Code, Codex and other agent CLIs; desktop app or self-host
Install: Desktop app from multica.ai/download, or self-host: `curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --with-server`, then `multica setup self-host`

### nanobot
Link: https://github.com/HKUDS/nanobot
Stars: ★ 50.3k
What it does: Lightweight, self-hosted personal AI agent in Python: chat from the browser, terminal or chat apps, with files, memory, tools and scheduled tasks.
Use it when: You want your own small assistant on a laptop or cheap server.
Works with: Hosted and local model providers; Python 3.11+
Install: `curl -fsSL https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.sh | sh`

### Comp AI CRM
Link: https://github.com/trycompai/crm
Stars: ★ 12.3k
What it does: Agent-first CRM from the Comp AI team: an agent runs on its own schedule, researches contacts and companies, and writes only facts it has evidence for; weak evidence becomes a suggestion for a person to confirm. Works with no data-vendor keys, using your own emails and meetings.
Use it when: You want a self-hosted CRM where an agent keeps records up to date instead of your sales team.
Works with: Self-host on Bun, Postgres and Docker; built for Vercel (AI Gateway, Sandbox)
Install: `git clone https://github.com/trycompai/crm.git && cd crm`, `cp .env.example .env`, `bun install`, `docker compose up -d`, `bun run db:deploy`, then `bun run dev`

### Cloudflare OS
Link: https://github.com/cloudflare/cloudflare-os
Stars: ★ 11.9k
What it does: Cloudflare's internal AI workspace: agent chat with company context, sandboxed mini-apps and guardrails.
Use it when: You want to give a whole company safe AI agents and build your own version of it.
Works with: Cloudflare Workers; pnpm
Install: Clone, then `pnpm run-local`
