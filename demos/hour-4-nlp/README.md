# 💬 Hour 4: Natural Language Processing

**Duration:** 1 hour  
**Exam Weight:** 15-20%  
**Philosophy:** Teaching Azure to understand human language - practical NLP magic!

## 🎓 Exam Focus Areas
- **Identify features of common NLP workload scenarios**
- **Identify Azure tools and services for NLP workloads**
- **Understand key phrase extraction, entity recognition, sentiment analysis**
- **Know language modeling, speech recognition, and translation**

## 📚 Key Concepts (5 min theory)

### NLP Service Ecosystem (UPDATED May 2025!)
| Old Name | New Name | Purpose |
|----------|----------|---------|
| Text Analytics | **Azure AI Language** | Text analysis & understanding |
| LUIS | **Conversational Language Understanding (CLU)** | Intent & entity extraction |
| QnA Maker | **Custom Question Answering** | FAQ-style Q&A |
| Form Recognizer | **Azure AI Document Intelligence** | Document data extraction |
| Speech Services | **Azure AI Speech** | Speech-to-text & text-to-speech |

### Core NLP Tasks
1. **Sentiment Analysis**: Positive/Negative/Neutral
2. **Key Phrase Extraction**: Main topics
3. **Entity Recognition**: People, places, organizations
4. **Language Detection**: Identify language
5. **Translation**: 100+ languages
6. **Speech Recognition**: Audio to text

## 🔥 Demo Scripts

### Demo 1: Azure AI Language Service (15 min)
```python
# language-service-demo.py
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Setup
key = "YOUR_LANGUAGE_KEY"
endpoint = "YOUR_LANGUAGE_ENDPOINT"
client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

# Demo texts
documents = [
    "I absolutely love the new Azure AI services! The documentation is fantastic.",
    "The hotel was terrible. Room was dirty and staff was rude.",
    "Microsoft announced Azure AI Foundry in Seattle on May 21, 2024."
]

print("🎭 DEMO 1: Sentiment Analysis")
sentiment_results = client.analyze_sentiment(documents)
for idx, result in enumerate(sentiment_results):
    print(f"Text {idx+1}: {result.sentiment} (Confidence: {result.confidence_scores[result.sentiment]:.2%})")
    print(f"  Scores - Pos: {result.confidence_scores.positive:.2%}, "
          f"Neg: {result.confidence_scores.negative:.2%}, "
          f"Neu: {result.confidence_scores.neutral:.2%}")

print("\n🔑 DEMO 2: Key Phrase Extraction")
key_phrases = client.extract_key_phrases(documents)
for idx, result in enumerate(key_phrases):
    print(f"Text {idx+1} key phrases: {', '.join(result.key_phrases)}")

print("\n🏢 DEMO 3: Entity Recognition")
entities = client.recognize_entities(documents)
for idx, result in enumerate(entities):
    print(f"Text {idx+1} entities:")
    for entity in result.entities:
        print(f"  - {entity.text} ({entity.category}, {entity.confidence_score:.2%})")

print("\n🔒 DEMO 4: PII Detection")
pii_text = ["My SSN is 123-45-6789 and email is john@contoso.com"]
pii_results = client.recognize_pii_entities(pii_text)
for result in pii_results:
    print("Detected PII:")
    for entity in result.entities:
        print(f"  - {entity.text} (Type: {entity.category})")
```

### Demo 2: Conversational Language Understanding (CLU) - Replacing LUIS (15 min)
```python
# clu-demo.py
"""
Live Demo: Pizza Ordering Bot with CLU

1. Navigate to language.cognitive.azure.com
2. Create new Conversational Language Understanding project:
   - Name: "PizzaOrderBot"
   - Language: English
   
3. Add intents:
   - OrderPizza: "I want to order a large pepperoni pizza"
   - CheckStatus: "What's the status of my order?"
   - CancelOrder: "I need to cancel my order"
   
4. Add entities:
   - Size: small, medium, large
   - Topping: pepperoni, mushroom, cheese
   - OrderNumber: pattern-based entity
   
5. Train and test the model
"""

from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

# CLU client setup
clu_key = "YOUR_CLU_KEY"
clu_endpoint = "YOUR_CLU_ENDPOINT"
project_name = "PizzaOrderBot"
deployment_name = "production"

client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))

# Test utterances
test_queries = [
    "I'd like a medium mushroom pizza please",
    "Where's my order #12345?",
    "Cancel order 54321"
]

for query in test_queries:
    result = client.analyze_conversation(
        task={
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "text": query,
                    "id": "1",
                    "participantId": "user"
                }
            },
            "parameters": {
                "projectName": project_name,
                "deploymentName": deployment_name
            }
        }
    )
    
    prediction = result["result"]["prediction"]
    print(f"\nQuery: '{query}'")
    print(f"Intent: {prediction['topIntent']} ({prediction['intents'][0]['confidence']:.2%})")
    if prediction.get("entities"):
        print("Entities:")
        for entity in prediction["entities"]:
            print(f"  - {entity['category']}: {entity['text']}")
```

