# Week 3 — AI Dev Workflow Lab
## Stack
- Python 3.11+, pytest for all tests, stdlib only
## Conventions
- Type hints on all functions
- One-line docstring on every public function
- Raise specific exceptions (ValueError, TypeError) — never bare `except:`
- No print statements outside `if __name__ == "__main__"`
## Do Not
- Use eval() or exec()
- Hardcode secrets or file paths
- Suppress exceptions silently
## AI Instructions
- Make one small change at a time, explain it before applying
- Run tests after every change
- Flag any security-related code and ask for human review