/**
 * Azure OpenAI Service Demo - AI-900
 *
 * This script demonstrates basic interaction with Azure OpenAI Service for:
 * 1. Text generation (completions)
 * 2. Chat interaction
 * 3. Image generation
 *
 * Requirements:
 * - Azure subscription
 * - Azure OpenAI Service resource
 * - Node.js installed
 */

// Import required packages
// To install: npm install @azure/openai dotenv

require('dotenv').config();
const { OpenAIClient, AzureKeyCredential } = require('@azure/openai');

// Load environment variables from .env file
const apiKey = process.env.TIMTAR_DEPLOYMENT_KEY;
const endpoint = process.env.TIMTAR_DEPLOYMENT_URI;
const deploymentName = process.env.DEPLOYMENT_NAME || "YOUR_DEPLOYMENT_NAME"; // e.g., "gpt-35-turbo"
const imageDeploymentName = process.env.IMAGE_DEPLOYMENT_NAME || "YOUR_DALLE_DEPLOYMENT_NAME"; // e.g., "dall-e-3"

// Initialize the OpenAI client
const client = new OpenAIClient(endpoint, new AzureKeyCredential(apiKey));

/**
 * Generate text using completion API
 */
async function generateText() {
  console.log("\n===== Text Generation Demo =====");

  try {
    // Define a simple prompt
    const prompt = "Write a short introduction to artificial intelligence for beginners:";
    console.log(`Prompt: ${prompt}`);

    // Get completions from the model
    const result = await client.getCompletions(deploymentName, [prompt], {
      maxTokens: 150,
      temperature: 0.7,
      topP: 0.95,
    });

    // Print the generated text
    for (const choice of result.choices) {
      console.log(`\nGenerated text: ${choice.text}`);
    }
  } catch (error) {
    console.error("Error generating text:", error);
  }
}

/**
 * Demonstrate chat interactions
 */
async function chatWithAI() {
  console.log("\n===== Chat Interaction Demo =====");

  try {
    // Define the conversation
    const messages = [
      { role: "system", content: "You are a helpful AI assistant that explains AI concepts in simple terms." },
      { role: "user", content: "What is machine learning and how is it used in everyday applications?" }
    ];

    console.log("User: What is machine learning and how is it used in everyday applications?");

    // Get a response from the chat model
    const result = await client.getChatCompletions(deploymentName, messages, {
      maxTokens: 300,
      temperature: 0.7,
    });

    // Print the response
    for (const choice of result.choices) {
      console.log(`\nAI Assistant: ${choice.message.content}`);
    }
  } catch (error) {
    console.error("Error in chat interaction:", error);
  }
}

/**
 * Generate an image using DALL-E
 */
async function generateImage() {
  console.log("\n===== Image Generation Demo =====");

  try {
    // Image prompt
    const prompt = "A friendly robot teaching a group of diverse students about AI, digital art style";
    console.log(`Generating image with prompt: "${prompt}"`);

    // Generate image
    const imageResult = await client.getImages(imageDeploymentName, prompt, { n: 1 });

    // Print the image URL
    if (imageResult.data && imageResult.data.length > 0) {
      console.log(`\nImage generated! URL: ${imageResult.data[0].url}`);
      console.log("To view the image, copy and paste the URL into your browser.");
    } else {
      console.log("No images were generated.");
    }
  } catch (error) {
    console.error("Error generating image:", error);
  }
}

/**
 * Demonstrate code generation capabilities
 */
async function generateCode() {
  console.log("\n===== Code Generation Demo =====");

  try {
    // Define a code generation prompt
    const messages = [
      { role: "system", content: "You are a helpful coding assistant." },
      { role: "user", content: "Write a simple Python function that calculates the average of a list of numbers" }
    ];

    console.log("User: Write a simple Python function that calculates the average of a list of numbers");

    // Get a response from the chat model for code
    const result = await client.getChatCompletions(deploymentName, messages, {
      maxTokens: 300,
      temperature: 0.3, // Lower temperature for more precise code
    });

    // Print the response
    for (const choice of result.choices) {
      console.log(`\nAI Code Assistant: ${choice.message.content}`);
    }
  } catch (error) {
    console.error("Error generating code:", error);
  }
}

/**
 * Main function to run all demos
 */
async function main() {
  console.log("Azure OpenAI Service Demo for AI-900\n");

  try {
    // Run the text generation demo
    await generateText();

    // Run the chat interaction demo
    await chatWithAI();

    // Run the code generation demo
    await generateCode();

    // Run the image generation demo
    await generateImage();

    console.log("\nAll demos completed successfully!");
  } catch (error) {
    console.error("Error in main function:", error);
  }
}

// Run the main function
main().catch((error) => {
  console.error("Unhandled error in main:", error);
});

/**
 * How to use this demo:
 *
 * 1. Create a .env file with your Azure OpenAI credentials:
 *    AZURE_OPENAI_API_KEY=your_api_key
 *    AZURE_OPENAI_ENDPOINT=your_endpoint
 *    DEPLOYMENT_NAME=your_model_deployment_name
 *    IMAGE_DEPLOYMENT_NAME=your_dalle_deployment_name
 *
 * 2. Install dependencies:
 *    npm install @azure/openai dotenv
 *
 * 3. Run the script:
 *    node azure-openai-quickstart.js
 */
