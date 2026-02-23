---
description: "Add a new demo feature to an existing hour-N module"
agent: "agent"
tools: ["search/codebase", "read", "edit"]
---

Add a new demo to ${input:hour:demos/hour-1-ai-fundamentals}/main.py.

Before making changes:
1. Read the existing main.py to understand the menu structure and patterns
2. Follow the exact same architecture: frozen dataclass for results, handler function, menu entry
3. Use the same error handling pattern (catch specific SDK exceptions, display via rich, return to menu)
4. Use lazy imports for any new Azure SDK modules
5. Add the new demo to the DEMOS tuple and update the menu numbering

The new demo should: ${input:description:describe what the demo should do}
