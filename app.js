#!/usr/bin/env node
'use strict';

// 🚀 AI-900 Grand Unified Demo Console App
// By Tim Warner - Your AI Learning Companion
// ============================================

require('dotenv').config();
const chalk = require('chalk');
const figlet = require('figlet');
const inquirer = require('inquirer');
const path = require('path');
const fs = require('fs').promises;

// Azure AI SDK imports
const { ComputerVisionClient } = require('@azure/cognitiveservices-computervision');
const { CognitiveServicesCredentials } = require('@azure/ms-rest-azure-js');
const { TextAnalyticsClient, AzureKeyCredential } = require('@azure/ai-text-analytics');
const { DocumentAnalysisClient } = require('@azure/ai-form-recognizer');
const { OpenAI } = require('openai');
const axios = require('axios');

// 🧠 AI Service Clients
let visionClient, textClient, formClient, openaiClient;

// 🎨 Console styling
const styles = {
    title: chalk.cyan.bold,
    success: chalk.green,
    error: chalk.red.bold,
    warning: chalk.yellow,
    info: chalk.blue,
    highlight: chalk.magenta.bold,
    muted: chalk.gray
};

// 🎯 Main Application Class
class AI900Demo {
    constructor() {
        this.isRunning = true;
        this.initializeClients();
    }

    // 🔧 Initialize Azure AI clients
    async initializeClients() {
        try {
            // Computer Vision
            if (process.env.COMPUTER_VISION_KEY && process.env.COMPUTER_VISION_ENDPOINT) {
                const credentials = new CognitiveServicesCredentials(process.env.COMPUTER_VISION_KEY);
                visionClient = new ComputerVisionClient(credentials, process.env.COMPUTER_VISION_ENDPOINT);
            }

            // Text Analytics / Language Service
            if (process.env.LANGUAGE_SERVICE_KEY && process.env.LANGUAGE_SERVICE_ENDPOINT) {
                textClient = new TextAnalyticsClient(
                    process.env.LANGUAGE_SERVICE_ENDPOINT,
                    new AzureKeyCredential(process.env.LANGUAGE_SERVICE_KEY)
                );
            }

            // Document Intelligence
            if (process.env.DOCUMENT_INTELLIGENCE_KEY && process.env.DOCUMENT_INTELLIGENCE_ENDPOINT) {
                formClient = new DocumentAnalysisClient(
                    process.env.DOCUMENT_INTELLIGENCE_ENDPOINT,
                    new AzureKeyCredential(process.env.DOCUMENT_INTELLIGENCE_KEY)
                );
            }

            // Azure OpenAI
            if (process.env.AZURE_OPENAI_KEY && process.env.AZURE_OPENAI_ENDPOINT) {
                openaiClient = new OpenAI({
                    apiKey: process.env.AZURE_OPENAI_KEY,
                    baseURL: `${process.env.AZURE_OPENAI_ENDPOINT}/openai/deployments/gpt-35-turbo`,
                    defaultQuery: { 'api-version': '2023-12-01-preview' },
                    defaultHeaders: {
                        'api-key': process.env.AZURE_OPENAI_KEY,
                    }
                });
            }

        } catch (error) {
            console.log(styles.warning('⚠️  Some services may not be available. Check your .env file.'));
        }
    }

    // 🎨 Display awesome banner
    displayBanner() {
        console.clear();
        console.log(styles.title(figlet.textSync('AI-900 DEMO', { horizontalLayout: 'full' })));
        console.log(styles.highlight('🚀 Azure AI Services Grand Unified Demo'));
        console.log(styles.info('   By Tim Warner - Microsoft MVP\n'));
        console.log(styles.muted('   Contoso Corp. - Innovation Through Intelligence\n'));
        console.log(styles.muted('═'.repeat(60)));
    }

    // 📋 Main menu
    async showMainMenu() {
        const choices = [
            { name: '🖼️  Computer Vision - Analyze Images', value: 'vision' },
            { name: '📝 Language Service - Text Analytics', value: 'language' },
            { name: '📄 Document Intelligence - Extract Data', value: 'document' },
            { name: '🎤 Speech Services - Voice Magic', value: 'speech' },
            { name: '🤖 Azure OpenAI - Generative AI', value: 'openai' },
            { name: '🔍 Search - Find Anything', value: 'search' },
            { name: '🛡️  Content Safety - Keep It Clean', value: 'safety' },
            { name: '🎨 Custom Vision - Your AI Models', value: 'custom' },
            { name: '🌐 Launch Web Interface', value: 'web' },
            new inquirer.Separator(),
            { name: '❌ Exit Application', value: 'exit' }
        ];

        const { choice } = await inquirer.prompt([{
            type: 'list',
            name: 'choice',
            message: 'Choose your AI adventure:',
            choices: choices,
            pageSize: 12
        }]);

        return choice;
    }

