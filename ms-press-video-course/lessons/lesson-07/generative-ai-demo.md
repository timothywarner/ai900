# Generative AI Demo Guide

This guide provides an overview of generative AI using Azure OpenAI Service, with practical examples and responsible AI considerations.

## Introduction to Generative AI

Generative AI refers to artificial intelligence systems that can generate new content such as text, images, audio, and code based on the data they've been trained on. Unlike traditional AI that focuses on prediction or classification, generative AI creates new outputs.

## Key Generative AI Models

### GPT (Generative Pre-trained Transformer)
- Used for text generation, translation, summarization, Q&A, and creative writing
- Progressive versions (GPT-3, GPT-3.5, GPT-4) with increasing capabilities
- Foundation for many commercial AI assistants

### DALL-E
- Specialized in generating images from text descriptions
- Can create artistic, photorealistic, and conceptual images
- Used for design ideation, content creation, and visualization

### Whisper
- Speech recognition model that converts spoken language to text
- Supports multiple languages and can translate between them
- Works across various audio qualities and environments

## Common Generative AI Applications

1. **Content Creation**
   - Writing assistance (articles, emails, marketing copy)
   - Image generation for marketing, design, and art
   - Video and audio content creation

2. **Conversational AI**
   - Customer service chatbots
   - Virtual assistants with domain expertise
   - Interactive training and education tools

3. **Code Generation**
   - Autocomplete and suggestions for developers
   - Documentation generation
   - Code translation between programming languages

4. **Design and Creativity**
   - Product design ideation
   - UI/UX prototyping
   - Creative problem-solving

## Azure OpenAI Service Demo Setup

To use Azure OpenAI Service, follow these steps:

1. **Prerequisites**:
   - Azure subscription
   - Azure OpenAI Service access (requires application)
   - Understanding of prompt engineering basics

2. **Resource Setup**:
   ```bash
   # Create resource group
   az group create --name rg-openai-demo --location eastus
   
   # Deploy Azure OpenAI resource
   az cognitiveservices account create \
     --name openai-demo-account \
     --resource-group rg-openai-demo \
     --kind OpenAI \
     --sku S0 \
     --location eastus
   
   # Get the endpoint and keys
   az cognitiveservices account show --name openai-demo-account \
     --resource-group rg-openai-demo \
     --query properties.endpoint \
     --output tsv
   
   az cognitiveservices account keys list \
     --name openai-demo-account \
     --resource-group rg-openai-demo
   ```

3. **Deploy a Model**:
   - Navigate to Azure OpenAI Studio
   - Select "Deployments" from the left menu
   - Click "Create new deployment"
   - Select model (e.g., "gpt-35-turbo" for chat completions)
   - Provide a deployment name and click "Create"

## Example: Text Generation with Azure OpenAI

```python
import os
import openai

# Setup the OpenAI client
openai.api_type = "azure"
openai.api_version = "2023-05-15"  # Check for latest version
openai.api_base = "YOUR_AZURE_OPENAI_ENDPOINT"
openai.api_key = "YOUR_AZURE_OPENAI_KEY"

# Set deployment name
deployment_name = "YOUR_DEPLOYMENT_NAME"  # e.g., "gpt-35-turbo-deployment"

# Example prompt
prompt = "Write a short paragraph explaining artificial intelligence to a 10-year-old child."

# Call the OpenAI API
response = openai.ChatCompletion.create(
    engine=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that explains complex topics in simple terms."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=150
)

# Display the response
print(response.choices[0].message.content)
```

## Example: Image Generation with DALL-E

```python
import os
import openai
import requests
from PIL import Image
from io import BytesIO

# Setup the OpenAI client
openai.api_type = "azure"
openai.api_version = "2023-06-01-preview"  # DALL-E specific version
openai.api_base = "YOUR_AZURE_OPENAI_ENDPOINT"
openai.api_key = "YOUR_AZURE_OPENAI_KEY"

# Image prompt
image_prompt = "A futuristic city with flying cars and tall glass buildings under a sunset sky, digital art style"

# Generate image
response = openai.Image.create(
    prompt=image_prompt,
    size="1024x1024",
    n=1
)

# Get image URL
image_url = response.data[0].url

# Download and display image
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.save("generated_image.png")
print(f"Image saved as 'generated_image.png'")
```

## Responsible AI Considerations

### Potential Issues with Generative AI

1. **Misinformation and Hallucinations**
   - AI can generate plausible-sounding but incorrect information
   - Models may "hallucinate" facts and details that don't exist

2. **Bias and Fairness**
   - Models can perpetuate or amplify biases present in training data
   - May produce stereotypical or discriminatory content

3. **Content Safety**
   - Potential to generate harmful, inappropriate, or offensive content
   - Need for robust content filtering and moderation

4. **Copyright and Ownership**
   - Questions around ownership of AI-generated content
   - Potential copyright issues when models trained on copyrighted material

### Mitigation Strategies

1. **Implement Content Filters**
   ```python
   # Example of content moderation
   response = openai.Completion.create(
       engine=deployment_name,
       prompt=user_input,
       temperature=0.5,
       max_tokens=100,
       content_filter={
           "hate": True,
           "hate/threatening": True,
           "self-harm": True,
           "sexual": True,
           "sexual/minors": True,
           "violence": True,
           "violence/graphic": True
       }
   )
   ```

2. **Set Clear System Messages**
   ```python
   messages=[
       {"role": "system", "content": "You are a helpful assistant. Always provide factual, accurate information. If you're unsure, acknowledge your uncertainty. Never provide harmful or misleading content."},
       {"role": "user", "content": user_prompt}
   ]
   ```

3. **Human-in-the-Loop**
   - Implement human review for sensitive use cases
   - Create feedback loops to improve AI outputs

4. **Transparent Communication**
   - Clearly communicate when content is AI-generated
   - Provide disclaimers about potential limitations and errors

## Exercise: Design a Generative AI Solution

1. **Identify a Business Problem**:
   - Choose a specific business challenge that generative AI could address
   - Define clear objectives and success criteria

2. **Select Appropriate Model**:
   - Determine which generative model best fits your use case
   - Consider model capabilities, limitations, and costs

3. **Design Prompt Strategy**:
   - Develop effective prompts for your specific use case
   - Include system messages to guide model behavior

4. **Implement Responsible AI Controls**:
   - Content filtering and moderation
   - Human review process
   - Bias detection and mitigation

5. **Measure and Evaluate**:
   - Define metrics to evaluate performance
   - Create a feedback loop for continuous improvement

## Resources

- [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Responsible AI Practices](https://www.microsoft.com/en-us/ai/responsible-ai)
- [Prompt Engineering Guide](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/prompt-engineering) 