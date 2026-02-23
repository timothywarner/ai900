# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Teaching/learning repository for Tim Warner's live O'Reilly **Microsoft Azure AI Fundamentals (AI-900)** certification prep course. 5-hour instructor-led class (80% demos, 20% theory).

## Running Demo Apps

Each demo is a standalone Python project using `uv`. Requires **Python 3.13+**.

```bash
cd demos/hour-N-whatever
uv sync                   # creates .venv, installs deps
uv run python main.py     # launches interactive menu
```

All demos share `demos/.env` for Azure credentials (loaded via `find_dotenv()`). Copy `demos/.env.example` to `demos/.env` and fill in keys. Hour 2 (ML) is the exception -- it runs locally with scikit-learn and needs no Azure credentials.

## Demo Architecture

All five `main.py` files follow the same pattern:

- **Entry point**: `main()` -> interactive menu loop -> demo handler functions
- **Data**: Frozen `@dataclass` instances (immutable by convention)
- **UI**: `rich` library for colored tables, panels, and formatted output
- **Assets**: Shared media in `demos/assets/` (images, audio, CSVs) -- all LFS-tracked
- **Env vars**: `python-dotenv` with `find_dotenv()` to locate the shared `demos/.env`
- **Type hints**: Full typing with `TYPE_CHECKING` guards for SDK imports

Each hour is fully independent -- own `pyproject.toml`, own `uv.lock`, can run in any order.

### .env Key Groups

| Variable prefix | Used by | Service |
|----------------|---------|---------|
| `AZURE_AI_*` | Hours 1, 3, 4 | Azure AI Services (multi-service key) |
| `AZURE_OPENAI_*` | Hour 5 | GPT-4o completions |
| `AZURE_OPENAI_DALLE_*` | Hour 5 | DALL-E 3 image generation |
| `AZURE_DOCUMENT_*` | Hour 3 | Document Intelligence |
| `AZURE_CUSTOM_VISION_*` | Hour 3 | Custom Vision (training + prediction) |

## Bicep Deployment

CAF-aligned modular IaC in `bicep/`. Modules: ai-services, openai, document-intelligence, search-service, machine-learning, storage-account, key-vault, log-analytics, app-insights.

```bash
az deployment group create \
  --resource-group AI900-Feb2026 \
  --template-file bicep/main.bicep \
  --parameters bicep/parameters/dev.bicepparam
```

## Scripts

- `scripts/validate-links.py` -- Scans all markdown files for broken HTTP links, outputs `link-validation-report.txt`. Run: `python scripts/validate-links.py /path/to/repo`
- `scripts/github-cli.ps1` -- GitHub CLI automation utilities (PowerShell)

## Git LFS

Binary files (`.pptx`, `.pdf`, `.png`, `.jpg`, `.mp4`, `.wav`, `.csv`, `.zip`) are LFS-tracked. Always `git lfs install` before cloning.

## Testing

No automated test suite. Demos are self-validating via interactive console output. Legacy Node.js tests exist in `feb-2026/to-be-archived/` but are not active.

## Terminology (Exam Updated May 2025)

- Cognitive Services -> **Azure AI Services**
- LUIS -> **CLU (Conversational Language Understanding)**
- QnA Maker -> **Custom Question Answering**
- AI Studio -> **Microsoft Foundry** (`ai.azure.com`)
- Language Studio -> **Deprecated** (use Foundry portal)
- Generative AI is the **highest-weighted domain** (20-25%)

## Commit Style

Present-tense imperative: "Add CV quickstart", "Fix README link".