    // 🖼️ Computer Vision Demo
    async runVisionDemo() {
        console.log(styles.title('\n🖼️  COMPUTER VISION DEMO'));
        console.log(styles.info('Analyzing Contoso product images...\n'));

        const imageChoices = [
            { name: '👤 Analyze People (Celebrity Recognition)', value: 'people' },
            { name: '🥕 Analyze Products (Carrot Classification)', value: 'products' },
            { name: '📍 Analyze Places (Scene Recognition)', value: 'places' },
            { name: '🔤 Extract Text (OCR)', value: 'ocr' },
            { name: '⬅️  Back to Main Menu', value: 'back' }
        ];

        const { imageChoice } = await inquirer.prompt([{
            type: 'list',
            name: 'imageChoice',
            message: 'What would you like to analyze?',
            choices: imageChoices
        }]);

        if (imageChoice === 'back') return;

        try {
            let imagePath;
            switch (imageChoice) {
                case 'people':
                    imagePath = path.join(__dirname, 'assets', 'People', 'celebrity01.jpg');
                    await this.analyzeImage(imagePath, 'Celebrity Detection for Contoso Marketing');
                    break;
                case 'products':
                    imagePath = path.join(__dirname, 'assets', 'Things', 'Carrot1.JPG');
                    await this.analyzeImage(imagePath, 'Contoso Agricultural Product Analysis');
                    break;
                case 'places':
                    imagePath = path.join(__dirname, 'assets', 'Places', 'bridge.jpg');
                    await this.analyzeImage(imagePath, 'Contoso Real Estate Location Analysis');
                    break;
                case 'ocr':
                    imagePath = path.join(__dirname, 'assets', 'OCR', 'business-card-english.jpg');
                    await this.extractText(imagePath);
                    break;
            }
        } catch (error) {
            console.log(styles.error(`❌ Error: ${error.message}`));
        }

        await this.waitForUser();
    }

    // 🔍 Analyze image with Computer Vision
    async analyzeImage(imagePath, context) {
        if (!visionClient) {
            throw new Error('Computer Vision client not initialized. Check your .env configuration.');
        }

        console.log(styles.info(`🔍 Analyzing: ${context}`));
        console.log(styles.muted(`📁 File: ${path.basename(imagePath)}\n`));

        const imageBuffer = await fs.readFile(imagePath);
        const analysis = await visionClient.analyzeImageInStream(imageBuffer, {
            visualFeatures: ['Categories', 'Description', 'Objects', 'Tags', 'Adult', 'Color', 'Faces']
        });

        // Display results
        console.log(styles.success('✅ Analysis Complete!\n'));

        if (analysis.description.captions.length > 0) {
            console.log(styles.highlight('🎯 AI Description:'));
            console.log(`   "${analysis.description.captions[0].text}" (${Math.round(analysis.description.captions[0].confidence * 100)}% confidence)\n`);
        }

        if (analysis.tags.length > 0) {
            console.log(styles.highlight('🏷️  Detected Tags:'));
            analysis.tags.slice(0, 8).forEach(tag => {
                console.log(`   • ${tag.name} (${Math.round(tag.confidence * 100)}%)`);
            });
            console.log('');
        }

        if (analysis.objects.length > 0) {
            console.log(styles.highlight('🎯 Objects Found:'));
            analysis.objects.forEach(obj => {
                console.log(`   • ${obj.object} at (${obj.rectangle.x}, ${obj.rectangle.y})`);
            });
            console.log('');
        }

        if (analysis.faces.length > 0) {
            console.log(styles.highlight('👥 Faces Detected:'));
            analysis.faces.forEach((face, i) => {
                console.log(`   • Person ${i+1}: ${face.gender}, ~${face.age} years old`);
            });
            console.log('');
        }
    }

