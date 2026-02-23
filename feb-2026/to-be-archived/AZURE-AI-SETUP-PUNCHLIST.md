# 🚀 Azure AI Services Setup Punchlist for Live Training

**Quick Reference:** Use this checklist to pre-provision all Azure AI services before your 4-hour live class.

> **Pro Tip:** Create all services in the same resource group (e.g., `AI900-LiveTraining`) and same region (e.g., `East US`) for easier management and lower latency.

## 📋 Pre-Class Setup Checklist

### 1. Azure Subscription & Resource Group
- [ ] **Azure Subscription** - Ensure you have credits available (~$50 recommended)
- [ ] **Resource Group** - Create `AI900-LiveTraining` in your preferred region
- [ ] **Region Selection** - Use `East US` or `West Europe` (best Azure OpenAI availability)

### 2. Core Azure AI Services (Multi-Service)
- [ ] **Azure AI Services (Multi-Service)**
  - Name: `ai900-aiservices`
  - Pricing Tier: `S0` (Standard)
  - Covers: Vision, Language, Speech, Decision
  - **Save:** Endpoint URL and Key

### 3. Azure OpenAI Service (Hour 5 - Highest Priority!)
- [ ] **Azure OpenAI Service**
  - Name: `ai900-openai`
  - Region: Check [availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)
  - Pricing Tier: `S0`
  - **Deploy Models:**
    - [ ] GPT-4 deployment: `gpt-4-deployment`
    - [ ] GPT-3.5 Turbo deployment: `gpt-35-turbo-deployment`
    - [ ] DALL-E 3 deployment: `dalle3-deployment`
  - **Save:** Endpoint, Key, and Deployment Names

### 4. Azure Machine Learning (Hour 2)
- [ ] **Azure Machine Learning Workspace**
  - Name: `ai900-mlworkspace`
  - **Associated Resources (auto-created):**
    - Storage Account
    - Key Vault
    - Application Insights
    - Container Registry (optional)
  - [ ] **Compute Instance** - Create `Standard_DS11_v2` (2 cores, 14GB RAM)
  - [ ] **Sample Datasets** - Ensure titanic, automobile-price datasets are accessible

### 5. Computer Vision Specific (Hour 3)
- [ ] **Custom Vision Service** (if demonstrating custom models)
  - Training Resource: `ai900-customvision-training`
  - Prediction Resource: `ai900-customvision-prediction`
  - Pricing Tier: `S0` for both
  - [ ] **Sample Project** - Create "Product Detection" with 5-10 sample images

