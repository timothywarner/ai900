# 🤖 ✨ Microsoft Azure AI Fundamentals (AI-900) Certification Prep (2nd Edition)

![Microsoft Azure AI Fundamentals](images/ai900-cover.png)

[![Website](https://img.shields.io/badge/Website-TechTrainerTim-blue)](https://techtrainertim.com) [![GitHub](https://img.shields.io/badge/GitHub-timothywarner-blue?logo=github)](https://github.com/timothywarner) [![LinkedIn](https://img.shields.io/badge/LinkedIn-TimothyWarner-blue?logo=linkedin)](https://www.linkedin.com/in/timothywarner)

Short link: [go.techtrainertim.com/ai900](https://github.com/timothywarner/ai900/)

Welcome to the official preparation course for the Microsoft Azure AI Fundamentals (AI-900) certification exam. This training program is designed to help you master Azure AI services and achieve certification. 🎯

## 📝 Exam Information

- **Name**: Microsoft Azure AI Fundamentals
- **Exam Code**: AI-900
- **Last Updated**: May 2, 2025
- **Official Page**: [Microsoft Learn AI-900](https://learn.microsoft.com/credentials/certifications/azure-ai-fundamentals/)

## 📂 Repository Structure - Two Learning Paths

This repository serves learners from two different platforms:

### 🎬 **For MS Press/LinkedIn Learning Students**
- **Folder:** `/ms-press-video-course/`
- **Course:** [Exam AI-900: Microsoft Azure AI Fundamentals (Video)](https://www.microsoftpressstore.com/store/exam-ai-900-microsoft-azure-ai-fundamentals-video-9780138202842)
- **Duration:** 4 hours across 8 lessons
- **Note:** This link is for the 1st edition. The 2nd edition is in production and this link will be updated when available.

### 🚀 **For O'Reilly Live Learning Students**
- **Folder:** `/demos/`
- **Course:** 5-hour live online training
- **Structure:** Hour-by-hour breakdown aligned with May 2025 exam objectives

## 🎓 Course Overview

This course provides hands-on experience and in-depth knowledge of Microsoft Azure AI services, including Azure OpenAI Service, Cognitive Services, Machine Learning, and responsible AI practices.

## 🎯 Certification Exam Domains

| Domain                                                    | Weight     |
|------------------------------------------------------------|------------|
| Describe Artificial Intelligence workloads and considerations | 15-20%     |
| Describe fundamental principles of machine learning on Azure  | 20-25%     |
| Describe features of computer vision workloads on Azure       | 15-20%     |
| Describe features of Natural Language Processing workloads    | 15-20%     |
| Describe features of generative AI workloads on Azure         | 15-20%     |

📄 [Detailed Exam Objectives](./docs/exam-resources/AI-900-exam-objectives.md) | 📚 [All Documentation](./docs/)

## 🎯 Learning Objectives

By completing this course, you will:
- 🚀 Understand core AI concepts and Microsoft's approach to responsible AI
- 💻 Gain practical experience with Azure Machine Learning
- 🔍 Implement computer vision solutions using Azure Cognitive Services
- 🗣️ Build natural language processing solutions with Azure services
- 🤖 Create generative AI solutions with Azure OpenAI Service
- 📝 Prepare effectively for the AI-900 certification exam

## 📚 Official Learning Resources

### Microsoft Learn Paths
- [Get started with artificial intelligence on Azure](https://docs.microsoft.com/en-us/learn/paths/get-started-with-artificial-intelligence-on-azure/)
- [Create no-code predictive models with Azure Machine Learning](https://docs.microsoft.com/en-us/learn/paths/create-no-code-predictive-models-azure-machine-learning/)
- [Explore computer vision in Microsoft Azure](https://docs.microsoft.com/en-us/learn/paths/explore-computer-vision-microsoft-azure/)
- [Explore natural language processing](https://docs.microsoft.com/en-us/learn/paths/explore-natural-language-processing/)
- [Explore Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/explore-azure-openai/)

### Azure Documentation
- [Azure AI Platform](https://azure.microsoft.com/en-us/overview/ai-platform/)
- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services)
- [Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/)
- [Microsoft Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai)

### Practice Resources
- [Official Microsoft AI-900 Sample Questions](https://learn.microsoft.com/credentials/certifications/resources/practice-assessments)
- [Microsoft Learn AI-900 Practice Assessment](https://learn.microsoft.com/credentials/certifications/azure-ai-fundamentals/practice/assessment?assessment-type=practice&assessmentId=26)
- [Whizlabs AI-900](https://www.whizlabs.com/microsoft-azure-certification-ai-900/)
- [MeasureUp AI-900](https://www.measureup.com/ai-900-microsoft-azure-ai-fundamentals.html)

## 🛠️ O'Reilly Live Learning Course Structure (5 Hours)

The `/demos/` folder contains materials for the 5-hour O'Reilly Live Learning course:

### 📚 Hour-by-Hour Breakdown
- **Hour 1: AI Fundamentals & Azure AI Platform** (15-20%)
  - Azure AI services overview, Responsible AI principles, Multi-service demos
- **Hour 2: Machine Learning on Azure** (15-20%)
  - Automated ML, Designer, ML concepts, Transformer architecture
- **Hour 3: Computer Vision Workloads** (15-20%)
  - Computer Vision, Custom Vision, Face API, OCR capabilities
- **Hour 4: Natural Language Processing** (15-20%)
  - Azure AI Language, CLU (replacing LUIS), Custom Question Answering, Speech
- **Hour 5: Generative AI & Azure AI Foundry** (20-25% - Highest!)
  - Azure OpenAI Service, Prompt engineering, Azure AI Foundry platform

## 🚀 **NEW! Unified AI-900 Demo Application**

Experience all Azure AI services through our **Contoso Corporation AI Portal** - a comprehensive Node.js application that demonstrates every service covered in the AI-900 exam!

### ⚡ Quick Start

1. **Clone and Setup**
   ```bash
   git clone https://github.com/timothywarner/ai900.git
   cd ai900
   npm install
   ```

2. **Configure Environment**
   ```bash
   # Copy sample environment file
   cp sample.env .env

   # Edit .env with your Azure AI service credentials
   # Get these from Azure Portal -> Your AI Services -> Keys and Endpoints
   ```

3. **Run the Console Demo**
   ```bash
   npm start
   # or for development with auto-reload and colored logs:
   npm run dev
   ```

4. **Launch Web Interface**
   ```bash
   # In a separate terminal:
   npm run web
   # Open browser to: http://localhost:3000
   
   # Or run with auto-reload:
   npm run dev:web
   ```

### 🎯 Demo Features

**Console Application (`npm start`):**
- Interactive menu-driven interface with educational AI-900 tips
- Enterprise-grade patterns: retry logic, input validation, error handling
- Real-time service health monitoring and metrics
- Uses actual Contoso Corporation branding and scenarios

**Web Application (`npm run web`):**
- **🖼️ Computer Vision**: Upload and analyze images, detect objects, extract text
- **📝 Language Analytics**: Real-time sentiment analysis and key phrase extraction
- **📄 Document Intelligence**: Process receipts and invoices with structured data extraction
- **🤖 Azure OpenAI**: Interactive chat with GPT models
- **📊 Service Metrics**: Monitor API usage and performance
- Beautiful responsive UI with Contoso Corporation branding

### 🔧 Environment Variables Required

See `sample.env` for complete configuration template. Key variables:

```bash
# Multi-Service AI (Recommended - single endpoint for multiple services)
AI_SERVICES_KEY=your_key_here
AI_SERVICES_ENDPOINT=https://your-resource.cognitiveservices.azure.com

# Document Intelligence (for form/receipt processing)
DOCUMENT_INTELLIGENCE_KEY=your_key_here
DOCUMENT_INTELLIGENCE_ENDPOINT=https://your-resource.cognitiveservices.azure.com

# Azure OpenAI Service (requires approved access)
AZURE_OPENAI_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
```

**💡 Pro Tip**: Use the **AI Services multi-service** resource for most demos - it provides access to multiple cognitive services with a single endpoint and key!

### 🎮 Using the Demo App

**Console Interface:**
- Interactive menu with emoji-rich UI
- Demonstrates real AI-900 exam scenarios with educational tips
- Enterprise patterns: retry logic, rate limiting awareness, error handling
- Real-time service health monitoring

**Web Interface:**
- Beautiful Bootstrap 5 UI with Contoso branding
- Upload images and documents for AI analysis
- Real-time text sentiment analysis
- Interactive chat with Azure OpenAI
- Mobile-responsive design

### 🧪 Testing & Quality Assurance

```bash
# Run all tests with coverage
npm test

# Run tests in watch mode during development
npm test:watch

# Run only unit tests
npm test:unit

# Run tests for CI/CD
npm test:ci
```

### 🔒 Security & Port Management

The app includes **automatic port cleanup** on startup:
- Automatically frees port 3000 if in use
- Cross-platform support (Windows/Mac/Linux)
- No manual intervention needed

```bash
# Manual port cleanup if needed
npm run force-close
```

### 📁 Demo Assets Included

- **Images**: Celebrity photos, products, landmarks in `/assets/`
- **Documents**: Sample receipts and invoices for OCR
- **Audio**: Speech samples for voice analysis
- **CSV**: Datasets for ML demonstrations

## 📋 Prerequisites

- 💻 Basic understanding of cloud computing concepts
- 🌐 Familiarity with Microsoft Azure (helpful but not required)
- 🔑 Microsoft Azure subscription (free trial or paid)
- 📝 Interest in artificial intelligence and machine learning
- **🆕 Node.js 18+** (for the unified demo application)

## 👨‍🏫 Instructor Contact

- **Name:** Tim Warner
- **Title:** Microsoft MVP & Certified Trainer
- **Website:** [techtrainertim.com](https://techtrainertim.com)
- **GitHub:** [@timothywarner](https://github.com/timothywarner)
- **LinkedIn:** [Timothy Warner](https://linkedin.com/in/timothywarner)
- **Twitter:** [@TechTrainerTim](https://twitter.com/TechTrainerTim)
- **YouTube:** [Tech Trainer Tim](https://youtube.com/c/TimothyWarner)
- **Email:** [tim@techtrainertim.com](mailto:tim@techtrainertim.com)
- **Microsoft Learn:** [TimothyWarner](https://learn.microsoft.com/users/timothywarner/transcript)

## 🚀 Troubleshooting

**Common Issues:**

1. **Port 3000 already in use**
   - The app automatically handles this on startup
   - Manual fix: `npm run force-close`

2. **Azure service errors**
   - Check your `.env` file has correct keys and endpoints
   - Verify your Azure subscription is active
   - Ensure services are deployed in accessible regions

3. **Module not found errors**
   - Run `npm install` to install all dependencies
   - Delete `node_modules` and run `npm install` again

## 🎓 For Instructors

This demo app is designed for live teaching scenarios:
- All demos work offline with placeholder data if Azure services unavailable
- Educational messages explain AI-900 concepts throughout
- Retry logic demonstrations show production best practices
- Error messages include learning opportunities

## 🏆 Certification Success Tips

1. **Hands-on Practice**: Use this demo app to experiment with each service
2. **Understand Concepts**: Pay attention to the educational tips in the console
3. **Review Metrics**: The app demonstrates monitoring and observability
4. **Security First**: Notice how the app handles credentials and validation

## 💬 License

This course material is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ for AI-900 Success**

[![Tim Warner](https://img.shields.io/badge/Created%20by-Tim%20Warner-blue?style=for-the-badge)](https://techtrainertim.com)
[![Microsoft MVP](https://img.shields.io/badge/Microsoft-MVP-blue?style=for-the-badge&logo=microsoft)](https://mvp.microsoft.com)
[![Certified Trainer](https://img.shields.io/badge/MCT-Certified%20Trainer-orange?style=for-the-badge)](https://learn.microsoft.com/certifications)

</div>
