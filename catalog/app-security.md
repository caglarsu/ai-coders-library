# App security

Run the AI pentesters (PentAGI, HexStrike AI, Strix, ARTEX, Claude BugHunter) and active scanners (ZAP, Nuclei) only against systems you own or have written permission to test.

### Security Audit Skill
Link: https://github.com/cloudflare/security-audit-skill
Stars: ★ 78.7k
What it does: Cloudflare's skill for multi-phase security audits with independently verified, machine-readable findings.
Use it when: You want your agent to audit your own code with fewer false positives.
Works with: Claude Code and other agents
Install: `npx skills add https://github.com/cloudflare/security-audit-skill`

### Strix
Link: https://github.com/usestrix/strix
Stars: ★ 77.7k
What it does: AI agents that pentest your app, confirm findings with proof-of-concepts and suggest fixes.
Use it when: You want an AI pentest of your own app before release.
Works with: Local code or URL; Docker
Install: `curl -sSL https://strix.ai/install | bash`, then `strix --target ./app`

### Shannon
Link: https://github.com/KeygraphHQ/shannon
Stars: ★ 52.3k
What it does: Autonomous AI pentester for web apps and APIs: reads your source, finds attack paths and runs real exploits to prove each finding. AGPL; Keygraph sells paid tiers.
Use it when: You want proof-backed findings on an app you own before it ships.
Works with: Anthropic, OpenAI, Bedrock and other providers; Docker, Node 22+
Install: `npx @keygraph/shannon@latest`

### Trivy
Link: https://github.com/aquasecurity/trivy
Stars: ★ 39.8k
What it does: Finds vulnerable dependencies, misconfigurations and leaked secrets in repos, containers, Kubernetes and IaC; generates SBOMs.
Use it when: Your assistant adds dependencies or writes Dockerfiles and Terraform, and you want them checked.
Works with: Repos, images, K8s, IaC, CI
Install: `brew install trivy`

### PentAGI
Link: https://github.com/vxcontrol/pentagi
Stars: ★ 35.1k
What it does: Fully autonomous multi-agent penetration testing system with its own web UI and toolset.
Use it when: You run security assessments and want an autonomous agent team doing the legwork.
Works with: Docker; OpenAI, Anthropic, Ollama, Bedrock and others
Install: Download its `docker-compose.yml` and `.env`, then `docker compose up -d`

### Nuclei
Link: https://github.com/projectdiscovery/nuclei
Stars: ★ 33.3k
What it does: Template-driven scanner for known vulnerabilities in web apps, APIs, networks, DNS and cloud.
Use it when: You want to check a deployed app against thousands of community-written exploit templates.
Works with: Any target you are authorised to scan
Install: `brew install nuclei`

### Claude BugHunter
Link: https://github.com/elementalsouls/Claude-BugHunter
Stars: ★ 24.2k
What it does: 84 skills and 15 commands for bug hunting and red-team work, built from 681 disclosed reports.
Use it when: You do authorised bug bounty or red-team work with Claude Code.
Works with: Claude Code
Install: `/plugin marketplace add elementalsouls/Claude-BugHunter` then `/plugin install claude-bughunter@elementalsouls`

### MobSF
Link: https://github.com/MobSF/Mobile-Security-Framework-MobSF
Stars: ★ 22.4k
What it does: Static and dynamic security analysis of Android, iOS and Windows apps.
Use it when: You ship a mobile app and want its build checked before release.
Works with: APK, IPA, APPX
Install: `docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest`

### ARTEX
Link: https://github.com/BaaRai/ARTEX
Stars: ★ 21.9k
What it does: Self-hosted, model-agnostic autonomous pentesting system with evidence-backed findings. AGPL.
Use it when: You want an autonomous pentest of your own systems with proof for every finding.
Works with: Docker; any model provider
Install: `git clone https://github.com/BaaRai/ARTEX.git` then `docker compose up -d --build`

### Semgrep
Link: https://github.com/semgrep/semgrep
Stars: ★ 18k
What it does: Fast static analysis with rules that look like the code they match.
Use it when: You want a pre-merge check on AI-written code, or to hunt every variant of a bug you just fixed.
Works with: 30+ languages, CI
Install: `brew install semgrep` or `pip install semgrep`

### ZAP
Link: https://github.com/zaproxy/zaproxy
Stars: ★ 16.3k
What it does: Dynamic web app scanner and intercepting proxy (OWASP's classic DAST).
Use it when: You want to scan a running web app for XSS, injection and header issues.
Works with: Any web app; Docker, CI
Install: `docker run -t zaproxy/zap-stable zap-baseline.py -t https://your.app`

### HexStrike AI
Link: https://github.com/0x4m4/hexstrike-ai
Stars: ★ 13.9k
What it does: MCP server that lets your AI agent run 150+ security tools for pentesting and bug bounty work.
Use it when: You want Claude or another MCP client to drive nmap, sqlmap and similar tools for you.
Works with: Any MCP client
Install: `git clone https://github.com/0x4m4/hexstrike-ai.git` then `pip install -r requirements.txt`

### BLA
Link: https://github.com/qybaihe/bla
Stars: ★ 7k
What it does: MCP server and CLI that hardens release builds (JS/TS bundles, Electron ASAR, WASM, Python, native binaries, model files) against AI reverse-engineering agents with decoys and obfuscation. Launched October 2026; its benchmarks are the authors' own.
Use it when: You ship closed-source builds and want AI agents to struggle to clone your logic. Run your own tests on the hardened output before shipping.
Works with: Claude Code, Codex, Cursor and any MCP client; Node 22+
Install: `npx bla-agents harden .`, then `--apply` to replace the build

### Opengrep
Link: https://github.com/opengrep/opengrep
Stars: ★ 3.4k
What it does: Open fork of the Semgrep engine for finding security issues in code.
Use it when: You want Semgrep-style rules with a fully open engine.
Works with: 30+ languages, CI
Install: `curl -fsSL https://raw.githubusercontent.com/opengrep/opengrep/main/install.sh | bash`

### OpenRASP
Link: https://github.com/baidu/openrasp
Stars: ★ 3k
What it does: Runtime self-protection agent that blocks attacks from inside the app. Quiet since 2025.
Use it when: You need in-app attack blocking for a Java or PHP service.
Works with: Java, PHP
Install: See the [installation wiki](https://github.com/baidu/openrasp/wiki/Installation)

### Comp AI
Link: https://github.com/trycompai/comp
Stars: ★ 2.1k
What it does: Open-source compliance platform, an alternative to Vanta and Drata: AI collects evidence, writes policies and tracks controls for SOC 2, ISO 27001, HIPAA and GDPR. This is the free, self-hosted Community Edition (AGPL); the managed Comp AI Cloud is paid.
Use it when: You need to get a company compliant and want to self-host the tooling instead of paying for a compliance SaaS.
Works with: Self-host; Node 20+, Bun, Postgres
Install: `git clone https://github.com/trycompai/comp.git`, copy the `.env.example` files, then `bun install`, `bun run docker:up`, `bun run db:migrate` and `bun run dev`

### DongTai IAST
Link: https://github.com/HXSecurity/DongTai
Stars: ★ 1.3k
What it does: Interactive testing that instruments a running Java app to find vulnerabilities while your tests run. Quiet since 2025.
Use it when: You have a Java service and want runtime findings during integration tests.
Works with: Java
Install: See the repo's deployment guide
