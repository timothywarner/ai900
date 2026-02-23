---
applyTo: "demos/**/*.py"
---

# Python Demo Conventions

- Every demo `main.py` follows the same architecture: `main()` -> menu loop -> handler functions
- Use frozen `@dataclass(frozen=True, slots=True)` for all data structures
- Import Azure SDKs lazily inside handler functions, not at module level
- Use `TYPE_CHECKING` guards for SDK type imports needed only in annotations
- All console output goes through `rich.console.Console` -- never bare `print()`
- Catch `HttpResponseError` and specific SDK exceptions, display via `console.print("[red]...")`, then `return` to menu
- Asset paths use `Path(__file__).resolve().parent.parent / "assets" / ...` -- never hardcode absolute paths
- Environment variables loaded with `_require_env()` helper that calls `sys.exit(1)` with a clear message on missing vars
