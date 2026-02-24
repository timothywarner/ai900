# AI-900 Live Punch List -- February 24, 2026

**Format:** O'Reilly Live | **Segments:** 5 x 50 min | **Region:** East US | **RG:** `AI900-Feb2026`

---

## Pre-Class Checklist

- [ ] Azure Portal open and signed in -- portal.azure.com
- [ ] Microsoft Foundry open and signed in -- ai.azure.com
- [ ] Foundry project created, multi-service resource connected (Management Center > Connected resources)
- [ ] Vision Studio open -- portal.vision.cognitive.azure.com
- [ ] Speech Studio open -- speech.microsoft.com
- [ ] Custom Vision open -- customvision.ai
- [ ] Azure ML Studio open -- ml.azure.com
- [ ] Verify `demos/.env` has all keys populated (run `uv run python main.py` in any hour dir to confirm)
- [ ] Terminal open in `C:\github\ai900\demos\`
- [ ] Exam practice assessment tab open -- https://learn.microsoft.com/credentials/certifications/exams/ai-900/practice/assessment?assessment-type=practice&assessmentId=26
- [ ] Exam sandbox tab open -- https://aka.ms/examdemo
- [ ] Repo link ready to share -- github.com/timothywarner/ai900

### Portal Bookmarks

| Portal | URL | Notes |
|--------|-----|-------|
| Azure Portal | portal.azure.com | Resource provisioning |
| Microsoft Foundry | ai.azure.com | Model catalog, playgrounds, language features, content filters |
| Azure ML Studio | ml.azure.com | AutoML, Designer, endpoints |
| Vision Studio | portal.vision.cognitive.azure.com | Image analysis, OCR, Face |
| Speech Studio | speech.microsoft.com | STT, TTS, voice gallery |
| Custom Vision | customvision.ai | Training + prediction projects |
| ~~Language Studio~~ | ~~language.cognitive.azure.com~~ | Deprecated -- use Foundry |

### Provisioned Resources

| # | Resource | SKU | Segment |
|---|----------|-----|---------|
| 1 | Azure AI Services (multi-service) | S0 | S1-S4 |
| 2 | Azure OpenAI Service | S0 | S5 (GPT-4o + DALL-E 3 deployed) |
| 3 | Azure ML workspace | -- | S2 |
| 4 | ML Compute Instance | Standard_DS11_v2 | S2 |
| 5 | Custom Vision -- Training | S0 | S3 |
| 6 | Custom Vision -- Prediction | S0 | S3 |
| 7 | Document Intelligence | S0 | S3 |

---

## S1 -- AI Fundamentals & Responsible AI (15-20%) | 09:00-10:00

### Theory (10 min)

- [ ] AI vs ML vs Deep Learning -- one slide, crisp one-liner each
- [ ] 4 exam workload types: computer vision, NLP, document processing, generative AI
- [ ] 6 Responsible AI principles -- mnemonic FAIR-PT: Fairness, Accountability, Inclusiveness, Reliability & Safety, Privacy & Security, Transparency

> EXAM TIP: Know all 6 RAI principles cold. Scenario questions like "Contoso wants AI that doesn't discriminate -- which principle?" Answer: Fairness.

### Portal Demos (15 min)

- [ ] Azure Portal: show the multi-service resource (kind: `AIServices`, S0) -- one key covers Vision, Language, Speech, Face
- [ ] Vision Studio: quick image analysis (captions, tags) to prove the multi-service key works
- [ ] Foundry portal: show Azure AI Content Safety text moderation

### Python Demo (15 min)

```
cd C:\github\ai900\demos\hour-1-ai-fundamentals
uv run python main.py
```

| Menu | Demo | What to show |
|------|------|-------------|
| 1 | Analyze an Image (Azure AI Vision) | Caption, tags, objects from satya.jpg |
| 2 | Content Safety Check | Paste hateful text, show severity scores (Hate/Sexual/Violence/Self-harm) |
| 3 | Responsible AI Principles Quiz | Run interactively with class -- scenario-based |
| 4 | AI Workload Identifier Quiz | Run interactively -- classify scenarios to workload types |

### Q&A / Break (10 min)

> EXAM TIP: Accountability means an organization must have governance processes -- people are ultimately responsible for AI decisions, not the AI itself.

---

## S2 -- Machine Learning (15-20%) | 10:00-11:00

### Theory (10 min)

- [ ] Supervised: regression (predict a number) vs classification (predict a category)
- [ ] Unsupervised: clustering (group similar items, no labels)
- [ ] Features vs labels | Training vs validation split
- [ ] Deep learning: CNNs for images, Transformers for sequences (attention mechanism -- on exam since May 2025)

> EXAM TIP: "When to use AutoML vs Designer vs Notebooks?" AutoML = fastest/no-code, Designer = visual drag-drop, Notebooks = full control. This is a frequent question.

### Portal Demos (15 min)

- [ ] Azure ML Studio (ml.azure.com): workspace tour -- compute, data, jobs, models, endpoints
- [ ] AutoML: show a completed run or start one with bank marketing CSV
- [ ] Designer: show a drag-drop pipeline (data > train > evaluate)

### Python Demo (20 min)

```
cd C:\github\ai900\demos\hour-2-machine-learning
uv run python main.py
```

| Menu | Demo | What to show |
|------|------|-------------|
| 1 | Explore Bank Marketing Dataset | Shape, columns, class imbalance (most said "no") -- binary classification |
| 2 | Classification (Decision Tree) | Accuracy, precision, recall, F1, confusion matrix -- explain each |
| 3 | Regression Concepts | Linear regression on synthetic data, R-squared, predicted vs actual |
| 4 | Clustering (KMeans) | Unsupervised -- 3 clusters, text scatter plot, no labels needed |
| 5 | ML Concepts Quiz | Interactive -- regression/classification/clustering/self-attention |

NOTE: Hour 2 runs locally with scikit-learn. No Azure credentials needed.

### Q&A / Break (5 min)

> EXAM TIP: Confusion matrix -- True Positive, False Positive, True Negative, False Negative. Precision = TP/(TP+FP). Recall = TP/(TP+FN). Know the difference.

---

## S3 -- Computer Vision (15-20%) | 11:00-12:00

### Theory (5 min)

- [ ] Image classification (label whole image) vs object detection (bounding boxes) vs OCR (text extraction)
- [ ] Face detection vs face analysis vs face verification (1:1) vs face identification (1:many)

> EXAM TIP: Verification = "Are these the same person?" (1:1). Identification = "Who is this person?" (1:many). This distinction appears frequently.

### Portal Demos (15 min)

- [ ] Vision Studio -- Image Analysis: describe image, tags, objects, smart crop
- [ ] Vision Studio -- OCR: printed + handwritten text
- [ ] Vision Studio -- Face: detect faces, head pose, blur, mask
- [ ] Custom Vision portal (customvision.ai): create project, show training images (Carrot*.JPG), train classifier, test, show export options (ONNX, Docker, CoreML)
- [ ] Document Intelligence (Azure Portal): analyze receipt or invoice with prebuilt model

### Python Demo (20 min)

```
cd C:\github\ai900\demos\hour-3-computer-vision
uv run python main.py
```

| Menu | Demo | What to show |
|------|------|-------------|
| 1 | Image Analysis | Caption, dense captions, tags, objects, smart crops -- pick satya.jpg or landmark |
| 2 | OCR (Read Text) | Extract text from clean and noisy images, show per-word confidence |
| 3 | Face Detection | Face rectangle, head pose, blur, mask, recognition quality |
| 4 | Document Intelligence | Receipt extraction -- merchant, line items, totals (uses contoso-receipt.png) |
| 5 | Custom Vision Concepts | Educational walkthrough + quiz (min 5 images/tag, compact vs standard, export) |

### Q&A / Break (10 min)

> EXAM TIP: Custom Vision needs a separate Training resource AND Prediction resource. Compact domains allow edge export (ONNX, Docker). Standard domains are cloud-only. Minimum 5 images per tag.

---

## S4 -- Natural Language Processing (15-20%) | 12:00-13:00

### Theory (5 min)

- [ ] Azure AI Language = text analytics + CLU + Custom Question Answering
- [ ] Azure AI Speech = speech-to-text + text-to-speech + translation
- [ ] Language Studio is deprecated -- all Language features are now in Microsoft Foundry (ai.azure.com)

> EXAM TIP: CLU replaced LUIS. Custom Question Answering replaced QnA Maker. The exam uses ONLY current names. Deprecated names appear as wrong answers (traps).

### Portal Demos (15 min)

- [ ] Foundry portal -- Sentiment Analysis: paste product reviews, show pos/neg/neutral scores
- [ ] Foundry portal -- Key Phrase Extraction: topics from a paragraph
- [ ] Foundry portal -- NER: highlight entities + PII detection
- [ ] Foundry portal -- CLU: show intent + entity concept (OrderPizza intent, size/topping entities)
- [ ] Foundry portal -- Custom Question Answering: import FAQ, test Q&A pairs
- [ ] Speech Studio (speech.microsoft.com): TTS with neural voices, STT from audio file

### Python Demo (20 min)

```
cd C:\github\ai900\demos\hour-4-nlp
uv run python main.py
```

| Menu | Demo | What to show |
|------|------|-------------|
| 1 | Sentiment Analysis | 5 sample reviews + optional user input, per-sentence breakdown |
| 2 | Key Phrase Extraction | Gettysburg Address or Kennedy Inaugural -- extract topics |
| 3 | NER & PII Detection | Named entities (org, person, date, money) + PII redaction (SSN, email, phone) |
| 4 | Language Detection | 5 languages auto-detected with confidence scores |
| 5 | Speech Recognition & Synthesis | STT from WAV files (weather, light on/off) + TTS to WAV |
| 6 | NLP Concepts Quiz | CLU vs Custom QA, intents vs entities, STT vs TTS |

### Q&A / Break (10 min)

> EXAM TIP: CLU = intents (what the user wants to DO) + entities (key details). Custom Question Answering = Q&A pairs from docs/URLs (FAQ bot). Know which to pick for each scenario.

---

## S5 -- Generative AI (20-25%) HIGHEST WEIGHT | 13:00-14:00

### Theory (5 min)

- [ ] Generative AI: produces NEW content (text, images, code) -- not just classify/predict
- [ ] Common scenarios: content creation, summarization, code gen, Q&A, image generation
- [ ] Responsible AI for GenAI: hallucinations, bias, content filtering, grounding with RAG
- [ ] Tokens = billing unit. ~4 chars = 1 token. Context window = token budget.

> EXAM TIP: This is 20-25% of the exam -- the single biggest domain. Know Microsoft Foundry, model catalog, prompt engineering, and content filtering. If you study one domain extra, make it this one.

### Portal Demos (10 min)

- [ ] Microsoft Foundry (ai.azure.com): portal tour -- projects, model catalog (1,600+ models), deployments
- [ ] Foundry Playground (Chat): GPT-4o -- system message, temperature slider
- [ ] Foundry Playground (Images): DALL-E 3 -- generate from text prompt
- [ ] Content Filters: show the 4 categories (hate, sexual, violence, self-harm) and severity levels

### Python Demo (20 min)

```
cd C:\github\ai900\demos\hour-5-generative-ai
uv run python main.py
```

| Menu | Demo | What to show |
|------|------|-------------|
| 1 | Chat with GPT-4o | Pick a persona (assistant/pirate/Socratic), show system message + conversation history + token usage |
| 2 | Prompt Engineering Workshop | Same question 4 ways: zero-shot > system message > few-shot > chain-of-thought. Show quality improving at each step. |
| 3 | Temperature Explorer | Same creative prompt at 0.0, 0.5, 1.0 -- deterministic vs creative |
| 4 | DALL-E 3 Image Generation | Generate image from text, show revised prompt, save URL |
| 5 | Content Filter Demo | Benign prompt passes, harmful prompt triggers 400 error -- content safety in action |
| 6 | RAG Pattern Explainer | Same question WITH and WITHOUT context. Fictional company KB. Shows grounding reduces hallucination. |
| 7 | Generative AI Quiz | 6 exam-style questions: Foundry, DALL-E, few-shot, tokens, content filters, RAG |

### Exam Prep Wrap-up (15 min)

- [ ] Register at Pearson VUE -- score 700+ to pass
- [ ] Free practice assessment: https://learn.microsoft.com/credentials/certifications/exams/ai-900/practice/assessment?assessment-type=practice&assessmentId=26
- [ ] Exam sandbox: https://aka.ms/examdemo
- [ ] Share repo: github.com/timothywarner/ai900

> EXAM TRAPS: Deprecated names still appear as WRONG answers -- Cognitive Services (now Azure AI Services), LUIS (now CLU), QnA Maker (now Custom Question Answering), AI Studio (now Microsoft Foundry), Language Studio (deprecated, use Foundry).

> EXAM TIP: Generative AI domain -- know these cold: Microsoft Foundry portal, model catalog, prompt engineering techniques (zero-shot, few-shot, chain-of-thought), temperature, content filtering (4 categories + severity levels), RAG pattern, tokens.

---

## Domain Weight Summary

| Domain | Weight | Segment |
|--------|--------|---------|
| AI workloads & Responsible AI | 15-20% | S1 |
| Machine Learning | 15-20% | S2 |
| Computer Vision | 15-20% | S3 |
| NLP | 15-20% | S4 |
| **Generative AI** | **20-25%** | **S5** |

Skills measured as of May 2, 2025 -- https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900