    // 📝 Extract text from image
    async extractText(imagePath) {
        console.log(styles.info('📝 Extracting text from business card...\n'));

        if (!visionClient) {
            throw new Error('Computer Vision client not initialized.');
        }

        const imageBuffer = await fs.readFile(imagePath);
        const ocrResult = await visionClient.readInStream(imageBuffer);

        // Get operation ID and poll for results
        const operationId = ocrResult.operationLocation.split('/').slice(-1)[0];

        let result;
        do {
            await new Promise(resolve => setTimeout(resolve, 1000));
            result = await visionClient.getReadResult(operationId);
        } while (result.status === 'running' || result.status === 'notStarted');

        if (result.status === 'succeeded') {
            console.log(styles.success('✅ Text Extraction Complete!\n'));
            console.log(styles.highlight('📋 Extracted Text:'));

            result.analyzeResult.readResults.forEach(page => {
                page.lines.forEach(line => {
                    console.log(`   ${line.text}`);
                });
            });
        }
    }

    // 📝 Language Service Demo
    async runLanguageDemo() {
        console.log(styles.title('\n📝 LANGUAGE SERVICE DEMO'));
        console.log(styles.info('Analyzing Contoso customer feedback...\n'));

        const textSamples = [
            "I absolutely love the new Contoso products! The quality is amazing and delivery was super fast. Will definitely order again!",
            "The Contoso service was disappointing. My order arrived late and the product was damaged. Very frustrated with this experience.",
            "Contoso has been my go-to company for years. Consistent quality and great customer service. Keep up the excellent work!",
            "La nueva línea de productos de Contoso es increíble. ¡Excelente calidad y precio justo!",
            "J'adore les nouveaux produits Contoso. La qualité est exceptionnelle et le service client est fantastique!"
        ];

        if (!textClient) {
            console.log(styles.error('❌ Language Service client not initialized. Check your .env configuration.'));
            await this.waitForUser();
            return;
        }

        for (let i = 0; i < textSamples.length; i++) {
            const text = textSamples[i];
            console.log(styles.highlight(`📝 Customer Review #${i + 1}:`));
            console.log(styles.muted(`"${text}"\n`));

            try {
                // Sentiment Analysis
                const sentimentResults = await textClient.analyzeSentiment([text]);
                const sentiment = sentimentResults[0];

                const sentimentIcon = sentiment.sentiment === 'positive' ? '😊' :
                                    sentiment.sentiment === 'negative' ? '😞' : '😐';

                console.log(styles.success(`${sentimentIcon} Sentiment: ${sentiment.sentiment.toUpperCase()} (${Math.round(sentiment.confidenceScores[sentiment.sentiment] * 100)}%)`));

                // Language Detection
                const languageResults = await textClient.detectLanguage([text]);
                const language = languageResults[0].primaryLanguage;
                console.log(styles.info(`🌍 Language: ${language.name} (${language.iso6391Name}) - ${Math.round(language.confidenceScore * 100)}% confidence`));

                // Key Phrases
                const keyPhraseResults = await textClient.extractKeyPhrases([text]);
                const keyPhrases = keyPhraseResults[0].keyPhrases;
                if (keyPhrases.length > 0) {
                    console.log(styles.info(`🔑 Key Phrases: ${keyPhrases.join(', ')}`));
                }

                console.log(styles.muted('─'.repeat(50)));

            } catch (error) {
                console.log(styles.error(`❌ Analysis failed: ${error.message}`));
            }
        }

        await this.waitForUser();
    }

    // 📄 Document Intelligence Demo
    async runDocumentDemo() {
        console.log(styles.title('\n📄 DOCUMENT INTELLIGENCE DEMO'));
        console.log(styles.info('Processing Contoso business documents...\n'));

        const docChoices = [
            { name: '🧾 Analyze Receipt', value: 'receipt' },
            { name: '📄 Analyze Invoice', value: 'invoice' },
            { name: '💳 Analyze Business Card', value: 'business_card' },
            { name: '⬅️  Back to Main Menu', value: 'back' }
        ];

        const { docChoice } = await inquirer.prompt([{
            type: 'list',
            name: 'docChoice',
            message: 'Which document type would you like to analyze?',
            choices: docChoices
        }]);

        if (docChoice === 'back') return;

        if (!formClient) {
            console.log(styles.error('❌ Document Intelligence client not initialized. Check your .env configuration.'));
            await this.waitForUser();
            return;
        }

        try {
            let documentPath;
            switch (docChoice) {
                case 'receipt':
                    documentPath = path.join(__dirname, 'assets', 'OCR', 'contoso-receipt.png');
                    await this.analyzeReceipt(documentPath);
                    break;
                case 'invoice':
                    documentPath = path.join(__dirname, 'assets', 'OCR', 'Invoice_1.pdf');
                    await this.analyzeInvoice(documentPath);
                    break;
                case 'business_card':
                    documentPath = path.join(__dirname, 'assets', 'OCR', 'business-card-english.jpg');
                    await this.analyzeBusinessCard(documentPath);
                    break;
            }
        } catch (error) {
            console.log(styles.error(`❌ Document analysis failed: ${error.message}`));
        }

        await this.waitForUser();
    }

