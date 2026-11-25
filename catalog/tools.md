# Tools

### REA
Link: https://github.com/morluto/rea
Stars: ★ 477.9k
What it does: Reverse engineering with agents, from app behaviour down to native binaries.
Use it when: You need to understand a binary, app bundle or web app you do not have the source for.
Works with: Claude Code, Codex and other agents; MCP
Install: `npx rea-agents setup`

### n8n
Link: https://github.com/n8n-io/n8n
Stars: ★ 212.1k
What it does: Workflow automation with native AI steps and 400+ integrations. Fair-code licence: free to self-host for your own use.
Use it when: You want to wire AI into business workflows visually.
Works with: Self-host or cloud
Install: `docker run -it --rm -p 5678:5678 docker.n8n.io/n8nio/n8n`

### Firecrawl
Link: https://github.com/firecrawl/firecrawl
Stars: ★ 209.6k
What it does: Search, scrape and crawl the web into clean data for agents. AGPL; self-hosting is free, the hosted API is paid.
Use it when: Your agent needs reliable web pages, search results or site crawls as input.
Works with: Any agent; CLI, API, MCP
Install: `npx -y firecrawl-cli@latest scrape https://example.com`

### MarkItDown
Link: https://github.com/microsoft/markitdown
Stars: ★ 198.4k
What it does: Converts PDF, Word, PowerPoint, Excel and more to Markdown for LLMs.
Use it when: You need to feed office documents to an agent.
Works with: Python; MCP
Install: `pip install 'markitdown[all]'`

### Ollama
Link: https://github.com/ollama/ollama
Stars: ★ 188.1k
What it does: Runs open models locally with one command.
Use it when: You want a local model for privacy, offline work or zero API cost.
Works with: macOS, Linux, Windows
Install: `curl -fsSL https://ollama.com/install.sh | sh`

### Dify
Link: https://github.com/langgenius/dify
Stars: ★ 161.9k
What it does: Platform for agentic workflows and RAG pipelines. Modified Apache licence.
Use it when: You want to build and host an LLM app without writing a backend.
Works with: Self-host or cloud
Install: Clone, then `docker compose up -d` in `docker/`

### CC Switch
Link: https://github.com/farion1231/cc-switch
Stars: ★ 157.1k
What it does: Desktop app to manage providers, MCP servers and skills across Claude Code, Codex, OpenCode and others.
Use it when: You switch between agents or model providers often.
Works with: macOS, Windows, Linux
Install: `brew install --cask cc-switch`

### Orca
Link: https://github.com/stablyai/orca
Stars: ★ 137.3k
What it does: Runs a fleet of agents on your own subscriptions, on desktop, mobile or a remote runtime.
Use it when: You want many agents working in parallel without paying for API usage.
Works with: Claude Code, Codex, Grok and others
Install: `brew install --cask stablyai/orca/orca`

### llama.cpp
Link: https://github.com/ggml-org/llama.cpp
Stars: ★ 136.2k
What it does: Fast LLM inference in C/C++ on almost any hardware.
Use it when: You want maximum control and speed running local models.
Works with: CPU, CUDA, Metal, Vulkan
Install: `curl -LsSf https://llama.app/install.sh | sh`

### Browser Use
Link: https://github.com/browser-use/browser-use
Stars: ★ 122k
What it does: Python library for AI browser agents.
Use it when: You build an app or script where an AI drives a browser.
Works with: Python
Install: `pip install browser-use`

### claude-mem
Link: https://github.com/thedotmack/claude-mem
Stars: ★ 119.7k
What it does: Captures what your agent does, compresses it, and brings the relevant parts back next session.
Use it when: Your agent forgets everything between sessions.
Works with: Claude Code and other agents
Install: `npx claude-mem install`

