# Skills

### Matt Pocock's skills
Link: https://github.com/mattpocock/skills
Stars: ★ 332.6k
What it does: Matt Pocock's own engineering skills, straight from his agent setup.
Use it when: You want battle-tested everyday skills from a well-known TypeScript educator.
Works with: Claude Code, Codex
Install: `claude plugin install mattpocock-skills@claude-plugins-official`

### Superpowers
Link: https://github.com/obra/superpowers
Stars: ★ 326.3k
What it does: Skills framework that makes the agent brainstorm, plan, write tests first, debug systematically and verify before claiming done.
Use it when: Your assistant jumps straight to code, skips tests, or says "fixed" without checking.
Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor
Install: `/plugin install superpowers@claude-plugins-official`

### ECC
Link: https://github.com/affaan-m/ECC
Stars: ★ 310.5k
What it does: Agent harness pack: skills, instincts, memory, security checks and research-first development.
Use it when: You want one install that tunes your whole agent setup rather than single skills.
Works with: Claude Code, Codex, OpenCode, Cursor
Install: `npx ecc-universal@2.2.3 setup`

### Karpathy Skills
Link: https://github.com/multica-ai/andrej-karpathy-skills
Stars: ★ 235.6k
What it does: One CLAUDE.md that counters the LLM coding pitfalls Andrej Karpathy described.
Use it when: You want a single drop-in file that makes the agent more careful.
Works with: Claude Code and any agent that reads CLAUDE.md
Install: `curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md`

### Anthropic Skills
Link: https://github.com/anthropics/skills
Stars: ★ 200.3k
What it does: Anthropic's official agent skills: documents, design, testing and more, plus examples to copy.
Use it when: You want the reference skills, or a template for writing your own.
Works with: Claude Code, Claude apps, API
Install: `/plugin marketplace add anthropics/skills`

### Ponytail
Link: https://github.com/DietrichGebert/ponytail
Stars: ★ 198.5k
What it does: Makes the agent take the simplest solution that works: stdlib before dependencies, one line before fifty.
Use it when: Your assistant over-engineers: extra abstractions, new dependencies, boilerplate "for later".
Works with: Claude Code, Codex
Install: `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail`

### UI UX Pro Max
Link: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
Stars: ★ 154k
What it does: Design intelligence skill for professional UI across web and mobile.
Use it when: Your agent's interfaces look amateur and you want design rules applied.
Works with: Claude Code and other agents
Install: `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` then `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`

### Graphify
Link: https://github.com/Graphify-Labs/graphify
Stars: ★ 153.2k
What it does: Turns a codebase, docs, SQL schemas and PDFs into a queryable knowledge graph using local AST parsing, no vector store.
Use it when: Your repo is large and the agent burns tokens grepping and reading files to find its way.
Works with: Claude Code, Cursor, Codex, Gemini CLI
Install: `uv tool install graphifyy`, then `/graphify` in your assistant

### Spec Kit
Link: https://github.com/github/spec-kit
Stars: ★ 151.3k
What it does: GitHub's toolkit for spec-driven development: write the spec, then let the agent build to it.
Use it when: Your agent drifts on larger features and you want a spec it must follow.
Works with: Copilot, Claude Code, Gemini CLI and others
Install: `uv tool install specify-cli`, then `specify init my-project`

### gstack
Link: https://github.com/garrytan/gstack
Stars: ★ 142.6k
What it does: Garry Tan's Claude Code setup: slash commands acting as CEO, eng manager, designer, reviewer, QA with a real browser, security officer and release engineer.
Use it when: You ship a product alone and want product, design, QA and release roles, not just a coder.
Works with: Claude Code (others partly); needs Git and Bun
Install: `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`

### Awesome DESIGN.md
Link: https://github.com/VoltAgent/awesome-design-md
Stars: ★ 129k
What it does: DESIGN.md files distilled from well-known brands' design systems.
Use it when: You want your agent to build UI in a specific, consistent visual style.
Works with: Any agent
Install: Copy a DESIGN.md into your project

### Caveman
Link: https://github.com/JuliusBrussee/caveman
Stars: ★ 122.8k
What it does: Skill and local proxy for shorter answers and smaller tool output, with every original recoverable.
Use it when: You want to cut token spend and wordy replies.
Works with: Claude Code, Codex and other agents
Install: `npx skills add JuliusBrussee/caveman -g`

### Taste Skill
Link: https://github.com/Leonxlnx/taste-skill
Stars: ★ 121.4k
What it does: Gives agents design taste: art direction, reference images and a browser check.
Use it when: You want pages that do not look like generic AI output.
Works with: Claude Code and other agents
Install: `/plugin marketplace add Leonxlnx/taste-skill` then `/plugin install taste-skill@taste-skill`

### Addy Osmani's agent skills
Link: https://github.com/addyosmani/agent-skills
Stars: ★ 120.3k
What it does: 26 production-grade engineering skills, such as code review, testing and performance.
Use it when: You want a broad, well-maintained set of engineering habits for your agent.
Works with: Claude Code, Codex, Cursor and others
Install: `npx skills add addyosmani/agent-skills`

### Impeccable
Link: https://github.com/pbakaus/impeccable
Stars: ★ 116.6k
What it does: Design vocabulary for your agent: commands to polish, critique and audit UI, and a detector for AI-slop design.
Use it when: Your agent builds UI that looks generic and you want it to look designed.
Works with: Claude Code and other agents; Chrome or Edge for page scans
Install: `npx impeccable install`

