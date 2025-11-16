# 🚀 Microsoft Azure AI Fundamentals (AI-900) - 5-Hour Live Training Plan

## 🎯 INSTRUCTOR QUICK REFERENCE
```
📁 DEMO LOCATIONS:
- Hour 1: demos/hour-1-ai-fundamentals/
- Hour 2: demos/hour-2-machine-learning/  
- Hour 3: demos/hour-3-computer-vision/
- Hour 4: demos/hour-4-nlp/
- Hour 5: demos/hour-5-generative-ai/

🔗 QUICK LINKS:
- Azure Portal: portal.azure.com
- AI Foundry: ai.azure.com (NEW!)
- ML Studio: ml.azure.com
- Custom Vision: customvision.ai
- Language Studio: language.cognitive.azure.com

⚠️ KEY UPDATES (May 2025):
- Cognitive Services → Azure AI Services
- LUIS → CLU (Conversational Language Understanding)
- QnA Maker → Custom Question Answering
- Generative AI now 20-25% (highest weight!)
```

## 📌 5-HOUR SEGMENT FOCUS PUNCHLIST

### ⏰ HOUR 1: AI Fundamentals & Responsible AI (15-20%)
**MUST COVER:**
- [ ] AI vs ML vs Deep Learning definitions
- [ ] 6 AI workload types (vision, NLP, document, speech, generative, decision)
- [ ] 6 Responsible AI principles (FAIR-PT)
- [ ] Azure AI Services overview & multi-service account
- [ ] **DEMOS:** Face detection with fairness analysis, Content moderation

### ⏰ HOUR 2: Machine Learning Fundamentals (15-20%)
**MUST COVER:**
- [ ] Supervised (regression/classification) vs Unsupervised (clustering) vs Reinforcement
- [ ] Deep learning techniques (CNNs for images, RNNs for sequences)
- [ ] **Transformer architecture** (attention mechanism, foundation of GPT/BERT) **NEW!**
- [ ] Features and labels in datasets
- [ ] Training vs Validation vs Test datasets (data splitting strategy)
- [ ] Overfitting/Underfitting concepts
- [ ] Azure ML capabilities: AutoML, Designer, Notebooks
- [ ] Model management and deployment in Azure ML
- [ ] **DEMOS:** AutoML classification (Titanic), Designer pipeline, Model deployment as endpoint

### ⏰ HOUR 3: Computer Vision Workloads (15-20%)
**MUST COVER:**
- [ ] Image classification solutions (categorization)
- [ ] Object detection solutions (bounding boxes, instance detection)
- [ ] Optical character recognition (OCR) - printed & handwritten text
- [ ] Facial detection and facial analysis (age, emotion, attributes)
- [ ] Face verification vs Face identification
- [ ] Azure AI Vision service capabilities
- [ ] Azure AI Face detection service capabilities
- [ ] Custom Vision for training domain-specific models
- [ ] **DEMOS:** Computer Vision API analysis, Custom Vision training (cats vs dogs), Face detection with attributes

### ⏰ HOUR 4: Natural Language Processing (15-20%)
**MUST COVER:**
- [ ] Key phrase extraction (topic identification)
- [ ] Entity recognition (named entities, PII detection)
- [ ] Sentiment analysis (positive/negative/neutral/mixed)
- [ ] Language modeling and understanding
- [ ] Speech recognition and synthesis (speech-to-text, text-to-speech)
- [ ] Translation (90+ languages)
- [ ] Azure AI Language service capabilities
- [ ] Azure AI Speech service capabilities
- [ ] Conversational Language Understanding (CLU) - intents & entities
- [ ] Custom Question Answering (formerly QnA Maker)
- [ ] **DEMOS:** Sentiment analysis, CLU pizza bot, Custom QA knowledge base, Speech synthesis

### ⏰ HOUR 5: Generative AI & Azure OpenAI (20-25% - HIGHEST!)
**MUST COVER:**
- [ ] Features of generative AI models (text, image, code generation)
- [ ] Common scenarios for generative AI (content creation, summarization, Q&A)
- [ ] Responsible AI considerations for generative AI (hallucinations, bias, content filtering)
- [ ] **Azure AI Foundry features and capabilities** (unified platform) **NEW!**
- [ ] **Azure AI Foundry model catalog** (1,600+ models from Microsoft, OpenAI, Meta, Hugging Face) **NEW!**
- [ ] Azure OpenAI Service features (GPT-4, GPT-3.5-Turbo, DALL-E 3, Embeddings, Whisper)
- [ ] Prompt engineering techniques (zero-shot, few-shot, system messages, temperature)
- [ ] Tokens and context windows
- [ ] Content filtering and safety features
- [ ] Grounding and RAG (Retrieval-Augmented Generation)
- [ ] **DEMOS:** AI Foundry portal tour, Model catalog, GPT-4 playground, DALL-E 3 image generation, Content filters, RAG pattern

## Course Philosophy: 80% Demos, 20% Theory, 100% Engagement! 

**Target Duration:** 5 Hours (with breaks)  
**Format:** O'Reilly Live Learning  
**Goal:** Delight learners with practical Azure AI demonstrations while preparing them for AI-900 certification

---

## 📋 Pre-Course Setup (Learners complete before class)
- Azure free account creation
- Install VS Code, Node.js, Python
- Clone this repository
- Quick environment verification checklist

---

## 🎯 Hour 1: AI Fundamentals & Azure AI Platform (15-20% of exam)

### Opening (10 min)
- **Hook:** "Let's build something amazing in the next 5 hours!"
- Quick intros & expectations
- Repository tour & setup verification
- **🎓 Exam Tip:** AI-900 is project-based - expect scenario questions!

