---
name: review-file

description: Review a named file for bugs, security vulnerabilities, and copilot-instructions.md violations. Use when asked to review, audit, or find problems in a file.
allowed-tools:
- shell
---
The user will name a file to review. Follow these steps:
1. Read the named file in full.
2. Read `.github/copilot-instructions.md` to load the project's coding conventions.
3. Review the file and report every issue with:
- Severity: critical / high / medium / low
- Exact line number(s)
- One-sentence description of the problem
- One-line fix suggestion
4. End with a verdict on one line: APPROVE, APPROVE WITH SUGGESTIONS, or REQUEST CHANGES.
5. Do not modify the file — report only. The developer decides what to apply.