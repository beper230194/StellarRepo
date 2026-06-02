---
name: commit-msg
description: Generate a conventional commit message from staged git changes. Use before committing or when asked to write a commit message.
allowed-tools:
- shell
---
1. Run `git diff --staged` to see exactly what has been staged.
2. If nothing is staged, output: "Nothing staged — run `git add` first." and stop.
3. Analyse the diff: what changed, what problem it solves, why it matters.
4. Write a conventional commit message in this exact format:
type(scope): short description under 72 characters
One sentence explaining WHY this change was made, not what changed.
5. Output the commit message only — no explanation, no surrounding text.
Valid types: feat, fix, docs, style, refactor, test, chore.