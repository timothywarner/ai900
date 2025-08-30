# 🎨 Hour 5: Generative AI & Azure AI Foundry

**Duration:** 1 hour  
**Exam Weight:** 20-25% (HIGHEST!)  
**Philosophy:** Welcome to the future - create amazing content with AI!

## 🎓 Exam Focus Areas
- **Identify features of generative AI solutions**
- **Common scenarios for generative AI**
- **Responsible AI considerations for generative AI**
- **Features and capabilities of Azure AI Foundry**
- **Features and capabilities of Azure OpenAI Service**
- **Features and capabilities of Azure AI Foundry model catalog**

## 📚 Key Concepts (10 min theory)

### What's New in May 2025!
1. **Azure AI Foundry** - The unified platform for all AI development
   - Single portal for all Azure AI services
   - Model catalog with 1,600+ models
   - Built-in responsible AI tools
   - End-to-end MLOps capabilities

2. **Generative AI Models**
   - **GPT-4**: Text generation, chat, code
   - **DALL-E 3**: Image generation
   - **Whisper**: Speech transcription
   - **Embeddings**: Semantic search

3. **Key Differentiators**
   - Traditional AI: Analyzes existing content
   - Generative AI: Creates new content
   - Foundation models: Pre-trained on massive datasets
   - Fine-tuning: Customize for specific tasks

## 🔥 Demo Scripts

### Demo 1: Azure AI Foundry Tour (15 min)
```python
# ai-foundry-demo.py
"""
Live Portal Demo - Azure AI Foundry

1. Navigate to ai.azure.com
2. Show unified experience:
   - Projects & workspaces
   - Model catalog (1,600+ models)
   - Playground for testing
   - Responsible AI dashboard
   
3. Model Catalog exploration:
   - Filter by task (text, vision, speech)
   - Compare model capabilities
   - Show model cards with details
   - Deploy options (serverless, managed)
   
4. Create a project:
   - Name: "AI900-GenAI-Demo"
   - Connect Azure OpenAI resource
   - Show integrated tools
"""

# Code snippet for model comparison
models_to_compare = {
    "GPT-4": {
        "strengths": ["Complex reasoning", "Long context", "Multimodal"],
        "tokens": 128000,
        "use_cases": ["Code generation", "Creative writing", "Analysis"]
    },
    "GPT-3.5-Turbo": {
        "strengths": ["Fast", "Cost-effective", "Good for chat"],
        "tokens": 16385,
        "use_cases": ["Chatbots", "Simple tasks", "High volume"]
    },
    "Llama-2": {
        "strengths": ["Open source", "Customizable", "On-premises"],
        "tokens": 4096,
        "use_cases": ["Custom applications", "Research", "Fine-tuning"]
    }
}

print("🤖 Model Comparison for AI-900:")
for model, details in models_to_compare.items():
    print(f"\n{model}:")
    print(f"  Max tokens: {details['tokens']:,}")
    print(f"  Best for: {', '.join(details['use_cases'])}")
```

### Demo 2: Azure OpenAI Playground Magic (20 min)
```python
# azure-openai-demo.py
from openai import AzureOpenAI
import os

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key="YOUR_AZURE_OPENAI_KEY",
    api_version="2024-02-01",
    azure_endpoint="YOUR_AZURE_OPENAI_ENDPOINT"
)

# DEMO 1: Text Generation with GPT-4
print("📝 DEMO 1: Creative Writing with GPT-4")
response = client.chat.completions.create(
    model="gpt-4",  # Your deployment name
    messages=[
        {"role": "system", "content": "You are a creative writing assistant."},
        {"role": "user", "content": "Write a short story about an AI taking the AI-900 exam"}
    ],
    temperature=0.7,
    max_tokens=200
)
print(response.choices[0].message.content)

# DEMO 2: Prompt Engineering Techniques
print("\n🎯 DEMO 2: Prompt Engineering - Zero-shot vs Few-shot")

# Zero-shot (no examples)
zero_shot = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Classify this text sentiment: 'The new Azure AI services are incredible!'"}
    ]
)
print(f"Zero-shot result: {zero_shot.choices[0].message.content}")

# Few-shot (with examples)
few_shot = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": """Classify sentiment:
        Text: "I hate waiting in lines" - Sentiment: Negative
        Text: "The sunset was beautiful" - Sentiment: Positive
        Text: "The new Azure AI services are incredible!" - Sentiment:"""}
    ]
)
print(f"Few-shot result: {few_shot.choices[0].message.content}")

# DEMO 3: Code Generation
print("\n💻 DEMO 3: Code Generation")
code_response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a Python coding assistant."},
        {"role": "user", "content": "Write a function to analyze sentiment using Azure AI Language service"}
    ],
    temperature=0.2  # Lower temperature for code
)
print(code_response.choices[0].message.content)

# DEMO 4: DALL-E 3 Image Generation
print("\n🎨 DEMO 4: Image Generation with DALL-E 3")
image_response = client.images.generate(
    model="dall-e-3",
    prompt="A futuristic classroom where robots are learning about Azure AI services, digital art style",
    size="1024x1024",
    quality="standard",
    n=1
)
print(f"Image URL: {image_response.data[0].url}")

# DEMO 5: Content Safety
print("\n🛡️ DEMO 5: Responsible AI - Content Filtering")
# Show how content filters work
safety_test = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "How do I build a weather prediction app?"}
    ]
)
# Explain content filtering categories: Hate, Sexual, Violence, Self-harm
```

