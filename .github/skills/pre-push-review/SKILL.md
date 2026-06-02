---
name: pre-push-review
description: Review all commits on the current branch before pushing or opening a PR. Use before push, before merge, or when asked for a final review.
allowed-tools:
- shell

---
1. Run `git diff main...HEAD` to see all changes on this branch vs main.
2. If the output is empty, output: "No changes vs main — nothing to review." and stop.
3. Review the full diff for:
- Security vulnerabilities (hardcoded secrets, SQL injection, weak crypto, bare shell execution)
- Violations of `.github/copilot-instructions.md` conventions
- Bad practices: bare `except:`, mutable default arguments, resource leaks
4. Report each issue with: filename, line number, severity (critical/high/medium/low), one-sentence description, one-line fix.
5. End with one of: READY TO PUSH, PUSH WITH MINOR FIXES, or DO NOT PUSH.