### Core Content (40 min)
**Theory Blast (10 min):**
- What is AI vs ML vs Deep Learning? (with visual diagram)
- Azure AI service categories: Vision, Language, Speech, Decision, OpenAI

**🔥 DEMO FEST (30 min):**
1. **Azure Portal Tour** - Creating your first Cognitive Service
2. **Multi-Service Demo** - One image, multiple AI services:
   - Computer Vision: "What's in this image?"
   - Face API: "Who's in this image?"
   - Custom Vision: "Is this a hot dog?"
3. **Responsible AI Dashboard** - Fairness analysis on a real model

### Wrap-up (10 min)
- Q&A
- **🎓 Exam Alert:** Know the 6 principles of Responsible AI!
- Quick break

---

## 🤖 Hour 2: Machine Learning on Azure (15-20% of exam)

### Opening (5 min)
- **Hook:** "From zero to deployed ML model in 45 minutes!"
- **🎓 Exam Tip:** Understand classification vs regression vs clustering

### Core Content (45 min)
**Theory Sprint (10 min):**
- ML lifecycle: Data → Train → Deploy → Monitor
- Automated ML vs Designer vs Notebooks

**🔥 MEGA DEMO (35 min):**
1. **Azure ML Workspace Setup** (5 min)
2. **Automated ML Project** (20 min):
   - Upload Titanic dataset
   - Configure AutoML experiment
   - Watch it train (explain what's happening)
   - Deploy best model as endpoint
   - Test with Postman/curl
3. **Designer Quick Tour** (10 min):
   - Drag-drop pipeline creation
   - No-code model training

### Wrap-up (10 min)
- **🎓 Exam Focus:** Know when to use each ML approach
- Break time!

---

## 👁️ Hour 3: Computer Vision Workloads (15-20% of exam)

### Opening (5 min)
- **Hook:** "Teaching computers to see - and understand!"
- **🎓 Exam Tip:** Differentiate between pre-built and custom vision services

### Core Content (45 min)
**Theory Bite (5 min):**
- Computer Vision vs Custom Vision vs Face vs Form Recognizer

**🔥 VISION DEMOS (40 min):**
1. **Computer Vision Deep Dive** (15 min):
   - Analyze local & URL images
   - Object detection with bounding boxes
   - OCR on handwritten notes
   - Spatial analysis demo
2. **Custom Vision Project** (15 min):
   - Upload training images (cats vs dogs)
   - Train classifier
   - Test & iterate
   - Export model (Edge, Docker, TensorFlow)
3. **Face API Magic** (10 min):
   - Face detection & attributes
   - Emotion recognition
   - Face verification (are these the same person?)

### Wrap-up (10 min)
- **🎓 Exam Alert:** Know the difference between Face Identification vs Verification
- Quick stretch!

---

## 💬 Hour 4: Natural Language Processing (15-20% of exam)

### Opening (5 min)
- **Hook:** "Let's teach Azure to understand human language!"
- **🎓 Exam Tip:** Language Understanding (LUIS) vs Text Analytics - know when to use each

### Core Content (45 min)
**Theory Nugget (5 min):**
- NLP service ecosystem in Azure
- Pre-built vs custom language models

**🔥 LANGUAGE DEMOS (40 min):**
1. **Text Analytics Playground** (15 min):
   - Sentiment analysis on reviews
   - Key phrase extraction
   - Entity recognition (PII detection)
   - Language detection challenge
2. **LUIS in Action** (15 min):
   - Build pizza ordering bot intents
   - Train with utterances
   - Test interactively
   - Improve with active learning
3. **QnA Maker Speed Run** (10 min):
   - Import FAQ from URL
   - Train knowledge base
   - Test Q&A pairs
   - Publish endpoint

### Wrap-up (10 min)
- **🎓 Exam Pro Tip:** LUIS = intents + entities, QnA Maker = question-answer pairs
- Final break!

---

## 🎨 Hour 5: Generative AI & Course Wrap-up (20-25% of exam - HIGHEST!)

### Opening (5 min)
- **Hook:** "Welcome to the future - let's create with AI!"
- **🎓 Exam Tip:** Understand prompt engineering and responsible AI for GenAI

### Core Content (35 min)
**Theory Flash (5 min):**
- Generative AI vs traditional AI
- Azure OpenAI Service overview
- Prompt engineering basics

**🔥 GENERATIVE AI SHOWCASE (30 min):**
1. **Azure OpenAI Playground** (20 min):
   - GPT model demos (completion, chat, embeddings)
   - Prompt engineering techniques:
     - Zero-shot vs few-shot
     - System messages
     - Temperature & parameters
   - DALL-E image generation
   - Code generation examples
2. **Responsible AI for GenAI** (10 min):
   - Content filters demo
   - Monitoring & guardrails
   - Best practices

### Course Finale (20 min)
- **🎓 Exam Preparation Lightning Round:**
  - Registration process & tips
  - Question types walkthrough
  - Time management strategies
  - Resources for continued learning
- **Live Q&A:** Any burning questions!
- **Call to Action:** 
  - Schedule your exam
  - Join our study group
  - Share your success stories

---

## 📚 Post-Course Resources
- Link to this GitHub repository
- AI-900 exam objectives document
- Practice test recommendations
- Community Discord/Slack invite
- Instructor contact for follow-up

## 🎪 Remember: Keep it PRACTICAL, keep it FUN, keep it FOCUSED on certification success!

**Instructor Notes:**
- Have backup demos ready
- Keep Azure costs in mind - use free tiers
- Encourage questions throughout
- Share exam tricks as "insider tips" during relevant demos
- Success stories make great transitions between sections