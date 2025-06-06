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

The repository serves two distinct audiences with separate content paths:

```
demos/                           # O'Reilly Live Learning 5-hour course
├── hour-1-ai-fundamentals/     # AI workloads & considerations (15-20%)
├── hour-2-machine-learning/    # ML principles on Azure (15-20%)
├── hour-3-computer-vision/     # Computer vision workloads (15-20%)
├── hour-4-nlp/                # Natural Language Processing (15-20%)
└── hour-5-generative-ai/      # Generative AI workloads (20-25% - HIGHEST!)

ms-press-video-course/          # MS Press/LinkedIn Learning 4-hour video course
├── README.md                   # Course overview and structure
└── lessons/                    # 8 lessons aligned with April 2024 objectives
    ├── lesson-01/             # Common AI workloads
    ├── lesson-02/             # Responsible AI principles
    ├── lesson-03/             # Machine learning techniques
    ├── lesson-04/             # Azure Machine Learning capabilities
    ├── lesson-05/             # Computer vision solutions
    ├── lesson-06/             # NLP workload scenarios
    ├── lesson-07/             # Generative AI features
    └── lesson-08/             # Azure OpenAI Service

apps/                           # Complete demo applications
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
   - `/assets/Audio-Video/` - Speech and video analysis samples
   - `/assets/OCR/` - Document samples for OCR demos
   - `/assets/People/`, `/Places/`, `/Things/` - Image samples for vision demos
   - `/assets/CSV/` - Datasets for ML demos

## Course Structures

### O'Reilly Live Learning (5 hours) - `/demos/`
- Hour 1: AI Fundamentals & Azure AI Platform (15-20%)
- Hour 2: Machine Learning on Azure (15-20%) - includes Transformer architecture
- Hour 3: Computer Vision Workloads (15-20%)
- Hour 4: Natural Language Processing (15-20%) - CLU & Custom QA
- Hour 5: Generative AI & Azure AI Foundry (20-25% - HIGHEST!)

### MS Press Video Course (4 hours) - `/ms-press-video-course/`
- Lesson 1: Identify features of common AI workloads (30 min)
- Lesson 2: Identify guiding principles for responsible AI (30 min)
- Lesson 3: Identify common machine learning techniques (30 min)
- Lesson 4: Describe Azure Machine Learning capabilities (30 min)
- Lesson 5: Identify common types of computer vision solutions (30 min)
- Lesson 6: Identify features of common NLP workload scenarios (30 min)
- Lesson 7: Identify features of generative AI solutions (30 min)
- Lesson 8: Identify capabilities of Azure OpenAI Service (40 min)

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

## Repository Maintenance Notes

1. **Git LFS**: Previously used for binary files but has been removed. The repository now uses standard Git for all files.

2. **Two Course Paths**: 
   - O'Reilly learners should use `/demos/` (5-hour live course)
   - MS Press/LinkedIn Learning viewers should use `/ms-press-video-course/` (4-hour video course)

3. **Important Files**:
   - Root `README.md` clearly explains both learning paths
   - `/ms-press-video-course/README.md` contains the MS Press course structure
   - This `CLAUDE.md` file guides AI assistance for the repository