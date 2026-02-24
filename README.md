# Microsoft Azure AI Fundamentals (AI-900) Certification Prep

![Microsoft Azure AI Fundamentals](images/ai900-cover.png)

[![Website](https://img.shields.io/badge/Website-TechTrainerTim-blue)](https://techtrainertim.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-TimothyWarner-blue?logo=linkedin)](https://www.linkedin.com/in/timothywarner)

Short link: [go.techtrainertim.com/ai900](https://github.com/timothywarner/ai900/)

Official preparation course for the **Microsoft Azure AI Fundamentals (AI-900)** certification exam. O'Reilly live training -- 5 hours, 80% demos, 20% theory.

## Exam Information

- **Exam Code**: AI-900
- **Objectives Updated**: May 2, 2025
- **Official Page**: [Microsoft Learn AI-900](https://learn.microsoft.com/credentials/certifications/azure-ai-fundamentals/)
- **Practice Assessment**: [Free official practice questions](https://learn.microsoft.com/credentials/certifications/exams/ai-900/practice/assessment?assessment-type=practice&assessmentId=26)
- **Exam Sandbox**: [aka.ms/examdemo](https://aka.ms/examdemo)

## Course Flow (5 Segments)

| Segment | Topic | Time | Exam Weight |
|---------|-------|------|-------------|
| S1 | AI Fundamentals & Responsible AI | 09:00 AM | 15-20% |
| S2 | Machine Learning | 10:00 AM | 15-20% |
| S3 | Computer Vision | 11:00 AM | 15-20% |
| S4 | Natural Language Processing | 12:00 PM | 15-20% |
| S5 | **Generative AI** | 01:00 PM | **20-25% (highest)** |

For full objective details, see [AI-900-exam-objectives.md](./docs/AI-900-exam-objectives.md).

## Repository Structure

```text
ai900/
├── .github/                        # GitHub config (CODEOWNERS, templates, Copilot agents)
│   ├── agents/                     # GitHub Copilot agent definitions
│   ├── instructions/               # Copilot custom instructions
│   ├── prompts/                    # Copilot prompt files
│   └── ISSUE_TEMPLATE/
├── bicep/                          # CAF-aligned IaC for lab environment
│   ├── main.bicep
│   ├── modules/                    # ai-services, openai, doc-intel, ML, etc.
│   └── parameters/                 # dev.bicepparam, prod.bicepparam
├── demos/                          # Live class demos (Python + uv)
│   ├── .env.example                # Template for Azure credentials
│   ├── assets/                     # Shared media & datasets (LFS-tracked)
│   │   ├── Audio-Video/
│   │   ├── CSV/
│   │   ├── OCR/
│   │   ├── People/
│   │   ├── Places/
│   │   └── Things/
│   ├── hour-1-ai-fundamentals/     # Vision, Content Safety, Responsible AI
│   ├── hour-2-machine-learning/    # scikit-learn classification/regression/clustering
│   ├── hour-3-computer-vision/     # Image Analysis, OCR, Face, Document Intelligence
│   ├── hour-4-nlp/                 # Sentiment, NER, Speech, CLU
│   └── hour-5-generative-ai/      # GPT-4o, DALL-E 3, prompt engineering, RAG
├── docs/                           # Course materials & exam prep
│   ├── warner-ai900-feb-2026.pptx  # Slide deck (current delivery)
│   ├── AI-900-exam-objectives.md   # Full objective domain
│   ├── AI-900-CORE-RESOURCES.md    # Curated study materials
│   ├── AI-900-PRACTICE-QUESTIONS.md
│   ├── AI-900-PRACTICE-QUESTIONS-SET2.md
│   ├── PRACTICE-QUESTIONS-GUIDE.md # Practice exam resources
│   ├── MCP-DOCS-SERVER-GUIDE.md    # Claude AI + MS Docs for cert prep
│   ├── INDEX.md                    # Guided tour of all materials
│   ├── LEARNING_RESOURCES.md
│   └── exam-metadata/
├── feb-2026/                       # Current delivery course plan
│   ├── course-plan-feb-2026.md
│   └── to-be-archived/            # Legacy content staged for removal
├── images/                         # README cover images
├── practice-questions/             # Practice questions by domain
│   ├── 01-ai-workloads-and-considerations/
│   ├── 02-machine-learning-on-azure/
│   ├── 03-computer-vision-workloads/
│   ├── 04-nlp-workloads/
│   └── 05-generative-ai-workloads/
├── scripts/                        # Utility scripts
│   ├── deploy-ai-services.sh
│   ├── cleanup-ai-services.sh
│   ├── validate-links.py
│   └── github-cli.ps1
└── temp/                           # Temporary working files
```

## Running the Demos

Each demo is a standalone Python project managed with [uv](https://docs.astral.sh/uv/). You need Python 3.13+ and uv installed.

```bash
cd demos/hour-1-ai-fundamentals
uv sync                   # creates .venv and installs dependencies
uv run python main.py     # launches interactive menu
```

Repeat for any `hour-N-*` folder. All demos share a single `demos/.env` file for Azure credentials:

```bash
cp demos/.env.example demos/.env
# Fill in your Azure AI Services keys and endpoints
```

## Bicep Deployment

Deploy the full lab environment with one command:

```bash
az deployment group create \
  --resource-group AI900-Feb2026 \
  --template-file bicep/main.bicep \
  --parameters bicep/parameters/dev.bicepparam
```

## Azure Terminology (Current as of May 2025)

The exam uses current Azure service names exclusively. Deprecated names appear only as **wrong** answers.

| Deprecated Name | Current Name |
|-----------------|--------------|
| Cognitive Services | **Azure AI Services** |
| LUIS | **CLU (Conversational Language Understanding)** |
| QnA Maker | **Custom Question Answering** |
| AI Studio | **Microsoft Foundry** (ai.azure.com) |
| Language Studio | **Deprecated** -- use Microsoft Foundry portal |

## Key Azure Portals

| Portal | URL | Notes |
|--------|-----|-------|
| Azure Portal | portal.azure.com | Resource management |
| Microsoft Foundry | ai.azure.com | Primary for Language, GenAI, model catalog |
| Azure ML Studio | ml.azure.com | AutoML, Designer, endpoints |
| Vision Studio | portal.vision.cognitive.azure.com | Image Analysis, OCR, Face |
| Speech Studio | speech.microsoft.com | Speech-to-text, text-to-speech |
| Custom Vision | customvision.ai | Image classification, object detection |

## Study Resources

### In This Repo

- [Practice Questions Guide](./docs/PRACTICE-QUESTIONS-GUIDE.md) -- 15 practice exam resources and study strategies
- [AI-900 Core Resources](./docs/AI-900-CORE-RESOURCES.md) -- Curated study materials, practice exams, MS Learn paths
- [MCP Microsoft Docs Server Guide](./docs/MCP-DOCS-SERVER-GUIDE.md) -- Use Claude AI + MS Docs for interactive cert prep
- [Docs Index](./docs/INDEX.md) -- Guided tour of all course materials

### Microsoft Learn Path

- [Introduction to AI in Azure](https://learn.microsoft.com/training/paths/get-started-with-artificial-intelligence-on-azure/) -- 14-module learning path covering all five exam domains

### Register for Exam

- [Pearson VUE Exam Registration](https://home.pearsonvue.com/microsoft)
- [Microsoft Certification Deals](https://learn.microsoft.com/credentials/certifications/deals)

## Prerequisites

- Basic understanding of cloud computing concepts
- Microsoft Azure subscription ([free trial](https://azure.microsoft.com/free/) or paid)
- Python 3.13+ and [uv](https://docs.astral.sh/uv/) for running demos
- Interest in artificial intelligence and machine learning

## Instructor

- **Name:** Tim Warner
- **Title:** Microsoft MVP & Certified Trainer
- **Website:** [techtrainertim.com](https://techtrainertim.com)
- **LinkedIn:** [Timothy Warner](https://linkedin.com/in/timothywarner)

## License

This course material is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
