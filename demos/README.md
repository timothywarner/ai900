# AI-900 Live Demos

Interactive Python demos for each hour of the AI-900 certification prep course. Each demo is a standalone project with its own dependencies -- run any of them independently in any order.

## Prerequisites

- **Python 3.13+**
- **[uv](https://docs.astral.sh/uv/)** package manager
- **Git LFS** -- binary assets (images, audio) are LFS-tracked. Run `git lfs pull` after cloning.
- **Azure credentials** in `demos/.env` (copy from `.env.example`)

## Quick Start

```bash
cp .env.example .env          # fill in your Azure keys
cd hour-1-ai-fundamentals
uv sync                        # install deps (creates .venv)
uv run python main.py          # launch interactive menu
```

Repeat for any `hour-N-*` folder.

## Demo Index

### Hour 1: AI Fundamentals (15-20% of exam)

**Folder:** `hour-1-ai-fundamentals/`
**Azure services:** Azure AI Vision, Azure AI Content Safety
**Credentials needed:** `AZURE_AI_ENDPOINT`, `AZURE_AI_KEY`

| # | Demo | Azure? | What it shows |
|---|------|--------|---------------|
| 1 | Image Analysis | Yes | Captions, tags, objects, people detection |
| 2 | Content Safety | Yes | Text moderation with severity scores |
| 3 | Responsible AI Quiz | No | 6 RAI principles (FAIR-PT mnemonic) |
| 4 | AI Workload Identifier | No | Match scenarios to AI workload types |

---

### Hour 2: Machine Learning (15-20% of exam)

**Folder:** `hour-2-machine-learning/`
**Azure services:** None -- runs entirely locally with scikit-learn
**Credentials needed:** None

| # | Demo | Azure? | What it shows |
|---|------|--------|---------------|
| 1 | Explore Dataset | No | Bank marketing CSV -- EDA with rich tables |
| 2 | Classification | No | Decision tree on bank marketing data |
| 3 | Regression | No | Linear regression on synthetic data |
| 4 | Clustering | No | K-Means on synthetic blobs |
| 5 | ML Concepts Quiz | No | Regression vs classification vs clustering |

**Asset:** `assets/bankmarketing_train.csv`

---

### Hour 3: Computer Vision (15-20% of exam)

**Folder:** `hour-3-computer-vision/`
**Azure services:** Azure AI Vision, Azure AI Face, Azure AI Document Intelligence
**Credentials needed:** `AZURE_AI_ENDPOINT`, `AZURE_AI_KEY`, `AZURE_DOCINTELL_ENDPOINT`, `AZURE_DOCINTELL_KEY`

| # | Demo | Azure? | What it shows |
|---|------|--------|---------------|
| 1 | Image Analysis | Yes | Landmarks, products, people -- captions and tags |
| 2 | OCR / Read | Yes | Printed text, noisy images, receipts |
| 3 | Face Detection | Yes | Face attributes (age, glasses, head pose) |
| 4 | Document Intelligence | Yes | Invoice field extraction with prebuilt model |
| 5 | Custom Vision Concepts | No | Educational panels + quiz (no API calls) |

**Assets:** 10 files across `assets/Places/`, `assets/Things/`, `assets/People/`, `assets/OCR/`

---

### Hour 4: Natural Language Processing (15-20% of exam)

**Folder:** `hour-4-nlp/`
**Azure services:** Azure AI Language, Azure AI Speech
**Credentials needed:** `AZURE_AI_ENDPOINT`, `AZURE_AI_KEY`

| # | Demo | Azure? | What it shows |
|---|------|--------|---------------|
| 1 | Sentiment Analysis | Yes | Positive/negative/neutral/mixed scoring |
| 2 | Key Phrase Extraction | Yes | Topic identification from text |
| 3 | Named Entity Recognition | Yes | People, places, orgs, dates + PII detection |
| 4 | Language Detection | Yes | Identify language of input text |
| 5 | Speech (STT + TTS) | Yes | Mic input to text, text to neural voice |
| 6 | NLP Concepts Quiz | No | Service selection scenarios |

**Assets:** 2 text files in `assets/OCR/`, 3 WAV files in `assets/Audio-Video/`
**Note:** Speech demo requires a working microphone. Region is hardcoded to `eastus2`.

---

### Hour 5: Generative AI (20-25% of exam -- HIGHEST WEIGHT)

**Folder:** `hour-5-generative-ai/`
**Azure services:** Azure OpenAI Service (GPT-4o, DALL-E 3)
**Credentials needed:** `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_KEY` (GPT); `AZURE_OPENAI_DALLE_ENDPOINT`, `AZURE_OPENAI_DALLE_KEY` (DALL-E, only for Demo 4)

| # | Demo | Azure? | What it shows |
|---|------|--------|---------------|
| 1 | Chat with GPT-4o | Yes | Persona selection, conversation history |
| 2 | Prompt Engineering | Yes | Zero-shot -> few-shot -> chain-of-thought |
| 3 | Temperature Explorer | Yes | Creativity vs determinism slider |
| 4 | DALL-E 3 Images | Yes | Text-to-image generation |
| 5 | Content Filters | Yes | Azure AI content safety categories |
| 6 | RAG Explainer | Yes | Grounded vs ungrounded answers |
| 7 | Generative AI Quiz | No | Exam-style questions on GenAI concepts |

**Assets:** None on disk -- all API-driven. DALL-E outputs saved to `generated_images/` at runtime.

## Shared Configuration

All demos load credentials from a single `demos/.env` file using `python-dotenv` with `find_dotenv()`. See `.env.example` for the full variable list with comments showing which hours use which keys.

| Variable Group | Used By | Service |
|----------------|---------|---------|
| `AZURE_AI_*` | Hours 1, 3, 4 | Multi-service AI resource |
| `AZURE_OPENAI_*` | Hour 5 | GPT-4o completions |
| `AZURE_OPENAI_DALLE_*` | Hour 5 (Demo 4 only) | DALL-E 3 image generation |
| `AZURE_DOCINTELL_*` | Hour 3 (Demo 4 only) | Document Intelligence |

## Shared Assets

All demo assets live in `demos/assets/` (LFS-tracked):

```
assets/
├── Audio-Video/     # WAV files for Speech demos (Hour 4)
├── CSV/             # Spreadsheet samples
├── OCR/             # Text images, receipts, text files (Hours 3, 4)
├── People/          # Face detection images (Hours 1, 3)
├── Places/          # Landmark images (Hour 3)
├── Things/          # Object detection, Custom Vision images (Hour 3)
└── bankmarketing_train.csv   # ML classification dataset (Hour 2)
```

## Troubleshooting

**`uv sync` fails with Python version error** -- You need Python 3.13+. All demos declare `requires-python = ">=3.13"`.

**Images/audio files are tiny text stubs** -- Run `git lfs pull` to download the actual binary files.

**"AZURE_AI_KEY not set"** -- Copy `.env.example` to `.env` and fill in your Azure credentials. The `.env` file must be in the `demos/` directory (not inside individual hour folders).

**Speech demo fails to import** -- The `azure-cognitiveservices-speech` SDK requires native libraries. On some systems you may need to install system-level audio dependencies.