    // 🧾 Analyze receipt
    async analyzeReceipt(filePath) {
        console.log(styles.info('🧾 Analyzing Contoso receipt...\n'));

        const fileBuffer = await fs.readFile(filePath);
        const poller = await formClient.beginAnalyzeDocument("prebuilt-receipt", fileBuffer);
        const { documents } = await poller.pollUntilDone();

        if (documents && documents.length > 0) {
            const receipt = documents[0];
            console.log(styles.success('✅ Receipt Analysis Complete!\n'));

            console.log(styles.highlight('🏪 Receipt Details:'));
            if (receipt.fields.MerchantName?.value) {
                console.log(`   Merchant: ${receipt.fields.MerchantName.value}`);
            }
            if (receipt.fields.TransactionDate?.value) {
                console.log(`   Date: ${receipt.fields.TransactionDate.value.toDateString()}`);
            }
            if (receipt.fields.Total?.value) {
                console.log(`   Total: $${receipt.fields.Total.value}`);
            }

            if (receipt.fields.Items?.values) {
                console.log(styles.highlight('\n🛒 Items:'));
                receipt.fields.Items.values.forEach((item, i) => {
                    const name = item.properties.Name?.value || 'Unknown item';
                    const price = item.properties.TotalPrice?.value || 0;
                    console.log(`   ${i + 1}. ${name} - $${price}`);
                });
            }
        }
    }

    // 🤖 Azure OpenAI Demo
    async runOpenAIDemo() {
        console.log(styles.title('\n🤖 AZURE OPENAI DEMO'));
        console.log(styles.info('Contoso AI Assistant - Powered by GPT\n'));

        if (!openaiClient) {
            console.log(styles.error('❌ Azure OpenAI client not initialized. Check your .env configuration.'));
            await this.waitForUser();
            return;
        }

        const prompts = [
            "Write a professional email to a Contoso customer apologizing for a delayed shipment and offering a 10% discount on their next order.",
            "Create a product description for Contoso's new smart home device that focuses on energy efficiency and user-friendly features.",
            "Generate 3 creative marketing taglines for Contoso's sustainable product line.",
            "Write a brief summary of how AI can transform customer service operations at Contoso."
        ];

        for (let i = 0; i < prompts.length; i++) {
            console.log(styles.highlight(`🎯 Prompt ${i + 1}:`));
            console.log(styles.muted(`${prompts[i]}\n`));

            try {
                console.log(styles.info('🧠 Thinking...'));

                const completion = await openaiClient.chat.completions.create({
                    messages: [
                        { role: "system", content: "You are a helpful AI assistant working for Contoso Corporation, a technology company focused on innovation and customer satisfaction." },
                        { role: "user", content: prompts[i] }
                    ],
                    max_tokens: 300
                });

                console.log(styles.success('\n✅ AI Response:'));
                console.log(`${completion.choices[0].message.content}\n`);
                console.log(styles.muted('─'.repeat(60)));

            } catch (error) {
                console.log(styles.error(`❌ AI request failed: ${error.message}`));
            }
        }

        await this.waitForUser();
    }

    // 🎤 Speech Services Demo (Placeholder)
    async runSpeechDemo() {
        console.log(styles.title('\n🎤 SPEECH SERVICES DEMO'));
        console.log(styles.info('Contoso Voice Intelligence\n'));
        console.log(styles.warning('🚧 Speech demo requires audio setup and will be implemented in the web version.'));
        console.log(styles.info('\nFeatures available in web interface:'));
        console.log('   • 🎤 Speech-to-Text conversion');
        console.log('   • 🔊 Text-to-Speech synthesis');
        console.log('   • 🌍 Real-time translation');
        console.log('   • 🎵 Audio analysis\n');

        await this.waitForUser();
    }