### Agent-Reach
Link: https://github.com/Panniantong/Agent-Reach
Stars: ★ 114.6k
What it does: One CLI for your agent to read and search X, Reddit, YouTube, GitHub and more without API fees.
Use it when: Your agent needs social and video sites as sources.
Works with: Claude Code and other agents
Install: See its README

### Playwright
Link: https://github.com/microsoft/playwright
Stars: ★ 101k
What it does: Web testing and automation across Chromium, Firefox and WebKit.
Use it when: You want your agent to write and run real end-to-end tests.
Works with: Node, Python, Java, .NET
Install: `npm init playwright@latest`

### MCP reference servers
Link: https://github.com/modelcontextprotocol/servers
Stars: ★ 92.2k
What it does: Official reference MCP servers: filesystem, git, memory, fetch and more.
Use it when: You want trusted basic MCP servers, or examples for writing your own.
Works with: Any MCP client
Install: `npx -y @modelcontextprotocol/server-memory` (one per server)

### Crawl4AI
Link: https://github.com/unclecode/crawl4ai
Stars: ★ 87.8k
What it does: Open-source web crawler and scraper that outputs LLM-ready Markdown.
Use it when: Your agent needs web pages as clean input and you want to self-host.
Works with: Python; MCP
Install: `pip install -U crawl4ai`

### RTK
Link: https://github.com/rtk-ai/rtk
Stars: ★ 87.8k
What it does: CLI proxy that cuts token use 60-90% on common dev commands.
Use it when: Your agent burns context on noisy command output.
Works with: Any agent that runs shell commands
Install: `brew install rtk`

### screenshot-to-code
Link: https://github.com/abi/screenshot-to-code
Stars: ★ 81.4k
What it does: Turns a screenshot into clean HTML, Tailwind, React or Vue code.
Use it when: You have a design image and want a coded starting point.
Works with: Docker; Claude, GPT and Gemini
Install: See its README

### Headroom
Link: https://github.com/headroomlabs-ai/headroom
Stars: ★ 80.8k
What it does: Compresses tool output, logs, files and RAG chunks before they reach the model.
Use it when: You want fewer tokens per agent turn without losing accuracy.
Works with: Python; coding agents
Install: `pip install headroom-ai`

### T3 Code
Link: https://github.com/pingdotgg/t3code
Stars: ★ 78.8k
What it does: Control Claude Code, Codex and other agents from any computer or phone.
Use it when: You want to check on or steer your agents when you are away from your desk.
Works with: Claude Code, Codex
Install: `curl -fsSL https://t3.codes/install.sh | sh`

### CodeGraph
Link: https://github.com/colbymchenry/codegraph
Stars: ★ 78.7k
What it does: Pre-indexed code knowledge graph that stays in sync with your code.
Use it when: Your agent spends many turns searching a large codebase.
Works with: Claude Code, Codex, Gemini, Cursor, OpenCode and others
Install: `npm i -g @colbymchenry/codegraph`

### Docling
Link: https://github.com/docling-project/docling
Stars: ★ 71k
What it does: Parses documents, including layout and tables, into AI-ready formats.
Use it when: You need accurate structure from complex PDFs, not just text.
Works with: Python; MCP
Install: `pip install docling`

### Mem0
Link: https://github.com/mem0ai/mem0
Stars: ★ 69.5k
What it does: Memory layer for AI agents and apps.
Use it when: You build an AI product that should remember users across conversations.
Works with: Python, Node; CLI
Install: `pip install mem0ai`

### Context7
Link: https://github.com/upstash/context7
Stars: ★ 65.4k
What it does: Feeds agents up-to-date library documentation.
Use it when: Your agent writes code against outdated APIs.
Works with: Claude Code, Cursor, Codex and others; MCP
Install: `npx ctx7 setup`

### LiteLLM
Link: https://github.com/BerriAI/litellm
Stars: ★ 63.9k
What it does: AI gateway: call 100+ model APIs in one format, with cost tracking and fallbacks.
Use it when: Your app or team uses several model providers.
Works with: Python SDK, proxy server
Install: `uv tool install 'litellm[proxy]'`

