# AI-900 Live Training - February 2026

**Format:** O'Reilly Live Learning | **Segments:** 5 x 50 min | **Philosophy:** 80% demos, 20% theory

---

## Quick-Access Bookmarks

| Portal | URL | Status |
| -------- | ----- | -------- |
| Azure Portal | portal.azure.com | |
| Azure AI Foundry | ai.azure.com | Primary -- Language features live here now |
| Azure ML Studio | ml.azure.com | |
| Vision Studio | portal.vision.cognitive.azure.com | Still active |
| Speech Studio | speech.microsoft.com | Still active, migrating to Foundry |
| Custom Vision | customvision.ai | Still active |
| ~~Language Studio~~ | ~~language.cognitive.azure.com~~ | Deprecated -- use Foundry instead |

---

## Segment 1 -- AI Fundamentals & Responsible AI (15-20%)

**50 min total = 10 min theory + 30 min demos + 10 min Q&A/break**

### Theory (10 min)

- [ ] AI vs ML vs Deep Learning -- one slide, crisp definitions
- [ ] 4 AI workload types on the exam: **computer vision, NLP, document processing, generative AI**
- [ ] 6 Responsible AI principles -- mnemonic **FAIR-PT**: Fairness, Accountability, Inclusiveness, Reliability & Safety, Privacy & Security, Transparency

### Demos (30 min)

- [ ] **Azure Portal** -- create a Foundry multi-service resource (kind: `AIServices`, S0) -- one key for Vision, Language, Speech, Face
- [ ] **Vision Studio** -- analyze an image (show how one key covers vision + language + speech)
- [ ] **Azure AI Content Safety** -- run text + image moderation
- [ ] **Responsible AI Dashboard** in Azure ML -- fairness metrics on a sample model

### Azure Products to Show

`Azure AI Services (multi-service)` | `Vision Studio` | `Azure AI Content Safety` | `Azure ML Responsible AI Dashboard`

### Exam Callout

> Know all 6 Responsible AI principles cold. Expect scenario questions like "Contoso wants to ensure their AI doesn't discriminate -- which principle?"

---

## Segment 2 -- Machine Learning on Azure (15-20%)

**50 min total = 10 min theory + 35 min demos + 5 min Q&A/break**

### Theory (10 min)

- [ ] Supervised learning: **regression** (predict a number) vs **classification** (predict a category)
- [ ] Unsupervised learning: **clustering** (group similar items)
- [ ] Deep learning: CNNs for images, RNNs for sequences
- [ ] **Transformer architecture** -- attention mechanism, foundation of GPT/BERT (NEW on exam)
- [ ] Features vs labels | Training vs validation datasets

### Demos (35 min)

- [ ] **Azure ML Studio** -- workspace tour (compute, data, jobs, models, endpoints)
- [ ] **Automated ML** -- upload Titanic CSV, run classification, review best model metrics
- [ ] **Designer** -- drag-drop pipeline: data source -> train -> evaluate -> deploy
- [ ] **Model deployment** -- deploy best model as managed online endpoint, test with curl/Postman

### Azure Products to Show

`Azure Machine Learning workspace` | `AutoML` | `Designer` | `Managed Online Endpoints` | `Compute Instances`

### Exam Callout

> "When should you use AutoML vs Designer vs Notebooks?" -- know the tradeoffs. AutoML = fastest, Designer = visual/no-code, Notebooks = full control.

---

## Segment 3 -- Computer Vision (15-20%)

**50 min total = 5 min theory + 40 min demos + 5 min Q&A/break**

### Theory (5 min)

- [ ] Image classification (single label) vs object detection (bounding boxes) vs OCR (text extraction)
- [ ] Facial detection vs facial analysis vs face verification vs face identification

### Demos (40 min)

- [ ] **Vision Studio -- Image Analysis** -- describe image, tags, objects, smart crop
- [ ] **Vision Studio -- OCR** -- printed text + handwritten text extraction
- [ ] **Custom Vision** -- create project, upload training images (cats vs dogs), train classifier, test with new image, show export options (Edge, Docker, ONNX)
- [ ] **Vision Studio -- Face** -- detect faces, return attributes (age, glasses, head pose)
- [ ] **Azure AI Document Intelligence** -- analyze an invoice with prebuilt model (key-value pairs, tables)

### Azure Products to Show

`Azure AI Vision` | `Custom Vision (Training + Prediction)` | `Azure AI Face` | `Azure AI Document Intelligence` | `Vision Studio`

### Exam Callout

> Face **verification** = "Are these two faces the same person?" (1:1). Face **identification** = "Who is this person?" (1:many). This distinction shows up frequently.

---

## Segment 4 -- Natural Language Processing (15-20%)

**50 min total = 5 min theory + 40 min demos + 5 min Q&A/break**

### Theory (5 min)

- [ ] NLP capabilities on the exam: key phrase extraction, entity recognition, sentiment analysis, language modeling, speech recognition/synthesis, translation
- [ ] **Azure AI Language** = text analytics + CLU + custom Q&A
- [ ] **Azure AI Speech** = speech-to-text + text-to-speech + translation

### Demos (40 min)

