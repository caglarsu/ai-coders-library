# AI Coder's Library

Curated skills, tools and workflows for developers who build with AI coding assistants.
Every entry is something we have used and would recommend, with a line on why.

## Ask your AI what fits you

Paste this into your coding assistant:

> Read https://github.com/caglarsu/ai-coders-library and tell me which entries are worth installing for how I work. Ask me what you need to know first.

## For AI assistants reading this

A user sent you this repo to find out which entries suit them. To answer:

1. Find out, if you do not already know: which coding assistant they use, their languages and stack, and what slows them down today.
2. Drop entries whose **Works with** column excludes their assistant.
3. If they ask about security tools, check that they own or are authorised to test the target before recommending an active scanner or AI pentester.
4. Recommend at most five entries, best fit first; when two fit equally, prefer the one with more **Stars**. For each give the name, one line on why it fits *this* user, and the **Install** step.
5. For video and voice models, check the live leaderboards linked in that section; the ranks in this file are a dated snapshot.
6. If nothing here fits, say so. Do not pad the list.

## Contents

- [Skills](#skills): skill packs and plugins that change how your coding assistant works
- [Agents](#agents): standalone AI agents you run yourself
- [Tools](#tools): CLIs and engines that sit next to your assistant
- [Video creation](#video-creation): code-driven video, AI video pipelines, and the best free video and voice models
- [App security](#app-security): scanners and AI pentesters for the code your assistant writes
- [Workflows](#workflows): repeatable practices that make AI-written code trustworthy

## Skills

| Name | Stars | What it does | Use it when | Works with | Install |
| ---- | ----- | ------------ | ----------- | ---------- | ------- |
| [Superpowers](https://github.com/obra/superpowers) | ★ 326.2k | Skills framework that makes the agent brainstorm, plan, write tests first, debug systematically and verify before claiming done. | Your assistant jumps straight to code, skips tests, or says "fixed" without checking. | Claude Code, Codex, Gemini CLI, OpenCode, Cursor | `/plugin install superpowers@claude-plugins-official` |
| [gstack](https://github.com/garrytan/gstack) | ★ 142.6k | Garry Tan's Claude Code setup: slash commands acting as CEO, eng manager, designer, reviewer, QA with a real browser, security officer and release engineer. | You ship a product alone and want product, design, QA and release roles, not just a coder. | Claude Code (others partly); needs Git and Bun | `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | ★ 198.5k | Makes the agent take the simplest solution that works: stdlib before dependencies, one line before fifty. | Your assistant over-engineers: extra abstractions, new dependencies, boilerplate "for later". | Claude Code, Codex | `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail` |
| [Graphify](https://github.com/Graphify-Labs/graphify) | ★ 153.2k | Turns a codebase, docs, SQL schemas and PDFs into a queryable knowledge graph using local AST parsing, no vector store. | Your repo is large and the agent burns tokens grepping and reading files to find its way. | Claude Code, Cursor, Codex, Gemini CLI | `uv tool install graphifyy`, then `/graphify` in your assistant |
| [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) | ★ 94.3k | Builds an interactive knowledge graph of your code with guided tours, a dashboard and Q&A. | You are new to a codebase, or onboarding someone, and want to see its architecture. | Claude Code, Codex, Cursor, Copilot, Gemini CLI | `/plugin marketplace add Egonex-AI/Understand-Anything` then `/plugin install understand-anything` |
| [CLI-Anything](https://github.com/HKUDS/CLI-Anything) | ★ 65.4k | Generates agent-friendly CLIs for desktop software (CAD, 3D, office, media) and hosts a hub of community-built ones. | You want your agent to drive an app that has no API or CLI of its own. | Claude Code, any agent that runs shell commands | `/plugin marketplace add HKUDS/CLI-Anything` then `/plugin install cli-anything`; hub: `pip install cli-anything-hub` |
| [Matt Pocock's skills](https://github.com/mattpocock/skills) | ★ 332.6k | Matt Pocock's own engineering skills, straight from his agent setup. | You want battle-tested everyday skills from a well-known TypeScript educator. | Claude Code, Codex | `claude plugin install mattpocock-skills@claude-plugins-official` |
| [ECC](https://github.com/affaan-m/ECC) | ★ 310.5k | Agent harness pack: skills, instincts, memory, security checks and research-first development. | You want one install that tunes your whole agent setup rather than single skills. | Claude Code, Codex, OpenCode, Cursor | `npx ecc-universal@2.2.3 setup` |
| [Impeccable](https://github.com/pbakaus/impeccable) | ★ 116.6k | Design vocabulary for your agent: commands to polish, critique and audit UI, and a detector for AI-slop design. | Your agent builds UI that looks generic and you want it to look designed. | Claude Code and other agents; Chrome or Edge for page scans | `npx impeccable install` |
| [Archify](https://github.com/tt-a1i/archify) | ★ 99.8k | Turns an idea, plan or codebase into a validated interactive architecture diagram. | You need architecture, sequence or data-flow diagrams that are checked before you see them. | Claude Code, Codex, Cursor, OpenCode, Copilot | `npx skills use tt-a1i/archify@archify --agent codex` (swap the agent name) |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) | ★ 72.6k | 52 editorial diagram types as self-contained HTML and SVG, styled to match your site. | You want diagrams for docs or a blog that look like they belong there, not like Mermaid. | Claude Code, Codex, Copilot, Cursor and others | `npx skills add cathrynlavery/diagram-design` |
| [last30days](https://github.com/mvanhorn/last30days-skill) | ★ 74.8k | Researches a topic across Reddit, X, YouTube, Hacker News, Polymarket and the web, then writes a grounded summary. | You need to know what people are saying about a tool or topic right now. | Claude Code and other agents | `/plugin marketplace add mvanhorn/last30days-skill` then `/plugin install last30days` |
| [rust-anything](https://github.com/erkamyaman/rust-anything) | ★ 9.5k | Rewrites an app in Rust one piece at a time, checking each step against the original's recorded behaviour. | You want to port a TypeScript or Python CLI, server or library to Rust without breaking it. | Claude Code; Rust toolchain | `cargo install rust-anything` |
| [App Store Compliance](https://github.com/mjmirza/app-store-compliance) | ★ 6.2k | Pre-submission guard with 124 documented App Store and Google Play rejection patterns and fixes. Free under $20M yearly revenue. | You are about to submit a mobile app and want to avoid a rejection. | Any agent that reads files | `git clone https://github.com/mjmirza/app-store-compliance` |

## Agents

| Name | Stars | What it does | Use it when | Works with | Install |
| ---- | ----- | ------------ | ----------- | ---------- | ------- |
| [OpenClaw](https://github.com/openclaw/openclaw) | ★ 395.2k | Personal AI assistant that runs on your machine and acts across your apps and chat platforms. | You want an always-on agent that does tasks for you outside the editor. | Any OS; bring your own model | `npm install -g openclaw@latest` then `openclaw onboard --install-daemon` |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | ★ 266k | Nous Research's terminal agent with configurable tools and model providers that learns as you use it. | You want an open-source CLI agent and the freedom to pick your own model. | macOS, Linux; many model providers | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| [career-ops](https://github.com/career-ops-hq/career-ops) | ★ 84.7k | Job search agent: scans boards, scores each job against your CV, tailors resume and cover letter, tracks applications. | You are job hunting and want your coding assistant to do the legwork. You still press Submit. | Claude Code, Codex, OpenCode | `npx @santifer/career-ops init` |
| [Cloudflare OS](https://github.com/cloudflare/cloudflare-os) | ★ 11.9k | Cloudflare's internal AI workspace: agent chat with company context, sandboxed mini-apps and guardrails. | You want to give a whole company safe AI agents and build your own version of it. | Cloudflare Workers; pnpm | Clone, then `pnpm run-local` |

## Tools

| Name | Stars | What it does | Use it when | Works with | Install |
| ---- | ----- | ------------ | ----------- | ---------- | ------- |
| [herdr](https://github.com/herdrdev/herdr) | ★ 52.8k | Terminal workspace for coding agents: sessions keep running when you detach or lose SSH, every pane shows working, blocked or idle, and agents can spawn and prompt each other. | You run several agents at once, or on remote machines, and lose track of which one is waiting on you. | Claude Code, Codex, Cursor, OpenCode and other terminal agents; macOS, Linux, Windows | `brew install herdr` or `curl -fsSL https://herdr.dev/install.sh \| sh`, then `herdr` |
| [colibri](https://github.com/JustVugg/colibri) | ★ 53.4k | Inference engine in C for large MoE models: hot experts on GPU, warm in RAM, cold streamed from NVMe. | You want to run a frontier open-weights model locally on hardware that cannot hold it in VRAM. | CUDA, Vulkan, macOS | `git clone https://github.com/JustVugg/colibri`, then build per its README |
| [T3 Code](https://github.com/pingdotgg/t3code) | ★ 78.8k | Control Claude Code, Codex and other agents from any computer or phone. | You want to check on or steer your agents when you are away from your desk. | Claude Code, Codex | `curl -fsSL https://t3.codes/install.sh \| sh` |
| [Orca](https://github.com/stablyai/orca) | ★ 137.3k | Runs a fleet of agents on your own subscriptions, on desktop, mobile or a remote runtime. | You want many agents working in parallel without paying for API usage. | Claude Code, Codex, Grok and others | `brew install --cask stablyai/orca/orca` |
| [Firecrawl](https://github.com/firecrawl/firecrawl) | ★ 209.6k | Search, scrape and crawl the web into clean data for agents. AGPL; self-hosting is free, the hosted API is paid. | Your agent needs reliable web pages, search results or site crawls as input. | Any agent; CLI, API, MCP | `npx -y firecrawl-cli@latest scrape https://example.com` |
| [OpenShell](https://github.com/ai-openshell/openshell) | ★ 21.9k | Safe, private sandbox runtime for autonomous agents, on your machine or cluster. | You let agents run unattended and want them fenced off from the rest of your system. | Any agent | `curl -LsSf https://raw.githubusercontent.com/ai-openshell/openshell/main/install.sh \| sh` |
| [Cua](https://github.com/trycua/cua) | ★ 32.9k | Open-source computer-use drivers, cross-OS sandboxes and benchmarks. | You build or test agents that operate a full desktop, not just a terminal. | macOS, Linux, Windows sandboxes | `curl -fsSL https://cua.ai/install.sh \| sh` |
| [Coder](https://github.com/coder/coder) | ★ 17.5k | Self-hosted secure development environments for developers and their agents. AGPL. | Your team wants agents working in governed cloud workspaces instead of laptops. | Any IDE or agent; Docker, Kubernetes, cloud VMs | `curl -fsSL https://coder.com/install.sh \| sh` |
| [json-render](https://github.com/vercel-labs/json-render) | ★ 19.8k | Generative UI framework: the AI answers with a screen built only from your app's components. | You want an AI feature that returns UI instead of a paragraph of text. | React, React Native, shadcn | `npm install @json-render/core @json-render/react` |
| [REA](https://github.com/morluto/rea) | ★ 477.9k | Reverse engineering with agents, from app behaviour down to native binaries. | You need to understand a binary, app bundle or web app you do not have the source for. | Claude Code, Codex and other agents; MCP | `npx rea-agents setup` |

## Video creation

Tools here have more than 30,000 stars.

| Name | Stars | What it does | Use it when | Works with | Install |
| ---- | ----- | ------------ | ----------- | ---------- | ------- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | ★ 89.9k | HeyGen's open-source video editor: your agent writes HTML compositions and renders them to MP4. | You want Claude Code or Codex to make promos, explainers or captioned clips from a prompt, a URL or your footage. | Claude Code, Codex; Node | `npx skills add heygen-com/hyperframes`, then `npx hyperframes init my-video` |
| [Remotion](https://github.com/remotion-dev/remotion) | ★ 75.6k | Make videos programmatically with React components. | You know React and want data-driven or templated videos rendered in code or CI. Companies above 3 people need a paid licence. | Node, React; agent skills at `remotion-dev/skills` | `npx create-video@latest` |
| [Manim](https://github.com/3b1b/manim) | ★ 96.9k | 3Blue1Brown's engine for precise animated maths and diagrams. | You explain an algorithm or concept and want exact, code-defined animation. | Python | `pip install manimgl` |
| [anime.js](https://github.com/juliangarnier/anime) | ★ 75.1k | Lightweight JavaScript animation engine. | You need motion graphics inside an HTML or web composition (HyperFrames supports it). | Browser, Node | `npm install animejs` |
| [OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | ★ 83.2k | Agentic video production system with production pipelines, tools and agent skills. AGPL. | You want an agent to run a whole production: script, assets, edit, render. | Claude Code and other agents | `git clone https://github.com/OpenMontageInc/OpenMontage.git`, then follow its README |
| [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | ★ 145.6k | Generates a finished short video (script, stock footage, voice, subtitles, music) from a topic. | You need many short vertical videos fast and stock footage is acceptable. | Docker; OpenAI, DeepSeek, Ollama and others | `git clone https://github.com/harry0703/MoneyPrinterTurbo.git`, then `docker compose -f docker-compose.release.yml up` |
| [Pixelle-Video](https://github.com/ATH-MaaS/Pixelle-Video) | ★ 30.5k | Fully automated short-video engine with AI-generated visuals. | You want topic-to-video like MoneyPrinterTurbo but with generated images and clips instead of stock footage. | Python, FFmpeg, ComfyUI | `git clone https://github.com/ATH-MaaS/Pixelle-Video.git`, then `uv run streamlit run web/app.py` |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | ★ 148.6k | Node-graph GUI and API for running diffusion models, including the open video models below. | You want to run open-weights video models on your own GPU, or chain generation steps. | NVIDIA, AMD, Apple silicon | Desktop app from comfy.org, or clone and `pip install -r requirements.txt` |
| [VoiceStudio](https://github.com/debpalash/VoiceStudio) | ★ 118.1k | Fully local voice cloning, voice design and video dubbing. AGPL. | Your video needs a voiceover or dub and you do not want to send audio to a cloud API. Clone only voices you have consent for. | macOS, Linux, Windows | `brew install --cask debpalash/tap/voicestudio` |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | ★ 68.2k | The encoder, decoder and filter engine underneath almost every tool here. | Your agent needs to cut, convert, resize, subtitle or stitch video from the command line. | Every OS | `brew install ffmpeg` |
| [OBS Studio](https://github.com/obsproject/obs-studio) | ★ 80.1k | Screen recording and live streaming. | You record product demos, tutorials or bug repros. | macOS, Windows, Linux | `brew install --cask obs` |
| [LosslessCut](https://github.com/mifi/lossless-cut) | ★ 46.4k | Trims and splits video without re-encoding, so it is instant and keeps full quality. | You need to cut a long recording into clips quickly. | macOS, Windows, Linux | `brew install --cask losslesscut` |

### Best free video generation models

Only open-weights models you can download and run without paying; closed and API-only models are left out. Ranks are from the [Artificial Analysis](https://artificialanalysis.ai/video/leaderboard/text-to-video) blind-vote boards, read on 2026-11-25. They move monthly, so check the live [text-to-video](https://artificialanalysis.ai/video/leaderboard/text-to-video) and [image-to-video](https://artificialanalysis.ai/video/leaderboard/image-to-video) boards. Run any of them locally with ComfyUI.

| Model | Maker | Rank | Licence | Use it when |
| ----- | ----- | ---- | ------- | ----------- |
| [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) | MiniMax | #3 text-to-video (Elo 1164), #6 image-to-video (1135); best free model | Free in the EU, UK, US and South Korea. Above $20M yearly revenue you need MiniMax's written permission; commercial products must show "MiniMax H3" | You want the best quality you can run yourself. |
| [Hyperflow H3](https://huggingface.co/VideoRebirthAI/hyperflow) | Video Rebirth | #4 text-to-video (1156), #10 image-to-video (1120) | Same licence as MiniMax H3 | You want a second H3-based model to compare. |
| [Pika H3 Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex) | Pika | #16 text-to-video (1123), #13 image-to-video (1116) | Same licence as MiniMax H3 | You mostly animate still images. |
| [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | Lightricks | #32 text-to-video (938), #35 image-to-video (914) | Free for companies under $10M yearly revenue; paid licence above | You want video and audio generated together in one pass. |
| [Wan 2.2](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B) | Alibaba | Not on the boards | Apache-2.0: free for any use, no revenue cap, region or attribution rule | You need a licence with no conditions at all. |

### Best free voice models

Text-to-speech models with open weights and a licence that allows commercial use. Ranks are from the [Artificial Analysis speech arena](https://artificialanalysis.ai/text-to-speech/leaderboard), read on 2026-11-25; check the live board before you commit. Fish Audio Drama 3 (#9) and Breeze TTS 2 (#15) rank higher but are research or non-commercial only, so they are left out. VoiceStudio, above, runs models like these locally.

| Model | Maker | Rank | Licence | Use it when |
| ----- | ----- | ---- | ------- | ----------- |
| [Ming-3.0-tts](https://huggingface.co/inclusionAI/Ming-3.0-tts-0.5B) | Ant Group | #27 (Elo 1180); best free model | MIT | You want the best free voice quality, in English, Chinese, Japanese, Korean or major European languages. |
| [Phonon 31M](https://huggingface.co/gradium/phonon-31m-en) | Gradium | #46 (1109) | Apache-2.0 | You need English speech from a tiny model on modest hardware. |
| [Kokoro 82M](https://huggingface.co/hexgrad/Kokoro-82M) | hexgrad | #68 (1061) | Apache-2.0 | You want a small, fast, widely supported voice model for narration. |
| [Maya1](https://huggingface.co/maya-research/maya1) | Maya Research | #74 (1049) | Apache-2.0 | You want to describe a voice in words and add emotions like laughter or whispering. |
| [Chatterbox](https://huggingface.co/ResembleAI/chatterbox) | Resemble AI | #87 (1021) | MIT | You need to clone a voice from a short sample, in many languages. Clone only voices you have consent for. |
| [VibeVoice 1.5B](https://huggingface.co/microsoft/VibeVoice-1.5B) | Microsoft | #91 (955) | MIT | You generate long, multi-speaker audio such as a podcast or dialogue. |

## App security

Run the AI pentesters (PentAGI, HexStrike AI, Strix, ARTEX, Claude BugHunter) and active scanners (ZAP, Nuclei) only against systems you own or have written permission to test.

| Name | Stars | What it does | Use it when | Works with | Install |
| ---- | ----- | ------------ | ----------- | ---------- | ------- |
| [Semgrep](https://github.com/semgrep/semgrep) | ★ 17.9k | Fast static analysis with rules that look like the code they match. | You want a pre-merge check on AI-written code, or to hunt every variant of a bug you just fixed. | 30+ languages, CI | `brew install semgrep` or `pip install semgrep` |
| [Opengrep](https://github.com/opengrep/opengrep) | ★ 3.4k | Open fork of the Semgrep engine for finding security issues in code. | You want Semgrep-style rules with a fully open engine. | 30+ languages, CI | `curl -fsSL https://raw.githubusercontent.com/opengrep/opengrep/main/install.sh \| bash` |
| [Trivy](https://github.com/aquasecurity/trivy) | ★ 39.7k | Finds vulnerable dependencies, misconfigurations and leaked secrets in repos, containers, Kubernetes and IaC; generates SBOMs. | Your assistant adds dependencies or writes Dockerfiles and Terraform, and you want them checked. | Repos, images, K8s, IaC, CI | `brew install trivy` |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | ★ 33.3k | Template-driven scanner for known vulnerabilities in web apps, APIs, networks, DNS and cloud. | You want to check a deployed app against thousands of community-written exploit templates. | Any target you are authorised to scan | `brew install nuclei` |
| [ZAP](https://github.com/zaproxy/zaproxy) | ★ 16.3k | Dynamic web app scanner and intercepting proxy (OWASP's classic DAST). | You want to scan a running web app for XSS, injection and header issues. | Any web app; Docker, CI | `docker run -t zaproxy/zap-stable zap-baseline.py -t https://your.app` |
| [Strix](https://github.com/usestrix/strix) | ★ 77.5k | AI agents that pentest your app, confirm findings with proof-of-concepts and suggest fixes. | You want an AI pentest of your own app before release. | Local code or URL; Docker | `curl -sSL https://strix.ai/install \| bash`, then `strix --target ./app` |
| [PentAGI](https://github.com/vxcontrol/pentagi) | ★ 35k | Fully autonomous multi-agent penetration testing system with its own web UI and toolset. | You run security assessments and want an autonomous agent team doing the legwork. | Docker; OpenAI, Anthropic, Ollama, Bedrock and others | Download its `docker-compose.yml` and `.env`, then `docker compose up -d` |
| [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) | ★ 13.9k | MCP server that lets your AI agent run 150+ security tools for pentesting and bug bounty work. | You want Claude or another MCP client to drive nmap, sqlmap and similar tools for you. | Any MCP client | `git clone https://github.com/0x4m4/hexstrike-ai.git` then `pip install -r requirements.txt` |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | ★ 22.3k | Static and dynamic security analysis of Android, iOS and Windows apps. | You ship a mobile app and want its build checked before release. | APK, IPA, APPX | `docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest` |
| [DongTai IAST](https://github.com/HXSecurity/DongTai) | ★ 1.3k | Interactive testing that instruments a running Java app to find vulnerabilities while your tests run. Quiet since 2025. | You have a Java service and want runtime findings during integration tests. | Java | See the repo's deployment guide |
| [OpenRASP](https://github.com/baidu/openrasp) | ★ 3k | Runtime self-protection agent that blocks attacks from inside the app. Quiet since 2025. | You need in-app attack blocking for a Java or PHP service. | Java, PHP | See the [installation wiki](https://github.com/baidu/openrasp/wiki/Installation) |
| [Claude BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | ★ 22.3k | 84 skills and 15 commands for bug hunting and red-team work, built from 681 disclosed reports. | You do authorised bug bounty or red-team work with Claude Code. | Claude Code | `/plugin marketplace add elementalsouls/Claude-BugHunter` then `/plugin install claude-bughunter@elementalsouls` |
| [ARTEX](https://github.com/BaaRai/ARTEX) | ★ 20k | Self-hosted, model-agnostic autonomous pentesting system with evidence-backed findings. AGPL. | You want an autonomous pentest of your own systems with proof for every finding. | Docker; any model provider | `git clone https://github.com/BaaRai/ARTEX.git` then `docker compose up -d --build` |

## Workflows

None yet.

## Contributing

Open a pull request that adds one row. Fill every column except **Stars**, which a daily job updates from GitHub. **Use it when** is what lets an AI match the entry to a reader, so name the situation, not the feature.

## License

[MIT](LICENSE)
