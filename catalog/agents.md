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

### Cloudflare OS
Link: https://github.com/cloudflare/cloudflare-os
Stars: ★ 11.9k
What it does: Cloudflare's internal AI workspace: agent chat with company context, sandboxed mini-apps and guardrails.
Use it when: You want to give a whole company safe AI agents and build your own version of it.
Works with: Cloudflare Workers; pnpm
Install: Clone, then `pnpm run-local`