### 6. Language Services (Hour 4)
- [ ] **Language Studio Access**
  - URL: [language.cognitive.azure.com](https://language.cognitive.azure.com)
  - [ ] **CLU Project** - Create "PizzaOrder" intent classification
  - [ ] **Custom Q&A** - Import sample knowledge base
  - [ ] **Entity Recognition** - Test with sample documents

### 7. Additional Services
- [ ] **Azure Bot Service** (Optional for demos)
  - Name: `ai900-bot`
  - Bot Type: Web App Bot
  - Pricing Tier: `F0` (Free)

### 8. Speech Services (if needed)
- [ ] **Speech Service Key** (covered by multi-service, but note region)
- [ ] **Voice Gallery Access** - Bookmark [speech.microsoft.com](https://speech.microsoft.com)

## 🔑 Service Credentials Template

Create a `credentials.md` file (⚠️ ADD TO .gitignore!) with this template:

```markdown
# Azure AI Services Credentials (DO NOT COMMIT!)

## Multi-Service AI
- Endpoint: https://ai900-aiservices.cognitiveservices.azure.com/
- Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

## Azure OpenAI
- Endpoint: https://ai900-openai.openai.azure.com/
- Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
- GPT-4 Deployment: gpt-4-deployment
- GPT-3.5 Deployment: gpt-35-turbo-deployment
- DALL-E Deployment: dalle3-deployment

## Azure ML Workspace
- Workspace: ai900-mlworkspace
- Resource Group: AI900-LiveTraining
- Subscription ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

## Custom Vision
- Training Endpoint: https://ai900-customvision-training.cognitiveservices.azure.com/
- Training Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
- Prediction Endpoint: https://ai900-customvision-prediction.cognitiveservices.azure.com/
- Prediction Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## 🎯 Demo Preparation Checklist

### Hour 1: AI Fundamentals
- [ ] Test multi-service endpoint with Postman/cURL
- [ ] Prepare Responsible AI discussion examples
- [ ] Bookmark [Azure AI Demo Gallery](https://azure.microsoft.com/products/ai-services/ai-demos/)

### Hour 2: Machine Learning
- [ ] Upload sample CSV to ML workspace
- [ ] Create one AutoML run (takes ~20 min, do before class)
- [ ] Designer pipeline template ready
- [ ] Transformer architecture slides/examples

### Hour 3: Computer Vision
- [ ] Test images ready in `/assets/` folders
- [ ] Vision Studio bookmarked: [portal.vision.cognitive.azure.com](https://portal.vision.cognitive.azure.com)
- [ ] OCR demo documents prepared
- [ ] Face API ethical use disclaimer ready

### Hour 4: NLP
- [ ] Language Studio projects created
- [ ] Sample utterances for CLU (10-15 examples)
- [ ] Q&A knowledge base with 5-10 Q&A pairs
- [ ] Text samples for sentiment/entity extraction

### Hour 5: Generative AI (25% of exam!)
- [ ] Azure OpenAI Studio access: [oai.azure.com](https://oai.azure.com)
- [ ] Prompt engineering examples prepared
- [ ] DALL-E demo prompts ready
- [ ] Azure AI Foundry (formerly AI Studio) tour ready
- [ ] Content filter discussion points

## 🛠️ Troubleshooting Tips

1. **Quota Issues**: If you hit OpenAI quota limits, have backup region ready
2. **CORS Errors**: Use Azure-provided playgrounds when possible
3. **Auth Failures**: Double-check key/endpoint pairs, ensure no trailing slashes
4. **Region Mismatch**: Keep all services in same region for demos
5. **Spending Limits**: Set up cost alerts at $25 and $40

## 📱 Quick Access Links for Live Demo

Bookmark these for quick access during training:

- **Azure Portal**: [portal.azure.com](https://portal.azure.com)
- **Vision Studio**: [portal.vision.cognitive.azure.com](https://portal.vision.cognitive.azure.com)
- **Language Studio**: [language.cognitive.azure.com](https://language.cognitive.azure.com)
- **ML Studio**: [ml.azure.com](https://ml.azure.com)
- **OpenAI Studio**: [oai.azure.com](https://oai.azure.com)
- **Speech Studio**: [speech.microsoft.com](https://speech.microsoft.com)
- **AI Foundry**: [ai.azure.com](https://ai.azure.com)

## 🚨 Emergency Backup Plan

If Azure services fail during demo:
1. **Recorded Demo Videos** - Have 2-3 min clips of each service
2. **Screenshots** - Full workflow screenshots in `/assets/demo-screenshots/`
3. **Postman Collection** - Pre-configured API calls that work offline
4. **Local Jupyter Notebooks** - Can run without Azure connection

## 💡 Final Pre-Class Checklist

Night before class:
- [ ] All services provisioned and tested
- [ ] Credentials file created and secured
- [ ] Demo data uploaded to all services
- [ ] Browser bookmarks organized
- [ ] Backup demos ready
- [ ] Cost alerts configured
- [ ] Resource group cleanup script ready for post-class

---

**Remember**: Keep your Azure OpenAI demos engaging - this is 25% of the exam now! Focus on practical prompt engineering and responsible AI use cases.

Good luck with your training tomorrow! 🎉