### Demo 3: Custom Question Answering (Replacing QnA Maker) (10 min)
```python
# custom-qa-demo.py
"""
Live Demo: FAQ Bot with Custom Question Answering

1. In language.cognitive.azure.com:
2. Create Custom Question Answering project
3. Add knowledge sources:
   - Import from URL: https://docs.microsoft.com/faq
   - Add manual Q&A pairs
   
4. Edit and enrich:
   - Add alternative questions
   - Set up follow-up prompts
   - Configure chitchat personality
"""

from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.core.credentials import AzureKeyCredential

# Setup
qa_key = "YOUR_QA_KEY"
qa_endpoint = "YOUR_QA_ENDPOINT"
project_name = "CompanyFAQ"
deployment_name = "production"

client = QuestionAnsweringClient(qa_endpoint, AzureKeyCredential(qa_key))

# Test questions
questions = [
    "What are your business hours?",
    "How do I reset my password?",
    "Do you offer refunds?"
]

for question in questions:
    response = client.get_answers(
        question=question,
        project_name=project_name,
        deployment_name=deployment_name
    )
    
    print(f"\nQ: {question}")
    if response.answers:
        print(f"A: {response.answers[0].answer}")
        print(f"Confidence: {response.answers[0].confidence:.2%}")
```

## 💡 Exam Tips & Tricks

### ⚡ Service Selection Matrix
| Scenario | Service | Key Feature |
|----------|---------|-------------|
| Analyze customer reviews | Azure AI Language | Sentiment & opinions |
| Build a chatbot | CLU + Bot Service | Intent recognition |
| Create FAQ bot | Custom Question Answering | Q&A pairs |
| Translate documents | Translator | 100+ languages |
| Transcribe meetings | Azure AI Speech | Real-time transcription |
| Extract form data | Document Intelligence | Structured extraction |

### 🎯 Key Differentiators
1. **CLU vs Custom Question Answering**
   - CLU: Complex intents & entities
   - Custom QA: Simple Q&A matching

2. **Language Detection vs Translation**
   - Detection: Identify the language
   - Translation: Convert between languages

3. **Entity Recognition Types**
   - Named entities: People, places, organizations
   - PII entities: SSN, credit cards, emails
   - Key phrases: Main topics/concepts

### 📝 Practice Questions

**Q1:** You need to build a bot that understands "Book a flight to Seattle tomorrow". Which service?
- A) Custom Question Answering
- B) Conversational Language Understanding (CLU) ✅
- C) Translator
- D) Azure AI Speech

**Q2:** A company wants to analyze customer support emails for satisfaction. Which feature?
- A) Key phrase extraction
- B) Entity recognition
- C) Sentiment analysis ✅
- D) Language detection

**Q3:** You need to extract data from invoices. Which service? 
- A) Azure AI Language
- B) Azure AI Document Intelligence ✅
- C) CLU
- D) Custom Question Answering

**Q4:** What's the maximum number of languages supported by Translator?
- A) 50
- B) 75
- C) 100+ ✅
- D) 200

## 🚀 Hands-on Challenge
**Language Detective Challenge:**
1. Analyze a movie review for sentiment
2. Extract key phrases
3. Identify any people/places mentioned
4. Winner: Most interesting insight found!

## 📌 Remember
- Show real-world applications (customer service, content moderation)
- Emphasize the rebranding (LUIS→CLU, QnA Maker→Custom QA)
- AI-900 loves "which service for what" questions
- Always mention language support capabilities

## 🔗 Resources
- [Azure AI Language Documentation](https://docs.microsoft.com/azure/cognitive-services/language-service/)
- [CLU Migration Guide](https://docs.microsoft.com/azure/cognitive-services/luis/migrate-to-clu)
- [Custom Question Answering](https://docs.microsoft.com/azure/cognitive-services/language-service/question-answering/)
- [Azure AI Speech](https://docs.microsoft.com/azure/cognitive-services/speech-service/) 