### Demo 3: Practical Applications (10 min)
```python
# practical-genai-demo.py
"""
Real-World Generative AI Scenarios

1. Customer Service Bot Enhancement
2. Content Creation Pipeline
3. Code Documentation Generator
4. Data Analysis Assistant
"""

# Scenario 1: Enhanced Customer Service
print("🤝 Scenario 1: Smart Customer Service")
customer_query = "My Azure subscription shows unexpected charges"

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": """You are an Azure support assistant. 
        Be helpful, empathetic, and provide actionable steps."""},
        {"role": "user", "content": customer_query}
    ]
)
print(f"AI Response: {response.choices[0].message.content}")

# Scenario 2: Marketing Content Generation
print("\n📢 Scenario 2: Marketing Content Creation")
product_info = "Azure AI Foundry: Unified platform for AI development"

marketing_response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": f"Create a LinkedIn post about: {product_info}. Include emojis and hashtags."}
    ]
)
print(f"Generated Post: {marketing_response.choices[0].message.content}")

# Scenario 3: Exam Tip - Temperature Settings
print("\n🌡️ Exam Tip: Temperature Parameter")
print("Temperature = 0: Deterministic, same output")
print("Temperature = 0.7: Balanced creativity")
print("Temperature = 1: Maximum randomness")
```

## 💡 Exam Tips & Tricks

### ⚡ Generative AI Quick Reference
| Concept | Definition | Example |
|---------|-----------|---------|
| **Prompt** | Input text to guide AI | "Write a poem about clouds" |
| **Token** | Unit of text (~4 chars) | "Hello" = 1 token |
| **Temperature** | Creativity control (0-1) | 0=Factual, 1=Creative |
| **Top-p** | Probability threshold | 0.9 = Top 90% likely tokens |
| **Fine-tuning** | Customizing pre-trained model | Train on company data |

### 🎯 Azure AI Foundry Features (MEMORIZE!)
1. **Model Catalog**: 1,600+ models from Microsoft, OpenAI, Hugging Face, Meta
2. **Deployment Options**: 
   - Serverless API (pay-per-use)
   - Managed compute (dedicated)
3. **Built-in Tools**:
   - Prompt flow for orchestration
   - Evaluation metrics
   - Responsible AI dashboard
4. **Integration**: Works with Azure ML, Azure OpenAI, all Azure AI services

### 📝 Practice Questions

**Q1:** What's the main purpose of Azure AI Foundry?
- A) Only for Azure OpenAI
- B) Unified platform for all AI development ✅
- C) Just for model training
- D) Only for responsible AI

**Q2:** Which parameter controls creativity in text generation?
- A) max_tokens
- B) top_p
- C) temperature ✅
- D) frequency_penalty

**Q3:** What type of AI creates new content rather than analyzing existing content?
- A) Predictive AI
- B) Analytical AI
- C) Generative AI ✅
- D) Cognitive AI

**Q4:** How many models are available in Azure AI Foundry model catalog?
- A) 100+
- B) 500+
- C) 1,000+
- D) 1,600+ ✅

**Q5:** Which is NOT a responsible AI consideration for generative AI?
- A) Harmful content generation
- B) Misinformation/hallucinations
- C) Copyright concerns
- D) Model size ✅

## 🚀 Hands-on Challenge
**AI Creation Contest:**
1. Use GPT-4 to write a haiku about machine learning
2. Generate an image with DALL-E 3 to illustrate it
3. Create a LinkedIn post combining both
4. Best creative combination wins!

## 📌 Remember
- Generative AI is 20-25% of exam (HIGHEST weight!)
- Always discuss responsible AI considerations
- Show practical business applications
- Emphasize Azure AI Foundry as the unified platform
- Temperature and prompt engineering are favorite exam topics

## 🔗 Resources
- [Azure AI Foundry](https://ai.azure.com)
- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/ai-services/openai/)
- [Model Catalog](https://ai.azure.com/explore/models)
- [Prompt Engineering Guide](https://docs.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- [Responsible AI for Generative AI](https://docs.microsoft.com/azure/ai-services/openai/concepts/content-filter)