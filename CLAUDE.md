# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Teaching/learning repository for Tim Warner's live O'Reilly **Microsoft Azure AI Fundamentals (AI-900)** certification prep course. 5-hour instructor-led class (80% demos, 20% theory).

## Repo Structure

```text
ai900/
├── demos/                        # All live class content
│   ├── assets/                   # Shared demo media & datasets (LFS-tracked)
│   │   ├── Audio-Video/          # WAV/MP4 files for Speech demos
│   │   ├── CSV/                  # Spreadsheet samples
│   │   ├── OCR/                  # Text images, invoices, receipts
│   │   ├── People/               # Face detection images
│   │   ├── Places/               # Landmark images
│   │   ├── Things/               # Object detection / Custom Vision images
│   │   └── bankmarketing_train.csv  # AutoML classification dataset
│   ├── .env                      # Live Azure keys (gitignored)
│   ├── .env.example              # Template for learners
│   ├── hour-1-ai-fundamentals/   # Vision, Content Safety, RAI quiz
│   ├── hour-2-machine-learning/  # sklearn classification/regression/clustering
│   ├── hour-3-computer-vision/   # Image Analysis, OCR, Face, Doc Intel
│   ├── hour-4-nlp/               # Sentiment, NER, Speech, CLU concepts
│   └── hour-5-generative-ai/     # GPT-4o, DALL-E 3, prompt engineering, RAG
├── docs/                         # Course materials & exam prep
│   ├── warner-ai900-nov-2025.pptx  # Main slide deck
│   ├── AI-900-exam-objectives.md
│   ├── AI-900-CORE-RESOURCES.md
│   ├── ai900-practice-question-prompt.txt
│   ├── images/                   # README cover images
│   └── exam-metadata/
├── bicep/                        # CAF-aligned IaC for lab environment
├── scripts/                      # validate-links.py, github-cli.ps1
├── feb-2026/                     # Current delivery (course plan, objective domain)
│   └── to-be-archived/           # Old content staged for removal
├── README.md, LICENSE, CONTRIBUTING.md, AGENTS.md
└── images/                       # README badge/cover images
```

## Running Demo Apps

Each demo is a standalone Python project using `uv`:

```bash
cd demos/hour-N-whatever
uv sync                   # creates .venv, installs deps
uv run python main.py     # launches interactive menu
```

All demos share `demos/.env` for Azure credentials (loaded via `find_dotenv()`).

## Bicep Deployment

```bash
az deployment group create \
  --resource-group AI900-Feb2026 \
  --template-file bicep/main.bicep \
  --parameters bicep/parameters/dev.bicepparam
```

## Git LFS

Binary files (`.pptx`, `.pdf`, `.png`, `.jpg`, `.mp4`, `.wav`, `.csv`, `.zip`) are LFS-tracked. Always `git lfs install` before cloning.

## Terminology (Exam Updated May 2025)

- Cognitive Services -> **Azure AI Services**
- LUIS -> **CLU (Conversational Language Understanding)**
- QnA Maker -> **Custom Question Answering**
- AI Studio -> **Azure AI Foundry** (`ai.azure.com`)
- Language Studio -> **Deprecated** (use Foundry portal)
- Generative AI is the **highest-weighted domain** (20-25%)

## Commit Style

Present-tense imperative: "Add CV quickstart", "Fix README link".
