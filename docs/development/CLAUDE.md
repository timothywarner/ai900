# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is an educational repository for the Microsoft Azure AI Fundamentals (AI-900) certification exam, updated for the May 2025 exam objectives. It's structured as a 5-hour O'Reilly Live Learning course with practical demonstrations (80% demos, 20% theory) aligned with current certification requirements.

## Key Commands

### Node.js Applications

For Bot Framework applications (`/apps/azure_bots/my-chat-bot/`):
```bash
npm install          # Install dependencies
npm start           # Run the bot
npm run watch       # Run with auto-restart
npm run lint        # Run ESLint
```

For Computer Vision SDK demos (`/apps/compvision-js-sdk/`):
```bash
npm install          # Install dependencies
node ComputerVisionQuickstart.js  # Run the demo
```

### Python Applications

Python demos don't have centralized dependency management. Each script lists required packages in its docstring. Common pattern:
```bash
pip install azure-cognitiveservices-vision-computervision
pip install azure-ai-textanalytics
pip install pillow
python <script_name>.py
```

### Azure Service Configuration

All demos require Azure service credentials. Follow this pattern:
1. Replace `YOUR_KEY` placeholders with actual Azure service keys
2. Replace `YOUR_ENDPOINT` placeholders with service endpoints
3. For `.env` files, copy `sample.env` to `.env` and fill in values

## Architecture & Organization

The repository follows a 5-hour course structure aligned with May 2025 AI-900 exam objectives:

```
demos/                           # Primary demo content organized by course hours
├── hour-1-ai-fundamentals/     # AI workloads & considerations (15-20%)
├── hour-2-machine-learning/    # ML principles on Azure (15-20%)
├── hour-3-computer-vision/     # Computer vision workloads (15-20%)
├── hour-4-nlp/                # Natural Language Processing (15-20%)
└── hour-5-generative-ai/      # Generative AI workloads (20-25% - HIGHEST!)

apps/                           # Complete demo applications
lessons/                        # Legacy materials (being phased out)
```

## Important Development Notes

1. **Educational Focus**: All code is designed for teaching Azure AI services. Demos should be clear, well-commented, and follow the configuration placeholder pattern.

2. **No Central Build System**: Each demo is self-contained. There are no repository-wide build, test, or lint commands.

3. **Azure Services Used (Updated May 2025)**:
   - Azure AI Services (formerly Cognitive Services)
   - Azure AI Language (includes CLU, Custom Question Answering)
   - Azure AI Vision, Azure AI Speech
   - Azure Machine Learning (Automated ML, Designer)
   - Azure OpenAI Service
   - Azure AI Foundry (unified platform)
   - Azure Bot Service

4. **Configuration Pattern**: All demos use placeholder values that must be replaced:
   - `YOUR_KEY` → Actual service key
   - `YOUR_ENDPOINT` → Service endpoint URL
   - `YOUR_DEPLOYMENT_NAME` → Model deployment name

5. **Media Assets**: The repository includes sample files for demos:
   - `/Audio-Video/` - Speech and video analysis samples
   - `/OCR/` - Document samples for OCR demos
   - `/People/`, `/Places/`, `/Things/` - Image samples for vision demos
   - `/CSV/` - Datasets for ML demos

## Course Structure

The course is designed for a 5-hour O'Reilly Live Learning session:
- Hour 1: AI Fundamentals & Azure AI Platform (15-20%)
- Hour 2: Machine Learning on Azure (15-20%) - includes Transformer architecture
- Hour 3: Computer Vision Workloads (15-20%)
- Hour 4: Natural Language Processing (15-20%) - CLU & Custom QA
- Hour 5: Generative AI & Azure AI Foundry (20-25% - HIGHEST!)

## Key Updates for May 2025 Exam

1. **Service Rebranding**:
   - Cognitive Services → Azure AI Services
   - LUIS → Conversational Language Understanding (CLU)
   - QnA Maker → Custom Question Answering
   - Text Analytics → Azure AI Language
   - Form Recognizer → Azure AI Document Intelligence

2. **New Content**:
   - Azure AI Foundry platform
   - Transformer architecture in ML
   - Increased focus on Generative AI (now highest weighted domain)

When creating or modifying demos, ensure they use current service names and align with May 2025 exam objectives.