---
name: explain-failures
description: Run pytest and explain every failing test in plain English. Use when tests are failing and the student wants to understand why before fixing.
allowed-tools:
- shell
---
1. Run `python -m pytest --tb=short -v` and capture the full output.
2. If all tests pass, output: "All tests pass." and stop.
3. For each failing test, explain:
    - **Test:** the test function name
    - **Root cause:** one sentence — what the code does vs. what the test expects
    - **Fix hint:** one line — what to change and roughly where
4. Do not fix the code. The goal is understanding, not automation.
5. After listing all failures, ask: "Which failure do you want to tackle first?"