    // 🔍 Search Demo (Placeholder)
    async runSearchDemo() {
        console.log(styles.title('\n🔍 SEARCH SERVICES DEMO'));
        console.log(styles.info('Contoso Intelligent Search\n'));
        console.log(styles.warning('🚧 Search demo requires Azure Cognitive Search setup.'));
        console.log(styles.info('\nCapabilities:'));
        console.log('   • 🔍 Full-text search across documents');
        console.log('   • 🧠 AI-powered search suggestions');
        console.log('   • 📊 Faceted search results');
        console.log('   • 🎯 Semantic search understanding\n');

        await this.waitForUser();
    }

    // 🛡️ Content Safety Demo (Placeholder)
    async runSafetyDemo() {
        console.log(styles.title('\n🛡️  CONTENT SAFETY DEMO'));
        console.log(styles.info('Contoso Content Protection\n'));
        console.log(styles.warning('🚧 Content Safety requires additional API setup.'));
        console.log(styles.info('\nProtection Features:'));
        console.log('   • 🚫 Harmful content detection');
        console.log('   • 🔞 Adult content filtering');
        console.log('   • 💬 Hate speech identification');
        console.log('   • ⚖️  Content moderation scoring\n');

        await this.waitForUser();
    }

    // 🎨 Custom Vision Demo (Placeholder)
    async runCustomVisionDemo() {
        console.log(styles.title('\n🎨 CUSTOM VISION DEMO'));
        console.log(styles.info('Contoso Custom AI Models\n'));
        console.log(styles.warning('🚧 Custom Vision requires trained models.'));
        console.log(styles.info('\nModel Capabilities:'));
        console.log('   • 🏷️  Custom image classification');
        console.log('   • 🎯 Object detection for specific items');
        console.log('   • 📊 Model performance metrics');
        console.log('   • 🔄 Continuous learning from feedback\n');

        await this.waitForUser();
    }

    // 🌐 Launch Web Interface
    async launchWebInterface() {
        console.log(styles.title('\n🌐 LAUNCHING WEB INTERFACE'));
        console.log(styles.info('Starting Contoso AI Web Portal...\n'));

        // Force close any existing processes on port 3000
        require('child_process').exec('lsof -ti:3000 | xargs kill -9 2>/dev/null', () => {
            console.log(styles.success('🔧 Port 3000 is ready!'));
        });

        setTimeout(async () => {
            try {
                require('./web-server.js');
                console.log(styles.success('🚀 Web server starting...'));
                console.log(styles.highlight('🌐 Open your browser to: http://localhost:3000'));
                console.log(styles.info('\n   Press Ctrl+C to return to console menu\n'));
            } catch (error) {
                console.log(styles.error(`❌ Failed to start web server: ${error.message}`));
                await this.waitForUser();
            }
        }, 1000);
    }

    // ⏳ Wait for user input
    async waitForUser() {
        await inquirer.prompt([{
            type: 'input',
            name: 'continue',
            message: 'Press Enter to continue...'
        }]);
    }

    // 🚀 Main application loop
    async run() {
        while (this.isRunning) {
            this.displayBanner();
            const choice = await this.showMainMenu();

            switch (choice) {
                case 'vision':
                    await this.runVisionDemo();
                    break;
                case 'language':
                    await this.runLanguageDemo();
                    break;
                case 'document':
                    await this.runDocumentDemo();
                    break;
                case 'speech':
                    await this.runSpeechDemo();
                    break;
                case 'openai':
                    await this.runOpenAIDemo();
                    break;
                case 'search':
                    await this.runSearchDemo();
                    break;
                case 'safety':
                    await this.runSafetyDemo();
                    break;
                case 'custom':
                    await this.runCustomVisionDemo();
                    break;
                case 'web':
                    await this.launchWebInterface();
                    break;
                case 'exit':
                    console.log(styles.success('\n🎯 Thanks for exploring Azure AI with Tim Warner!'));
                    console.log(styles.info('Keep learning, keep building! 🚀\n'));
                    this.isRunning = false;
                    break;
            }
        }
    }
}

// 🎬 Application Entry Point
if (require.main === module) {
    const app = new AI900Demo();
    app.run().catch(error => {
        console.error(styles.error('💥 Application Error:'), error);
        process.exit(1);
    });
}

module.exports = AI900Demo;
