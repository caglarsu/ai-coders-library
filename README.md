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
4. Recommend at most five entries, best fit first. For each give the name, one line on why it fits *this* user, and the **Install** step.
5. If nothing here fits, say so. Do not pad the list.

## Contents

- [Skills](#skills): skill packs and plugins that change how your coding assistant works
- [Agents](#agents): standalone AI agents you run yourself
- [Tools](#tools): CLIs and engines that sit next to your assistant
- [App security](#app-security): scanners and AI pentesters for the code your assistant writes
- [Workflows](#workflows): repeatable practices that make AI-written code trustworthy

## Skills

| Name | What it does | Use it when | Works with | Install |
| ---- | ------------ | ----------- | ---------- | ------- |
| [Superpowers](https://github.com/obra/superpowers) | Skills framework that makes the agent brainstorm, plan, write tests first, debug systematically and verify before claiming done. | Your assistant jumps straight to code, skips tests, or says "fixed" without checking. | Claude Code, Codex, Gemini CLI, OpenCode, Cursor | `/plugin install superpowers@claude-plugins-official` |
| [gstack](https://github.com/garrytan/gstack) | Garry Tan's Claude Code setup: slash commands acting as CEO, eng manager, designer, reviewer, QA with a real browser, security officer and release engineer. | You ship a product alone and want product, design, QA and release roles, not just a coder. | Claude Code (others partly); needs Git and Bun | `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | Makes the agent take the simplest solution that works: stdlib before dependencies, one line before fifty. | Your assistant over-engineers: extra abstractions, new dependencies, boilerplate "for later". | Claude Code, Codex | `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail` |
| [Graphify](https://github.com/Graphify-Labs/graphify) | Turns a codebase, docs, SQL schemas and PDFs into a queryable knowledge graph using local AST parsing, no vector store. | Your repo is large and the agent burns tokens grepping and reading files to find its way. | Claude Code, Cursor, Codex, Gemini CLI | `uv tool install graphifyy`, then `/graphify` in your assistant |
| [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) | Builds an interactive knowledge graph of your code with guided tours, a dashboard and Q&A. | You are new to a codebase, or onboarding someone, and want to see its architecture. | Claude Code, Codex, Cursor, Copilot, Gemini CLI | `/plugin marketplace add Egonex-AI/Understand-Anything` then `/plugin install understand-anything` |
| [CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Generates agent-friendly CLIs for desktop software (CAD, 3D, office, media) and hosts a hub of community-built ones. | You want your agent to drive an app that has no API or CLI of its own. | Claude Code, any agent that runs shell commands | `/plugin marketplace add HKUDS/CLI-Anything` then `/plugin install cli-anything`; hub: `pip install cli-anything-hub` |

## Agents

| Name | What it does | Use it when | Works with | Install |
| ---- | ------------ | ----------- | ---------- | ------- |
| [OpenClaw](https://github.com/openclaw/openclaw) | Personal AI assistant that runs on your machine and acts across your apps and chat platforms. | You want an always-on agent that does tasks for you outside the editor. | Any OS; bring your own model | `npm install -g openclaw@latest` then `openclaw onboard --install-daemon` |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Nous Research's terminal agent with configurable tools and model providers that learns as you use it. | You want an open-source CLI agent and the freedom to pick your own model. | macOS, Linux; many model providers | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| [career-ops](https://github.com/career-ops-hq/career-ops) | Job search agent: scans boards, scores each job against your CV, tailors resume and cover letter, tracks applications. | You are job hunting and want your coding assistant to do the legwork. You still press Submit. | Claude Code, Codex, OpenCode | `npx @santifer/career-ops init` |

## Tools

| Name | What it does | Use it when | Works with | Install |
| ---- | ------------ | ----------- | ---------- | ------- |
| [colibri](https://github.com/JustVugg/colibri) | Inference engine in C for large MoE models: hot experts on GPU, warm in RAM, cold streamed from NVMe. | You want to run a frontier open-weights model locally on hardware that cannot hold it in VRAM. | CUDA, Vulkan, macOS | `git clone https://github.com/JustVugg/colibri`, then build per its README |

## App security

Run the AI pentesters (PentAGI, HexStrike AI, Strix) and active scanners (ZAP, Nuclei) only against systems you own or have written permission to test.

| Name | What it does | Use it when | Works with | Install |
| ---- | ------------ | ----------- | ---------- | ------- |
| [Semgrep](https://github.com/semgrep/semgrep) | Fast static analysis with rules that look like the code they match. | You want a pre-merge check on AI-written code, or to hunt every variant of a bug you just fixed. | 30+ languages, CI | `brew install semgrep` or `pip install semgrep` |
| [Opengrep](https://github.com/opengrep/opengrep) | Open fork of the Semgrep engine for finding security issues in code. | You want Semgrep-style rules with a fully open engine. | 30+ languages, CI | `curl -fsSL https://raw.githubusercontent.com/opengrep/opengrep/main/install.sh \| bash` |
| [Trivy](https://github.com/aquasecurity/trivy) | Finds vulnerable dependencies, misconfigurations and leaked secrets in repos, containers, Kubernetes and IaC; generates SBOMs. | Your assistant adds dependencies or writes Dockerfiles and Terraform, and you want them checked. | Repos, images, K8s, IaC, CI | `brew install trivy` |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | Template-driven scanner for known vulnerabilities in web apps, APIs, networks, DNS and cloud. | You want to check a deployed app against thousands of community-written exploit templates. | Any target you are authorised to scan | `brew install nuclei` |
| [ZAP](https://github.com/zaproxy/zaproxy) | Dynamic web app scanner and intercepting proxy (OWASP's classic DAST). | You want to scan a running web app for XSS, injection and header issues. | Any web app; Docker, CI | `docker run -t zaproxy/zap-stable zap-baseline.py -t https://your.app` |
| [Strix](https://github.com/usestrix/strix) | AI agents that pentest your app, confirm findings with proof-of-concepts and suggest fixes. | You want an AI pentest of your own app before release. | Local code or URL; Docker | `curl -sSL https://strix.ai/install \| bash`, then `strix --target ./app` |
| [PentAGI](https://github.com/vxcontrol/pentagi) | Fully autonomous multi-agent penetration testing system with its own web UI and toolset. | You run security assessments and want an autonomous agent team doing the legwork. | Docker; OpenAI, Anthropic, Ollama, Bedrock and others | Download its `docker-compose.yml` and `.env`, then `docker compose up -d` |
| [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) | MCP server that lets your AI agent run 150+ security tools for pentesting and bug bounty work. | You want Claude or another MCP client to drive nmap, sqlmap and similar tools for you. | Any MCP client | `git clone https://github.com/0x4m4/hexstrike-ai.git` then `pip install -r requirements.txt` |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Static and dynamic security analysis of Android, iOS and Windows apps. | You ship a mobile app and want its build checked before release. | APK, IPA, APPX | `docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest` |
| [DongTai IAST](https://github.com/HXSecurity/DongTai) | Interactive testing that instruments a running Java app to find vulnerabilities while your tests run. Quiet since 2025. | You have a Java service and want runtime findings during integration tests. | Java | See the repo's deployment guide |
| [OpenRASP](https://github.com/baidu/openrasp) | Runtime self-protection agent that blocks attacks from inside the app. Quiet since 2025. | You need in-app attack blocking for a Java or PHP service. | Java, PHP | See the [installation wiki](https://github.com/baidu/openrasp/wiki/Installation) |

## Workflows

None yet.

## Contributing

Open a pull request that adds one row. Fill every column: **Use it when** is what lets an AI match the entry to a reader, so name the situation, not the feature.

## License

[MIT](LICENSE)
