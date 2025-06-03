# Azure OpenAI Service: Beginner's Guide

This guide provides a straightforward introduction to Azure OpenAI Service capabilities for beginners studying for the AI-900 certification.

## What is Azure OpenAI Service?

Azure OpenAI Service is a cloud-based offering that gives you access to powerful AI models like GPT-4, GPT-3.5, DALL-E, and others in a secure Azure environment. It lets you integrate advanced AI capabilities into your applications without having to build or train complex AI models yourself.

## What Can Azure OpenAI Service Do?

For beginners, the three main capabilities to understand are:

1. **Text Generation**: Creating human-like text based on prompts
2. **Code Generation**: Writing or completing code snippets
3. **Image Generation**: Creating images from text descriptions

## Demo Script Overview

The `azure-openai-quickstart.js` script in this folder demonstrates these three key capabilities using simple examples:

- Text generation using completions API
- Chat interactions
- Code generation
- Image generation with DALL-E

## Running the Demo

### Prerequisites

- An Azure account
- An Azure OpenAI Service resource (requires application approval)
- Node.js installed on your computer
- Basic understanding of JavaScript (but you don't need to be an expert!)

### Step 1: Set Up Your Azure OpenAI Service

1. Apply for access to Azure OpenAI Service at [https://aka.ms/oaiapply](https://aka.ms/oaiapply)
2. Once approved, create an Azure OpenAI resource in the Azure portal
3. Deploy models through Azure OpenAI Studio:
   - Text/chat model (like "gpt-35-turbo")
   - Image generation model (like "dall-e-3")
4. Note your endpoint URL and API key

### Step 2: Prepare Your Environment

1. Create a new folder for your project
2. Create a file named `.env` with the following content:
   ```
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_ENDPOINT=your_endpoint
   DEPLOYMENT_NAME=your_text_model_deployment_name
   IMAGE_DEPLOYMENT_NAME=your_dalle_deployment_name
   ```
3. Open a terminal and run:
   ```
   npm init -y
   npm install @azure/openai dotenv
   ```

### Step 3: Run the Demo

1. Copy the `azure-openai-quickstart.js` script into your project folder
2. Run the script:
   ```
   node azure-openai-quickstart.js
   ```
3. Observe the output for each capability demo

## Understanding the Script

The script is divided into separate functions, each demonstrating a different Azure OpenAI capability:

- `generateText()`: Shows how to generate text completions
- `chatWithAI()`: Demonstrates interactive chat conversations
- `generateCode()`: Shows how to generate code examples
- `generateImage()`: Creates images based on text descriptions

## Customizing the Prompts

Feel free to modify the prompts in the script to see different responses:

- Change the prompt in `generateText()` to generate different content
- Modify the user message in `chatWithAI()` to ask different questions
- Change the code request in `generateCode()` to generate different code samples
- Update the image prompt in `generateImage()` to create different images

## Important Concepts for AI-900

As you work with this demo, keep these key concepts in mind:

1. **Prompts**: Text instructions that guide the AI models
2. **Tokens**: Units of text (roughly 4 characters) that the model processes
3. **Temperature**: Controls randomness (0=deterministic, 1=creative)
4. **Maximum tokens**: Limits the length of the generated response

## Resources for Learning More

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Azure OpenAI Service Overview](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview)
- [Prompt Engineering Guide](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/prompt-engineering)
- [Microsoft Learn AI-900 Modules](https://learn.microsoft.com/en-us/training/paths/get-started-with-artificial-intelligence-on-azure/) 