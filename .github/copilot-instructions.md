# Copilot Instructions

## Repository Purpose

Teaching repo for Tim Warner's O'Reilly AI-900 certification prep course. 5-hour instructor-led class (80% demos, 20% theory). All demo code is Python, all IaC is Bicep.

## Architecture

- Each `demos/hour-N-*` folder is a standalone Python project with its own `pyproject.toml` and `uv.lock`. Do NOT assume shared dependencies between hours.
- Demo pattern: `main.py` drives an interactive menu -> demo handlers -> `rich` UI output -> frozen `@dataclass` objects for data.
- All demos load credentials from `demos/.env` via `python-dotenv` + `find_dotenv()`. Hour 2 is the exception -- runs locally with scikit-learn, no Azure creds needed.
- Binary assets (images, audio, CSVs) are Git LFS tracked under `demos/assets/`.

## Coding Standards

- Python 3.13+ required across all demos
- Use `uv` for dependency management, never pip directly
- Immutable patterns: frozen dataclasses, spread syntax for lists, never mutate
- Full type hints on all function signatures with `from __future__ import annotations`
- `rich` library for all terminal UI (tables, panels, formatted output)
- Error handling: catch specific Azure SDK exceptions, display user-friendly messages, return to menu
- No hardcoded secrets -- always use environment variables via `_require_env()` pattern
- Max function length: 50 lines. Max file length: 800 lines (demo files may stretch to 900)

## Azure Terminology (CRITICAL)

Always use current names. Deprecated names appear ONLY as wrong answers in exam items.

| Deprecated | Current |
|------------|---------|
| Cognitive Services | Azure AI Services |
| LUIS | CLU (Conversational Language Understanding) |
| QnA Maker | Custom Question Answering |
| AI Studio | Microsoft Foundry (ai.azure.com) |
| Form Recognizer | Azure AI Document Intelligence |
| Cognitive Search | Azure AI Search |
| Language Studio | Deprecated -- use Foundry portal |

## Environment Variable Groups

| Prefix | Used by | Service |
|--------|---------|---------|
| `AZURE_AI_*` | Hours 1, 3, 4 | Multi-service AI resource |
| `AZURE_OPENAI_*` | Hour 5 | GPT-4o completions |
| `AZURE_OPENAI_DALLE_*` | Hour 5 (Demo 4) | DALL-E 3 |
| `AZURE_DOCINTELL_*` | Hour 3 (Demo 4) | Document Intelligence |

## Commands

```bash
cd demos/hour-N-whatever && uv sync && uv run python main.py
az deployment group create --resource-group AI900-Feb2026 --template-file bicep/main.bicep --parameters bicep/parameters/dev.bicepparam
python scripts/validate-links.py .
```

## Conventions

- Commit style: present-tense imperative ("Add CV quickstart", "Fix README link")
- Demo folders: `hour-N-topic` naming. Do not invent new top-level structures.
- No automated test suite. Demos are validated by interactive output.
- Practice questions go in `practice-questions/NN-domain-name/` with `<domain>-practice-items.md` naming.