### Archify
Link: https://github.com/tt-a1i/archify
Stars: ★ 99.8k
What it does: Turns an idea, plan or codebase into a validated interactive architecture diagram.
Use it when: You need architecture, sequence or data-flow diagrams that are checked before you see them.
Works with: Claude Code, Codex, Cursor, OpenCode, Copilot
Install: `npx skills use tt-a1i/archify@archify --agent codex` (swap the agent name)

### Understand Anything
Link: https://github.com/Egonex-AI/Understand-Anything
Stars: ★ 94.3k
What it does: Builds an interactive knowledge graph of your code with guided tours, a dashboard and Q&A.
Use it when: You are new to a codebase, or onboarding someone, and want to see its architecture.
Works with: Claude Code, Codex, Cursor, Copilot, Gemini CLI
Install: `/plugin marketplace add Egonex-AI/Understand-Anything` then `/plugin install understand-anything`

### OpenSpec
Link: https://github.com/Fission-AI/OpenSpec
Stars: ★ 75.7k
What it does: Lightweight spec-driven development for AI coding assistants.
Use it when: You want specs and change proposals without a heavy process.
Works with: Claude Code, Cursor, Codex and others
Install: `npm install -g @fission-ai/openspec@latest`

### last30days
Link: https://github.com/mvanhorn/last30days-skill
Stars: ★ 74.8k
What it does: Researches a topic across Reddit, X, YouTube, Hacker News, Polymarket and the web, then writes a grounded summary.
Use it when: You need to know what people are saying about a tool or topic right now.
Works with: Claude Code and other agents
Install: `/plugin marketplace add mvanhorn/last30days-skill` then `/plugin install last30days`

### Humanizer
Link: https://github.com/blader/humanizer
Stars: ★ 73.4k
What it does: Removes the tell-tale signs of AI-generated writing from text.
Use it when: Your docs, posts or emails read like a chatbot wrote them.
Works with: Claude Code, Codex and others
Install: `/plugin marketplace add blader/humanizer` then `/plugin install humanizer@humanizer`

### Diagram Design
Link: https://github.com/cathrynlavery/diagram-design
Stars: ★ 72.6k
What it does: 52 editorial diagram types as self-contained HTML and SVG, styled to match your site.
Use it when: You want diagrams for docs or a blog that look like they belong there, not like Mermaid.
Works with: Claude Code, Codex, Copilot, Cursor and others
Install: `npx skills add cathrynlavery/diagram-design`

### CLI-Anything
Link: https://github.com/HKUDS/CLI-Anything
Stars: ★ 65.4k
What it does: Generates agent-friendly CLIs for desktop software (CAD, 3D, office, media) and hosts a hub of community-built ones.
Use it when: You want your agent to drive an app that has no API or CLI of its own.
Works with: Claude Code, any agent that runs shell commands
Install: `/plugin marketplace add HKUDS/CLI-Anything` then `/plugin install cli-anything`; hub: `pip install cli-anything-hub`

### Get Shit Done
Link: https://github.com/gsd-build/get-shit-done
Stars: ★ 64.1k
What it does: Meta-prompting, context engineering and spec-driven development system.
Use it when: You want structure for long Claude Code projects without much ceremony.
Works with: Claude Code
Install: See its README

### Marketing Skills
Link: https://github.com/coreyhaines31/marketingskills
Stars: ★ 62.6k
What it does: Marketing skills: conversion, copywriting, SEO, analytics and growth engineering.
Use it when: You built the product and now need landing pages, copy and growth work done well.
Works with: Claude Code and other agents
Install: `npx skills add coreyhaines31/marketingskills`

### i-have-adhd
Link: https://github.com/ayghri/i-have-adhd
Stars: ★ 62.3k
What it does: Makes the agent lead with the next action, number steps and stop burying the answer.
Use it when: Long agent replies lose you, or you want answers you can act on at a glance.
Works with: Claude Code and other agents
Install: `claude plugin marketplace add ayghri/i-have-adhd` then `claude plugin install i-have-adhd@i-have-adhd`

### BMAD Method
Link: https://github.com/bmad-code-org/BMAD-METHOD
Stars: ★ 55.7k
What it does: Agile AI-driven development method with planning, architecture and dev agent roles.
Use it when: You want a full agile process run by agents, from brief to stories to code.
Works with: Claude Code, Cursor and others
Install: `npx bmad-method install`

### Obsidian Skills
Link: https://github.com/obsidianmd/obsidian-skills
Stars: ★ 53.7k
What it does: Teaches your agent Obsidian and open formats: Markdown, Bases, JSON Canvas.
Use it when: You keep notes or docs in Obsidian and want the agent to edit them properly.
Works with: Claude Code and other agents
Install: `claude plugin marketplace add obsidianmd/obsidian-skills` then `claude plugin install obsidian@obsidian-skills`

### rust-anything
Link: https://github.com/erkamyaman/rust-anything
Stars: ★ 9.5k
What it does: Rewrites an app in Rust one piece at a time, checking each step against the original's recorded behaviour.
Use it when: You want to port a TypeScript or Python CLI, server or library to Rust without breaking it.
Works with: Claude Code; Rust toolchain
Install: `cargo install rust-anything`

### App Store Compliance
Link: https://github.com/mjmirza/app-store-compliance
Stars: ★ 6.3k
What it does: Pre-submission guard with 124 documented App Store and Google Play rejection patterns and fixes. Free under $20M yearly revenue.
Use it when: You are about to submit a mobile app and want to avoid a rejection.
Works with: Any agent that reads files
Install: `git clone https://github.com/mjmirza/app-store-compliance`