### MemPalace
Link: https://github.com/MemPalace/mempalace
Stars: ★ 60.7k
What it does: Free open-source AI memory system with strong benchmark results.
Use it when: You want local, free long-term memory for an agent.
Works with: Claude Code and other agents; Python
Install: `uv tool install mempalace`

### Chrome DevTools MCP
Link: https://github.com/ChromeDevTools/chrome-devtools-mcp
Stars: ★ 59.3k
What it does: Gives agents Chrome DevTools: page inspection, console, network and performance traces.
Use it when: Your agent needs to debug or profile a page in a real browser.
Works with: Any MCP client
Install: `npm i chrome-devtools-mcp@latest -g`

### Open Code Review
Link: https://github.com/alibaba/open-code-review
Stars: ★ 56.3k
What it does: Code review tool combining deterministic checks with an LLM agent, with line-level findings.
Use it when: You want automated AI review on every pull request.
Works with: CLI, CI; agent skill
Install: `npm install -g @alibaba-group/open-code-review`

### agent-browser
Link: https://github.com/vercel-labs/agent-browser
Stars: ★ 53.9k
What it does: Browser automation CLI designed for AI agents.
Use it when: You want your agent to click through a web app from the shell.
Works with: Any agent that runs shell commands
Install: `npm install -g agent-browser`

### colibri
Link: https://github.com/JustVugg/colibri
Stars: ★ 53.4k
What it does: Inference engine in C for large MoE models: hot experts on GPU, warm in RAM, cold streamed from NVMe.
Use it when: You want to run a frontier open-weights model locally on hardware that cannot hold it in VRAM.
Works with: CUDA, Vulkan, macOS
Install: `git clone https://github.com/JustVugg/colibri`, then build per its README

### herdr
Link: https://github.com/herdrdev/herdr
Stars: ★ 52.8k
What it does: Terminal workspace for coding agents: sessions keep running when you detach or lose SSH, every pane shows working, blocked or idle, and agents can spawn and prompt each other.
Use it when: You run several agents at once, or on remote machines, and lose track of which one is waiting on you.
Works with: Claude Code, Codex, Cursor, OpenCode and other terminal agents; macOS, Linux, Windows
Install: `brew install herdr` or `curl -fsSL https://herdr.dev/install.sh | sh`, then `herdr`

### Cua
Link: https://github.com/trycua/cua
Stars: ★ 32.9k
What it does: Open-source computer-use drivers, cross-OS sandboxes and benchmarks.
Use it when: You build or test agents that operate a full desktop, not just a terminal.
Works with: macOS, Linux, Windows sandboxes
Install: `curl -fsSL https://cua.ai/install.sh | sh`

### OpenShell
Link: https://github.com/ai-openshell/openshell
Stars: ★ 21.9k
What it does: Safe, private sandbox runtime for autonomous agents, on your machine or cluster.
Use it when: You let agents run unattended and want them fenced off from the rest of your system.
Works with: Any agent
Install: `curl -LsSf https://raw.githubusercontent.com/ai-openshell/openshell/main/install.sh | sh`

### json-render
Link: https://github.com/vercel-labs/json-render
Stars: ★ 19.8k
What it does: Generative UI framework: the AI answers with a screen built only from your app's components.
Use it when: You want an AI feature that returns UI instead of a paragraph of text.
Works with: React, React Native, shadcn
Install: `npm install @json-render/core @json-render/react`

### Coder
Link: https://github.com/coder/coder
Stars: ★ 17.5k
What it does: Self-hosted secure development environments for developers and their agents. AGPL.
Use it when: Your team wants agents working in governed cloud workspaces instead of laptops.
Works with: Any IDE or agent; Docker, Kubernetes, cloud VMs
Install: `curl -fsSL https://coder.com/install.sh | sh`
