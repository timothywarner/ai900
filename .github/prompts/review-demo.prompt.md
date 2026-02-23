---
description: "Audit a demo module for completeness and correctness"
agent: "ask"
tools: ["search/codebase", "read"]
---

Audit the demo at ${input:path:demos/hour-1-ai-fundamentals/main.py} for:

1. **Dependencies**: Do pyproject.toml deps match all imports?
2. **Environment variables**: Are all needed vars documented in demos/.env.example?
3. **Asset files**: Do all referenced files exist under demos/assets/?
4. **Code quality**: Any missing error handling, hardcoded paths, or type annotation gaps?
5. **Will it run?**: Can a learner clone this repo and run `uv sync && uv run python main.py` successfully?

Produce a structured pass/fail report for each category.