> **Portal note:** Language Studio (language.cognitive.azure.com) was deprecated Dec 2025. Demo all Language features in **Azure AI Foundry** (ai.azure.com) instead. Connect your Foundry multi-service resource to a Foundry project first (Management Center > Connected resources > + New connection).

- [ ] **Foundry portal -- Sentiment Analysis** -- paste product reviews, show positive/negative/neutral/mixed scores
- [ ] **Foundry portal -- Key Phrase Extraction** -- extract topics from a paragraph
- [ ] **Foundry portal -- Named Entity Recognition** -- highlight entities + PII detection
- [ ] **Foundry portal -- CLU (Conversational Language Understanding)** -- build pizza ordering bot: define intents (OrderPizza, CheckStatus), add entities (size, topping), train, test
- [ ] **Foundry portal -- Custom Question Answering** -- import FAQ URL, create knowledge base, test Q&A pairs
- [ ] **Speech Studio** -- text-to-speech with neural voices, speech-to-text live mic demo (speech.microsoft.com still works)

### Azure Products to Show

`Azure AI Language (via Foundry portal)` | `Azure AI Speech` | `Azure AI Foundry` | `Speech Studio` | `CLU` | `Custom Question Answering`

### Exam Callout

> CLU replaced LUIS. Custom Question Answering replaced QnA Maker. Language Studio replaced by Foundry portal. The exam uses current names exclusively. CLU = intents + entities. Custom QA = question-answer pairs from docs/URLs.

---

## Segment 5 -- Generative AI & Azure OpenAI (20-25%) **HIGHEST WEIGHT**

**50 min total = 5 min theory + 35 min demos + 10 min exam prep/wrap-up**

### Theory (5 min)

- [ ] Generative AI models: produce text, images, code (not just classify/predict)
- [ ] Common scenarios: content creation, summarization, code generation, Q&A, image generation
- [ ] Responsible AI for GenAI: hallucinations, bias, content filtering, grounding with RAG
- [ ] Tokens and context windows -- explain like a budget

### Demos (35 min)

- [ ] **Azure AI Foundry** -- portal tour: projects, model catalog, deployments, playgrounds
- [ ] **Azure AI Foundry Model Catalog** -- browse 1,600+ models (OpenAI, Meta Llama, Mistral, Hugging Face)
- [ ] **Azure OpenAI Playground (Chat)** -- GPT-4o: system message, zero-shot vs few-shot prompting, temperature slider
- [ ] **Azure OpenAI Playground (Images)** -- DALL-E 3: generate images from text prompts
- [ ] **Prompt Engineering** -- live demo: vague prompt -> refined prompt -> system message -> few-shot examples (show quality improvement at each step)
- [ ] **Content Filters** -- show Azure OpenAI built-in content filtering categories (hate, sexual, violence, self-harm) and severity levels
- [ ] **RAG pattern** -- explain grounding: "your data" + AI model = accurate, sourced answers

### Azure Products to Show

`Azure AI Foundry` | `Azure AI Foundry Model Catalog` | `Azure OpenAI Service` | `GPT-4o` | `DALL-E 3` | `Content Filters` | `RAG / On Your Data`

### Exam Prep Wrap-up (10 min)

- [ ] Register at Pearson VUE -- score 700+ to pass
- [ ] Free practice assessment: [Microsoft Learn Practice Assessment](https://learn.microsoft.com/credentials/certifications/exams/ai-900/practice/assessment?assessment-type=practice&assessmentId=26)
- [ ] Exam sandbox: [aka.ms/examdemo](https://aka.ms/examdemo)
- [ ] Biggest traps: deprecated names (LUIS, QnA Maker, Cognitive Services) still appear as wrong answers
- [ ] This repo: `github.com/timothywarner/ai900`

### Exam Callout

> Generative AI is 20-25% of the exam -- the single biggest domain. Know Azure AI Foundry (the portal), the model catalog, prompt engineering techniques, and content filtering. If you only study one domain extra hard, make it this one.

---

## Pre-Class Provisioning Checklist

| # | Resource | Kind / SKU | Used In | Notes |
| --- | ---------- | ----------- | --------- | ------- |
| 1 | Foundry multi-service | `AIServices` / S0 | Seg 1-4 | One key for Vision Studio, Foundry Language, Speech Studio, Face |
| 2 | Azure OpenAI Service | S0 | Seg 5 | Deploy GPT-4o + DALL-E 3 |
| 3 | Azure ML workspace | -- | Seg 2 | Auto-creates Storage, Key Vault, App Insights |
| 4 | ML Compute Instance | Standard_DS11_v2 | Seg 2 | For AutoML + Designer |
| 5 | Custom Vision - Training | S0 | Seg 3 | Separate from multi-service |
| 6 | Custom Vision - Prediction | S0 | Seg 3 | Separate from multi-service |
| 7 | Document Intelligence | S0 | Seg 3 | Invoice analysis demo |

### Foundry Portal Setup (do before class)

1. Go to ai.azure.com, create a Foundry project
2. Management Center > Connected resources > connect your Foundry multi-service resource (#1 above)
3. Verify Language features (sentiment, CLU, Custom QA) are accessible in the project

> Put everything in one resource group (`AI900-Feb2026`) in `East US`. Tear down after class.
