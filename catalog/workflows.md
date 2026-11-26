# Workflows

Practices that make AI-written code trustworthy, in the order you use them. These are habits, not repos, so they have no stars. Each links to its primary source.

### Spec first, build in a fresh session
Link: https://code.claude.com/docs/en/best-practices
What you do: Have the agent interview you, one question at a time, until you have a `SPEC.md`; then start a new session that builds from it.
Use it when: The task is bigger than one bug fix, or you keep correcting the agent mid-build.
Related on this list: Spec Kit, OpenSpec, Superpowers
More sources: [Harper Reed](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)

### A short instruction file
Link: https://agents.md
What you do: Keep `AGENTS.md` or `CLAUDE.md` to the exact build, test and lint commands, your conventions and the gotchas; leave out anything the agent can read in the code.
Use it when: The agent keeps running the wrong command or breaking the same project rule.
More sources: [Claude Code best practices](https://code.claude.com/docs/en/best-practices)

### One small task, then commit
Link: https://addyosmani.com/blog/ai-coding-workflow/
What you do: Ask for one function, bug or feature at a time and commit after each, so any step can be rolled back. Never commit code you cannot explain.
Use it when: Big asks come back as large diffs you cannot review.
Related on this list: Addy Osmani's agent skills

### Red/green TDD
Link: https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/
What you do: Tell the agent how to run the tests, have it write a test that fails, confirm it fails, then let it write the code that makes it pass.
Use it when: You fix bugs or add logic and want proof it works, plus a guard against regressions.
Related on this list: Superpowers, Matt Pocock's skills
More sources: [Kent Beck](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes)

### Give it a check and ask for evidence
Link: https://code.claude.com/docs/en/best-practices
What you do: Give the agent a command that proves the task is done, and have it show that command and its output, not just say "tests pass".
Use it when: The agent reports success on work that turns out broken.
Related on this list: Playwright

### Review in a fresh context, against the spec
Link: https://code.claude.com/docs/en/best-practices
What you do: Have a separate session or subagent check the change against every requirement and edge case in the spec; tell it to skip style.
Use it when: Before you merge anything the agent wrote.
Related on this list: Open Code Review, Security Audit Skill

### Parallel agents in git worktrees
Link: https://code.claude.com/docs/en/common-workflows
What you do: Give each agent its own worktree and branch (`claude --worktree <name>`), run three or four at most, and merge only what passes review.
Use it when: You have several independent tasks and are waiting on one agent at a time.
Related on this list: Orca, Multica
More sources: [Simon Willison on Git](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/)

### Hard rules in hooks, not prompts
Link: https://code.claude.com/docs/en/best-practices
What you do: Put rules that must never break (no edits to migrations, run the linter after every edit) in hooks and permission settings; the agent can ignore a prompt but not a hook.
Use it when: A rule in your instruction file keeps getting broken.
