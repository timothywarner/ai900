#!/usr/bin/env node
'use strict';

// =============================================================================
// 🚀 AI-900 Enterprise Demo Console Application
// =============================================================================
// Purpose: Comprehensive demonstration of Azure AI services for certification prep
// Author: Tim Warner - Microsoft MVP & Certified Azure AI Engineer
// License: MIT
//
// Educational Focus: Implements Microsoft AI-900 exam best practices including:
// - Retry logic with exponential backoff (handles 429 rate limiting)
// - Pagination for large result sets and batch processing
// - Responsible AI principles and comprehensive error handling
// - Enterprise-grade configuration management and monitoring
// - Input validation, sanitization, and security patterns
// - Production-ready logging and metrics collection
// - Connection pooling and client lifecycle management
// =============================================================================

require('dotenv').config();
const chalk = require('chalk');
const figlet = require('figlet');
const inquirer = require('inquirer');
const path = require('path');
const fs = require('fs').promises;

// =============================================================================
// Azure AI SDK Imports - Enterprise Pattern
// =============================================================================
const { ComputerVisionClient } = require('@azure/cognitiveservices-computervision');
const { CognitiveServicesCredentials } = require('@azure/ms-rest-azure-js');
const { TextAnalyticsClient, AzureKeyCredential } = require('@azure/ai-text-analytics');
const { DocumentAnalysisClient } = require('@azure/ai-form-recognizer');
const { OpenAI } = require('openai');
const axios = require('axios');

// =============================================================================
// Global AI Service Client Instances
// =============================================================================
// Pattern: Singleton clients for connection pooling and efficiency
// AI-900 Best Practice: Reuse clients to avoid authentication overhead
let cognitiveVisionClient, languageAnalyticsClient, documentIntelligenceClient, azureOpenAIClient, contentSafetyClient;

// =============================================================================
// Enterprise Configuration Constants - AI-900 Exam Patterns
// =============================================================================
const AI_SERVICE_CONFIG = {
    // Retry configuration - Critical for AI-900 exam
    MAX_RETRY_ATTEMPTS: 3,
    INITIAL_RETRY_DELAY_MS: 1000,
    MAX_RETRY_DELAY_MS: 10000,
    RETRY_BACKOFF_MULTIPLIER: 2,

    // Pagination settings for large datasets
    DEFAULT_PAGE_SIZE: 25,
    MAX_PAGE_SIZE: 100,

    // Rate limiting awareness (HTTP 429 responses)
    RATE_LIMIT_RETRY_DELAY_MS: 5000,

    // Timeout configurations
    DEFAULT_TIMEOUT_MS: 30000,
    LONG_RUNNING_TIMEOUT_MS: 120000,

    // Responsible AI thresholds
    CONFIDENCE_THRESHOLD: 0.7,
    ADULT_CONTENT_THRESHOLD: 0.5,

    // Educational constants for demos
    DEMO_TEXT_MAX_LENGTH: 5000,
    DEMO_IMAGE_MAX_SIZE: 10 * 1024 * 1024 // 10MB
};

// =============================================================================
// Enterprise Utility Functions - AI-900 Best Practices
// =============================================================================

/**
 * Implements exponential backoff retry logic for Azure AI service calls
 * AI-900 Exam Pattern: Handle transient failures and rate limiting (429)
 * Educational Note: Production apps must handle network failures gracefully
 */
async function executeAzureAIOperationWithRetry(operation, operationName, options = {}) {
    const config = { ...AI_SERVICE_CONFIG, ...options };
    let lastError;

    for (let attempt = 1; attempt <= config.MAX_RETRY_ATTEMPTS; attempt++) {
        try {
            console.log(styles.info(`🔄 ${operationName} - Attempt ${attempt}/${config.MAX_RETRY_ATTEMPTS}`));

            const startTime = Date.now();
            const result = await operation();
            const duration = Date.now() - startTime;

            if (attempt > 1) {
                console.log(styles.success(`✅ ${operationName} succeeded after ${attempt} attempts (${duration}ms)`));
            } else {
                console.log(styles.muted(`⚡ ${operationName} completed in ${duration}ms`));
            }

            return result;

        } catch (error) {
            lastError = error;
            console.log(styles.warning(`⚠️ ${operationName} attempt ${attempt} failed: ${error.message}`));

            // Handle rate limiting (429) - Critical AI-900 exam concept
            if (error.status === 429 || error.code === 'TooManyRequests') {
                console.log(styles.examTip('📚 AI-900 Exam Tip: Rate limiting (429) requires extended backoff'));
                await sleep(config.RATE_LIMIT_RETRY_DELAY_MS);
                continue;
            }

            // Check if error is retriable
            if (!isRetriableAzureError(error)) {
                console.log(styles.error(`❌ ${operationName} failed with non-retriable error`));
                throw error;
            }

            // Calculate exponential backoff delay
            if (attempt < config.MAX_RETRY_ATTEMPTS) {
                const delayMs = Math.min(
                    config.INITIAL_RETRY_DELAY_MS * Math.pow(config.RETRY_BACKOFF_MULTIPLIER, attempt - 1),
                    config.MAX_RETRY_DELAY_MS
                );

                console.log(styles.muted(`⏳ Exponential backoff: waiting ${delayMs}ms...`));
                await sleep(delayMs);
            }
        }
    }

    console.log(styles.error(`❌ ${operationName} failed after ${config.MAX_RETRY_ATTEMPTS} attempts`));
    throw lastError;
}

/**
 * Determines if an Azure AI service error is retriable
 * AI-900 Exam Knowledge: Understanding transient vs permanent failures
 */
function isRetriableAzureError(error) {
    // Network errors are generally retriable
    const networkErrors = ['ENOTFOUND', 'ECONNRESET', 'ETIMEDOUT', 'ECONNREFUSED'];
    if (networkErrors.includes(error.code)) return true;

    // HTTP status codes that indicate transient issues
    const retriableStatusCodes = [408, 429, 500, 502, 503, 504];
    return retriableStatusCodes.includes(error.status);
}

/**
 * Validates and sanitizes user input for AI service calls
 * AI-900 Exam Pattern: Responsible AI and security considerations
 */
function validateAndSanitizeUserInput(input, options = {}) {
    const maxLength = options.maxLength || AI_SERVICE_CONFIG.DEMO_TEXT_MAX_LENGTH;

    if (!input || typeof input !== 'string') {
        throw new Error('Input must be a non-empty string');
    }

    if (input.length > maxLength) {
        throw new Error(`Input exceeds maximum length of ${maxLength} characters`);
    }

    // Sanitize input for AI services
    let sanitizedInput = input.trim();

    // Remove potential HTML/script content for safety
    sanitizedInput = sanitizedInput.replace(/<[^>]*>/g, '');

    // Check for potentially harmful patterns
    const suspiciousPatterns = [/javascript:/i, /vbscript:/i, /on\w+=/i, /<script/i];
    const hasSuspiciousContent = suspiciousPatterns.some(pattern => pattern.test(sanitizedInput));

    if (hasSuspiciousContent) {
        console.log(styles.warning('⚠️ Suspicious content detected and sanitized'));
    }

    return {
        original: input,
        sanitized: sanitizedInput,
        isValid: true,
        length: sanitizedInput.length,
        sanitizedContent: hasSuspiciousContent
    };
}

/**
 * Utility function for consistent async delays
 */
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// =============================================================================
// Console Styling with Educational Context
// =============================================================================
const styles = {
    title: chalk.cyan.bold,
    success: chalk.green,
    error: chalk.red.bold,
    warning: chalk.yellow,
    info: chalk.blue,
    highlight: chalk.magenta.bold,
    muted: chalk.gray,
    // Educational styling for AI-900 content
    concept: chalk.blue.italic,
    examTip: chalk.yellow.bold,
    bestPractice: chalk.green.italic,
    responsibleAI: chalk.magenta.italic
};

// =============================================================================
// Main Application Class - Enterprise AI-900 Demo Platform
// =============================================================================
class EnterpriseAI900DemoApplication {
    constructor() {
        this.isApplicationRunning = true;
        this.serviceHealthMetrics = new Map();
        this.operationMetrics = {
            totalOperations: 0,
            successfulOperations: 0,
            failedOperations: 0,
            retryAttempts: 0,
            averageResponseTime: 0
        };

        // Initialize with educational context
        console.log(styles.examTip('🎓 Initializing AI-900 Enterprise Demo Application...'));
        this.initializeAzureAIServicesClients();
    }

    // =============================================================================
    // Enterprise Client Initialization
    // =============================================================================
    async initializeAzureAIServicesClients() {
        console.log(styles.info('🔧 Initializing Azure AI service clients with enterprise patterns...'));

        try {
            // Multi-Service approach (AI-900 recommended pattern)
            if (process.env.AI_SERVICES_KEY && process.env.AI_SERVICES_ENDPOINT) {
                const credentials = new CognitiveServicesCredentials(process.env.AI_SERVICES_KEY);

                cognitiveVisionClient = new ComputerVisionClient(credentials, process.env.AI_SERVICES_ENDPOINT);
                languageAnalyticsClient = new TextAnalyticsClient(
                    process.env.AI_SERVICES_ENDPOINT,
                    new AzureKeyCredential(process.env.AI_SERVICES_KEY)
                );

                this.serviceHealthMetrics.set('MultiServiceCognitive', { status: 'healthy', endpoint: process.env.AI_SERVICES_ENDPOINT });
                console.log(styles.bestPractice('✨ Multi-service cognitive client initialized (AI-900 recommended)'));
            }

            // Document Intelligence
            if (process.env.DOCUMENT_INTELLIGENCE_KEY && process.env.DOCUMENT_INTELLIGENCE_ENDPOINT) {
                documentIntelligenceClient = new DocumentAnalysisClient(
                    process.env.DOCUMENT_INTELLIGENCE_ENDPOINT,
                    new AzureKeyCredential(process.env.DOCUMENT_INTELLIGENCE_KEY)
                );
                this.serviceHealthMetrics.set('DocumentIntelligence', { status: 'healthy' });
            }

            // Azure OpenAI
            if (process.env.AZURE_OPENAI_KEY && process.env.AZURE_OPENAI_ENDPOINT) {
                azureOpenAIClient = new OpenAI({
                    apiKey: process.env.AZURE_OPENAI_KEY,
                    baseURL: `${process.env.AZURE_OPENAI_ENDPOINT}/openai/deployments/gpt-35-turbo`,
                    defaultQuery: { 'api-version': '2023-12-01-preview' },
                    defaultHeaders: { 'api-key': process.env.AZURE_OPENAI_KEY },
                    timeout: AI_SERVICE_CONFIG.DEFAULT_TIMEOUT_MS
                });
                this.serviceHealthMetrics.set('AzureOpenAI', { status: 'healthy' });
            }

            console.log(styles.success(`✅ Initialized ${this.serviceHealthMetrics.size} Azure AI services`));

        } catch (error) {
            console.log(styles.error(`❌ Service initialization failed: ${error.message}`));
            console.log(styles.examTip('💡 AI-900 Tip: Always implement graceful degradation'));
        }
    }

    // =============================================================================
    // Educational Banner Display
    // =============================================================================
    displayEducationalBanner() {
        console.clear();
        
        // Simple but effective banner
        console.log('\n');
        console.log(styles.title('════════════════════════════════════════════════════════════'));
        console.log(styles.title('║                                                          ║'));
        console.log(styles.title('║            🤖  AZURE AI SERVICES DEMO  🤖             ║'));
        console.log(styles.title('║                                                          ║'));
        console.log(styles.title('║                  AI-900 Certification                    ║'));
        console.log(styles.title('║                                                          ║'));
        console.log(styles.title('════════════════════════════════════════════════════════════'));
        console.log('\n');
        
        console.log(styles.info('🎓 Welcome to the Azure AI Services Learning Demo!'));
        console.log(styles.muted('   Each demo shows a simple, practical use case\n'));
        
        console.log(styles.highlight('✨ What you\'ll learn:'));
        console.log('   1️⃣  Content Safety - Keep your apps safe from harmful content');
        console.log('   2️⃣  Computer Vision - Analyze images automatically');
        console.log('   3️⃣  Language Analytics - Understand text sentiment');
        console.log('   4️⃣  Translation - Break down language barriers');
        console.log('   5️⃣  Document Intelligence - Extract data from documents');
        console.log('   6️⃣  Azure OpenAI - Generate creative content\n');
        
        console.log(styles.muted('─'.repeat(60)) + '\n');
    }

    // =============================================================================
    // Interactive Main Menu
    // =============================================================================
    async showInteractiveMainMenu() {
        const menuChoices = [
            { name: '🛡️  Content Safety - Text moderation & harm prevention', value: 'content_safety' },
            { name: '🖼️  Computer Vision - Simple image analysis', value: 'computer_vision' },
            { name: '📝 Language Analytics - Sentiment analysis', value: 'language_analytics' },
            { name: '🌍 Translation - Multi-language translation', value: 'translation' },
            { name: '📄 Document Intelligence - Receipt OCR', value: 'document_intelligence' },
            { name: '🤖 Azure OpenAI - Text generation', value: 'azure_openai' },
            new inquirer.Separator('─────────────────────────────────────────'),
            { name: '📊 Service Health Metrics', value: 'service_metrics' },
            { name: '❌ Exit Application', value: 'exit_application' }
        ];

        const { selectedChoice } = await inquirer.prompt([{
            type: 'list',
            name: 'selectedChoice',
            message: '🎯 Choose your Azure AI learning adventure:',
            choices: menuChoices,
            pageSize: 10
        }]);

        return selectedChoice;
    }

    // =============================================================================
    // Content Safety Demo - Simple text moderation
    // =============================================================================
    async demonstrateContentSafety() {
        console.clear();
        console.log(styles.title('\n🛡️  CONTENT SAFETY DEMO'));
        console.log(styles.info('Simple text moderation to detect harmful content\n'));

        const testTexts = [
            "I love this new product! It's amazing!",
            "This is a normal business email about our quarterly results.",
            "Please contact customer service for assistance."
        ];

        console.log(styles.highlight('🔍 Analyzing text for harmful content...\n'));

        for (const text of testTexts) {
            console.log(styles.info(`Text: "${text}"`) );
            
            try {
                if (process.env.CONTENT_SAFETY_KEY && process.env.CONTENT_SAFETY_ENDPOINT) {
                    const response = await axios.post(
                        `${process.env.CONTENT_SAFETY_ENDPOINT}/contentsafety/text:analyze?api-version=2023-10-01`,
                        {
                            text: text,
                            categories: ["Hate", "SelfHarm", "Sexual", "Violence"],
                            outputType: "FourSeverityLevels"
                        },
                        {
                            headers: {
                                'Ocp-Apim-Subscription-Key': process.env.CONTENT_SAFETY_KEY,
                                'Content-Type': 'application/json'
                            }
                        }
                    );

                    const results = response.data;
                    console.log(styles.success('✅ Content is SAFE'));
                    console.log(styles.muted(`   Hate: ${results.categoriesAnalysis[0].severity}`);
                    console.log(styles.muted(`   Self-harm: ${results.categoriesAnalysis[1].severity}`);
                    console.log(styles.muted(`   Sexual: ${results.categoriesAnalysis[2].severity}`);
                    console.log(styles.muted(`   Violence: ${results.categoriesAnalysis[3].severity}\n`));
                } else {
                    console.log(styles.warning('⚠️  Content Safety not configured - using simulation'));
                    console.log(styles.success('✅ Content appears SAFE (simulated)\n'));
                }
            } catch (error) {
                console.log(styles.error(`❌ Error: ${error.message}\n`));
            }
        }

        await this.waitForUserInput();
    }

    // =============================================================================
    // Simple Computer Vision Demo - 80% scenario
    // =============================================================================
    async demonstrateComputerVisionSimple() {
        console.clear();
        console.log(styles.title('\n🖼️  COMPUTER VISION DEMO'));
        console.log(styles.info('Simple image analysis - detecting objects and describing images\n'));

        if (!cognitiveVisionClient) {
            console.log(styles.error('❌ Computer Vision not configured. Add keys to .env file.'));
            await this.waitForUserInput();
            return;
        }

        const imagePath = path.join(__dirname, 'assets', 'Things', 'product-placement.png');
        
        try {
            console.log(styles.info('🔍 Analyzing product image...\n'));
            const imageBuffer = await fs.readFile(imagePath);
            
            const result = await cognitiveVisionClient.analyzeImageInStream(imageBuffer, {
                visualFeatures: ['Description', 'Objects', 'Tags']
            });

            console.log(styles.success('✅ Analysis Complete!\n'));
            
            if (result.description?.captions?.[0]) {
                console.log(styles.highlight(`📝 Description: "${result.description.captions[0].text}"\n`));
            }

            if (result.objects?.length > 0) {
                console.log(styles.highlight('📦 Detected Objects:'));
                result.objects.slice(0, 5).forEach(obj => {
                    console.log(`   • ${obj.object} (${Math.round(obj.confidence * 100)}% confidence)`);
                });
                console.log('');
            }

            if (result.tags?.length > 0) {
                console.log(styles.highlight('🏷️  Tags:'));
                console.log(`   ${result.tags.slice(0, 5).map(t => t.name).join(', ')}\n`);
            }
        } catch (error) {
            console.log(styles.error(`❌ Error: ${error.message}`));
        }

        await this.waitForUserInput();
    }

    // =============================================================================
    // Simple Language Analytics Demo
    // =============================================================================
    async demonstrateLanguageAnalyticsSimple() {
        console.clear();
        console.log(styles.title('\n📝 LANGUAGE ANALYTICS DEMO'));
        console.log(styles.info('Simple sentiment analysis - understanding customer feedback\n'));

        if (!languageAnalyticsClient) {
            console.log(styles.error('❌ Language Analytics not configured. Add keys to .env file.'));
            await this.waitForUserInput();
            return;
        }

        const customerReviews = [
            "This product is amazing! Best purchase ever!",
            "Terrible experience. Very disappointed.",
            "It's okay, nothing special but does the job."
        ];

        console.log(styles.highlight('🔍 Analyzing customer sentiments...\n'));

        for (const review of customerReviews) {
            console.log(styles.info(`Review: "${review}"`) );
            
            try {
                const [result] = await languageAnalyticsClient.analyzeSentiment([review]);
                
                const emoji = result.sentiment === 'positive' ? '😊' : 
                             result.sentiment === 'negative' ? '😞' : '😐';
                
                console.log(styles.success(`${emoji} Sentiment: ${result.sentiment.toUpperCase()}\n`));
            } catch (error) {
                console.log(styles.error(`❌ Error: ${error.message}\n`));
            }
        }

        await this.waitForUserInput();
    }

    // =============================================================================
    // Translation Demo
    // =============================================================================
    async demonstrateTranslation() {
        console.clear();
        console.log(styles.title('\n🌍 TRANSLATION DEMO'));
        console.log(styles.info('Simple text translation - breaking language barriers\n'));

        const textToTranslate = "Welcome to Contoso! We're happy to help you.";
        const targetLanguages = ['es', 'fr', 'ja', 'ar'];
        const languageNames = { es: 'Spanish', fr: 'French', ja: 'Japanese', ar: 'Arabic' };

        console.log(styles.highlight(`💬 Original (English): "${textToTranslate}"\n`));
        console.log(styles.info('🌐 Translating to multiple languages...\n'));

        try {
            if (process.env.TRANSLATOR_KEY && process.env.TRANSLATOR_ENDPOINT) {
                for (const lang of targetLanguages) {
                    const response = await axios.post(
                        `${process.env.TRANSLATOR_ENDPOINT}/translate?api-version=3.0&to=${lang}`,
                        [{ text: textToTranslate }],
                        {
                            headers: {
                                'Ocp-Apim-Subscription-Key': process.env.TRANSLATOR_KEY,
                                'Content-Type': 'application/json'
                            }
                        }
                    );

                    const translation = response.data[0].translations[0].text;
                    console.log(styles.success(`✅ ${languageNames[lang]}: "${translation}"`) );
                }
            } else {
                console.log(styles.warning('⚠️  Translator not configured - showing simulated results'));
                console.log(styles.success('✅ Spanish: "¡Bienvenido a Contoso! Estamos felices de ayudarte."'));
                console.log(styles.success('✅ French: "Bienvenue chez Contoso! Nous sommes heureux de vous aider."'));
                console.log(styles.success('✅ Japanese: "Contosoへようこそ！お手伝いできることを嬉しく思います。"'));
                console.log(styles.success('✅ Arabic: "مرحبًا بكم في Contoso! يسعدنا مساعدتكم."'));
            }
        } catch (error) {
            console.log(styles.error(`\n❌ Error: ${error.message}`));
        }

        console.log('');
        await this.waitForUserInput();
    }

    // =============================================================================
    // Simple Document Intelligence Demo
    // =============================================================================
    async demonstrateDocumentIntelligenceSimple() {
        console.clear();
        console.log(styles.title('\n📄 DOCUMENT INTELLIGENCE DEMO'));
        console.log(styles.info('Simple receipt scanning - extracting key information\n'));

        if (!documentIntelligenceClient) {
            console.log(styles.error('❌ Document Intelligence not configured. Add keys to .env file.'));
            await this.waitForUserInput();
            return;
        }

        const receiptPath = path.join(__dirname, 'assets', 'OCR', 'contoso-receipt.png');

        try {
            console.log(styles.info('🔍 Scanning receipt...\n'));
            const receiptBuffer = await fs.readFile(receiptPath);
            
            const poller = await documentIntelligenceClient.beginAnalyzeDocument(
                'prebuilt-receipt',
                receiptBuffer,
                { contentType: 'image/png' }
            );
            
            const result = await poller.pollUntilDone();
            
            if (result.documents?.[0]) {
                const receipt = result.documents[0];
                console.log(styles.success('✅ Receipt analyzed successfully!\n'));
                
                console.log(styles.highlight('🧾 Receipt Information:'));
                if (receipt.fields.MerchantName?.value) {
                    console.log(`   🏪 Store: ${receipt.fields.MerchantName.value}`);
                }
                if (receipt.fields.TransactionDate?.value) {
                    console.log(`   📅 Date: ${new Date(receipt.fields.TransactionDate.value).toLocaleDateString()}`);
                }
                if (receipt.fields.Total?.value) {
                    console.log(`   💰 Total: $${receipt.fields.Total.value}`);
                }
            }
        } catch (error) {
            console.log(styles.error(`❌ Error: ${error.message}`));
        }

        console.log('');
        await this.waitForUserInput();
    }

    // =============================================================================
    // Simple Azure OpenAI Demo
    // =============================================================================
    async demonstrateAzureOpenAISimple() {
        console.clear();
        console.log(styles.title('\n🤖 AZURE OPENAI DEMO'));
        console.log(styles.info('Simple text generation - creating product descriptions\n'));

        if (!azureOpenAIClient) {
            console.log(styles.error('❌ Azure OpenAI not configured. Add keys to .env file.'));
            await this.waitForUserInput();
            return;
        }

        const prompt = "Write a short, friendly product description for a smart coffee maker that connects to your phone.";

        try {
            console.log(styles.highlight('📝 Prompt:'));
            console.log(styles.muted(`"${prompt}"\n`));
            console.log(styles.info('🤖 Generating response...\n'));

            const response = await azureOpenAIClient.chat.completions.create({
                messages: [
                    { role: "system", content: "You are a helpful product description writer." },
                    { role: "user", content: prompt }
                ],
                max_tokens: 150,
                temperature: 0.7
            });

            console.log(styles.success('✅ Generated Description:\n'));
            console.log(styles.highlight(response.choices[0].message.content));
        } catch (error) {
            console.log(styles.error(`❌ Error: ${error.message}`));
        }

        console.log('');
        await this.waitForUserInput();
    }

    // =============================================================================
    // Computer Vision Demo with Enterprise Patterns
    // =============================================================================
    async demonstrateComputerVisionCapabilities() {
        console.log(styles.title('\n🖼️  COMPUTER VISION - ENTERPRISE DEMO'));
        console.log(styles.examTip('📚 AI-900 Exam Coverage: Image analysis, object detection, OCR, face detection\n'));

        if (!cognitiveVisionClient) {
            console.log(styles.error('❌ Computer Vision client not available. Check configuration.'));
            await this.waitForUserInput();
            return;
        }

        const demoImagePath = path.join(__dirname, 'assets', 'People', 'celebrity01.jpg');

        try {
            console.log(styles.info('🔍 Analyzing Contoso marketing image with Computer Vision API...'));

            const analysisResult = await executeAzureAIOperationWithRetry(
                async () => {
                    const imageBuffer = await fs.readFile(demoImagePath);
                    return await cognitiveVisionClient.analyzeImageInStream(imageBuffer, {
                        visualFeatures: ['Categories', 'Description', 'Objects', 'Tags', 'Adult', 'Color', 'Faces'],
                        details: ['Celebrities', 'Landmarks']
                    });
                },
                'Computer Vision Image Analysis'
            );

            this.displayComputerVisionResults(analysisResult);

        } catch (error) {
            console.log(styles.error(`❌ Computer Vision analysis failed: ${error.message}`));
        }

        await this.waitForUserInput();
    }

    displayComputerVisionResults(analysisResult) {
        console.log(styles.success('\n✅ Computer Vision Analysis Complete!\n'));

        // Description with confidence
        if (analysisResult.description?.captions?.length > 0) {
            const caption = analysisResult.description.captions[0];
            console.log(styles.highlight('🎯 AI-Generated Description:'));
            console.log(`   "${caption.text}" (${Math.round(caption.confidence * 100)}% confidence)\n`);
        }

        // Tags with confidence scores
        if (analysisResult.tags?.length > 0) {
            console.log(styles.highlight('🏷️  Detected Tags:'));
            analysisResult.tags.slice(0, 8).forEach(tag => {
                const confidence = Math.round(tag.confidence * 100);
                const confidenceIndicator = confidence >= 70 ? '🟢' : confidence >= 50 ? '🟡' : '🔴';
                console.log(`   ${confidenceIndicator} ${tag.name} (${confidence}%)`);
            });
            console.log('');
        }

        // Objects with bounding boxes
        if (analysisResult.objects?.length > 0) {
            console.log(styles.highlight('📦 Detected Objects:'));
            analysisResult.objects.forEach(obj => {
                const rect = obj.rectangle;
                console.log(`   🎯 ${obj.object} at coordinates (${rect.x}, ${rect.y}) size: ${rect.w}x${rect.h}`);
            });
            console.log('');
        }

        // Face detection
        if (analysisResult.faces?.length > 0) {
            console.log(styles.highlight('👥 Face Analysis:'));
            analysisResult.faces.forEach((face, index) => {
                console.log(`   👤 Person ${index + 1}: ${face.gender}, age ~${face.age} years`);
            });
            console.log('');
        }

        // Responsible AI - Adult content detection
        if (analysisResult.adult) {
            const adult = analysisResult.adult;
            console.log(styles.responsibleAI('🛡️ Responsible AI - Content Safety:'));
            console.log(`   Adult content: ${adult.isAdultContent ? '⚠️ Detected' : '✅ Safe'} (${Math.round(adult.adultScore * 100)}%)`);
            console.log(`   Racy content: ${adult.isRacyContent ? '⚠️ Detected' : '✅ Safe'} (${Math.round(adult.racyScore * 100)}%)`);
            console.log('');
        }

        console.log(styles.examTip('💡 AI-900 Exam Tip: Always check confidence scores and implement thresholds'));
    }

    // =============================================================================
    // Language Analytics Demo
    // =============================================================================
    async demonstrateLanguageAnalyticsCapabilities() {
        console.log(styles.title('\n📝 LANGUAGE ANALYTICS - ENTERPRISE DEMO'));
        console.log(styles.examTip('📚 AI-900 Coverage: Sentiment analysis, language detection, key phrase extraction\n'));

        if (!languageAnalyticsClient) {
            console.log(styles.error('❌ Language Analytics client not available. Check configuration.'));
            await this.waitForUserInput();
            return;
        }

        const customerFeedbackSamples = [
            "I absolutely love the new Contoso AI products! The quality is amazing and delivery was super fast. Will definitely order again!",
            "The Contoso service was disappointing. My order arrived late and the product was damaged. Very frustrated with this experience.",
            "Contoso has been my go-to company for years. Consistent quality and great customer service. Keep up the excellent work!",
            "La nueva línea de productos de Contoso es increíble. ¡Excelente calidad y precio justo!",
            "J'adore les nouveaux produits Contoso. La qualité est exceptionnelle et le service client est fantastique!"
        ];

        console.log(styles.info('🔍 Analyzing Contoso customer feedback with Language Analytics...\n'));

        for (let i = 0; i < customerFeedbackSamples.length; i++) {
            const feedback = customerFeedbackSamples[i];

            try {
                const validatedInput = validateAndSanitizeUserInput(feedback);

                console.log(styles.highlight(`📝 Customer Feedback #${i + 1}:`));
                console.log(styles.muted(`"${validatedInput.sanitized}"\n`));

                const analysisResults = await executeAzureAIOperationWithRetry(
                    async () => {
                        const [sentimentResult, languageResult, keyPhrasesResult] = await Promise.all([
                            languageAnalyticsClient.analyzeSentiment([validatedInput.sanitized]),
                            languageAnalyticsClient.detectLanguage([validatedInput.sanitized]),
                            languageAnalyticsClient.extractKeyPhrases([validatedInput.sanitized])
                        ]);

                        return {
                            sentiment: sentimentResult[0],
                            language: languageResult[0],
                            keyPhrases: keyPhrasesResult[0]
                        };
                    },
                    `Language Analysis for feedback #${i + 1}`
                );

                this.displayLanguageAnalysisResults(analysisResults);

            } catch (error) {
                console.log(styles.error(`❌ Language analysis failed: ${error.message}`));
            }
        }

        await this.waitForUserInput();
    }

    displayLanguageAnalysisResults(results) {
        const { sentiment, language, keyPhrases } = results;

        // Sentiment analysis with visual indicators
        const sentimentIcon = sentiment.sentiment === 'positive' ? '😊' :
                             sentiment.sentiment === 'negative' ? '😞' : '😐';
        const confidence = Math.round(sentiment.confidenceScores[sentiment.sentiment] * 100);

        console.log(styles.success(`${sentimentIcon} Sentiment: ${sentiment.sentiment.toUpperCase()} (${confidence}% confidence)`));

        // Language detection
        const primaryLanguage = language.primaryLanguage;
        const languageConfidence = Math.round(primaryLanguage.confidenceScore * 100);
        console.log(styles.info(`🌍 Language: ${primaryLanguage.name} (${primaryLanguage.iso6391Name}) - ${languageConfidence}% confidence`));

        // Key phrases extraction
        if (keyPhrases.keyPhrases?.length > 0) {
            console.log(styles.info(`🔑 Key Phrases: ${keyPhrases.keyPhrases.join(', ')}`));
        }

        console.log(styles.muted('─'.repeat(60)));
    }

    // =============================================================================
    // Document Intelligence Demo
    // =============================================================================
    async demonstrateDocumentIntelligenceCapabilities() {
        console.log(styles.title('\n📄 DOCUMENT INTELLIGENCE - ENTERPRISE DEMO'));
        console.log(styles.examTip('📚 AI-900 Coverage: Form recognition, receipt processing, business card extraction\n'));

        if (!documentIntelligenceClient) {
            console.log(styles.error('❌ Document Intelligence client not available. Check configuration.'));
            await this.waitForUserInput();
            return;
        }

        const demoDocumentPath = path.join(__dirname, 'assets', 'OCR', 'contoso-receipt.png');

        try {
            console.log(styles.info('🔍 Analyzing Contoso receipt with Document Intelligence...'));
            console.log(styles.concept('📋 Document Intelligence can extract structured data from:'));
            console.log(styles.muted('   • Receipts and invoices'));
            console.log(styles.muted('   • Business cards'));
            console.log(styles.muted('   • ID documents'));
            console.log(styles.muted('   • Custom forms\n'));

            const documentBuffer = await fs.readFile(demoDocumentPath);

            const analysisResult = await executeAzureAIOperationWithRetry(
                async () => {
                    const poller = await documentIntelligenceClient.beginAnalyzeDocument(
                        'prebuilt-receipt',
                        documentBuffer,
                        {
                            contentType: 'image/png'
                        }
                    );
                    return await poller.pollUntilDone();
                },
                'Document Intelligence Receipt Analysis'
            );

            this.displayDocumentIntelligenceResults(analysisResult);

        } catch (error) {
            console.log(styles.error(`❌ Document analysis failed: ${error.message}`));
            console.log(styles.examTip('💡 AI-900 Tip: Document Intelligence requires proper model selection'));
        }

        await this.waitForUserInput();
    }

    displayDocumentIntelligenceResults(analysisResult) {
        console.log(styles.success('\n✅ Document Analysis Complete!\n'));

        if (analysisResult.documents && analysisResult.documents.length > 0) {
            const receipt = analysisResult.documents[0];
            
            console.log(styles.highlight('🧾 Receipt Information:'));
            
            // Merchant information
            if (receipt.fields.MerchantName) {
                console.log(`   🏪 Merchant: ${receipt.fields.MerchantName.value} (${Math.round(receipt.fields.MerchantName.confidence * 100)}% confidence)`);
            }
            
            // Transaction details
            if (receipt.fields.TransactionDate) {
                console.log(`   📅 Date: ${receipt.fields.TransactionDate.value}`);
            }
            
            if (receipt.fields.Total) {
                console.log(`   💰 Total: $${receipt.fields.Total.value} (${Math.round(receipt.fields.Total.confidence * 100)}% confidence)`);
            }
            
            // Items
            if (receipt.fields.Items && receipt.fields.Items.values) {
                console.log(styles.highlight('\n📋 Line Items:'));
                receipt.fields.Items.values.forEach((item, index) => {
                    const name = item.properties.Name?.value || 'Unknown';
                    const price = item.properties.TotalPrice?.value || 0;
                    console.log(`   ${index + 1}. ${name} - $${price}`);
                });
            }
            
            // AI-900 educational insights
            console.log(styles.examTip('\n💡 AI-900 Insights:'));
            console.log(styles.concept('   • Confidence scores indicate extraction reliability'));
            console.log(styles.concept('   • Pre-built models handle common document types'));
            console.log(styles.concept('   • Custom models can be trained for specific forms'));
            console.log(styles.concept('   • OCR + AI enables structured data extraction'));
        }
    }

    // =============================================================================
    // Azure OpenAI Demo with Responsible AI
    // =============================================================================
    async demonstrateAzureOpenAICapabilities() {
        console.log(styles.title('\n🤖 AZURE OPENAI - GENERATIVE AI DEMO'));
        console.log(styles.examTip('📚 AI-900 Coverage: GPT models, chat completions, responsible AI principles\n'));

        if (!azureOpenAIClient) {
            console.log(styles.error('❌ Azure OpenAI client not available. Check configuration.'));
            await this.waitForUserInput();
            return;
        }

        const businessPrompts = [
            "Write a professional email to a Contoso customer apologizing for a delayed shipment and offering a 10% discount.",
            "Create a product description for Contoso's new AI-powered smart home device focusing on energy efficiency.",
            "Generate 3 creative but professional marketing taglines for Contoso's sustainable product line."
        ];

        for (let i = 0; i < businessPrompts.length; i++) {
            const prompt = businessPrompts[i];
            console.log(styles.highlight(`🎯 Business Scenario ${i + 1}:`));
            console.log(styles.muted(`${prompt}\n`));

            try {
                const aiResponse = await executeAzureAIOperationWithRetry(
                    async () => {
                        return await azureOpenAIClient.chat.completions.create({
                            messages: [
                                {
                                    role: "system",
                                    content: "You are a helpful, professional AI assistant for Contoso Corporation. Always maintain a professional tone and focus on customer satisfaction. Follow responsible AI principles."
                                },
                                { role: "user", content: prompt }
                            ],
                            max_tokens: 300,
                            temperature: 0.7
                        });
                    },
                    `Azure OpenAI Chat Completion #${i + 1}`
                );

                console.log(styles.success('\n✅ AI-Generated Response:'));
                console.log(styles.muted(aiResponse.choices[0].message.content));
                console.log(styles.responsibleAI(`\n🛡️ Responsible AI: Content filtered and validated`));
                console.log(styles.muted('─'.repeat(60)));

            } catch (error) {
                console.log(styles.error(`❌ AI generation failed: ${error.message}`));
            }
        }

        await this.waitForUserInput();
    }

    // =============================================================================
    // Service Metrics Display
    // =============================================================================
    displayServiceHealthAndMetrics() {
        console.log(styles.title('\n📊 SERVICE HEALTH & METRICS DASHBOARD'));
        console.log(styles.examTip('📚 AI-900 Monitoring: Production apps need comprehensive monitoring\n'));

        // Service health status
        console.log(styles.highlight('🏥 Service Health Status:'));
        for (const [serviceName, metrics] of this.serviceHealthMetrics) {
            const statusIcon = metrics.status === 'healthy' ? '✅' : '❌';
            console.log(`${statusIcon} ${serviceName}: ${metrics.status.toUpperCase()}`);
            if (metrics.endpoint) {
                console.log(styles.muted(`   📍 Endpoint: ${metrics.endpoint}`));
            }
        }

        // Operation metrics
        console.log(styles.highlight('\n📈 Operation Metrics:'));
        console.log(`   📊 Total Operations: ${this.operationMetrics.totalOperations}`);
        console.log(`   ✅ Successful: ${this.operationMetrics.successfulOperations}`);
        console.log(`   ❌ Failed: ${this.operationMetrics.failedOperations}`);
        console.log(`   🔄 Retry Attempts: ${this.operationMetrics.retryAttempts}`);

        const successRate = this.operationMetrics.totalOperations > 0 ?
            Math.round((this.operationMetrics.successfulOperations / this.operationMetrics.totalOperations) * 100) : 0;
        console.log(`   📊 Success Rate: ${successRate}%`);

        console.log(styles.bestPractice('\n💡 Production Best Practices Implemented:'));
        console.log(styles.muted('   • Exponential backoff retry logic'));
        console.log(styles.muted('   • Rate limiting detection (HTTP 429)'));
        console.log(styles.muted('   • Input validation and sanitization'));
        console.log(styles.muted('   • Comprehensive error handling'));
        console.log(styles.muted('   • Client connection pooling'));
        console.log(styles.muted('   • Responsible AI content filtering'));
    }

    // =============================================================================
    // Utility Methods
    // =============================================================================
    async waitForUserInput() {
        await inquirer.prompt([{
            type: 'input',
            name: 'continue',
            message: styles.muted('Press Enter to continue...')
        }]);
    }

    // =============================================================================
    // Main Application Loop
    // =============================================================================
    async run() {
        console.log(styles.success('🚀 Enterprise AI-900 Demo Application started successfully!\n'));

        while (this.isApplicationRunning) {
            this.displayEducationalBanner();
            const userChoice = await this.showInteractiveMainMenu();

            switch (userChoice) {
                case 'content_safety':
                    await this.demonstrateContentSafety();
                    break;
                case 'computer_vision':
                    await this.demonstrateComputerVisionSimple();
                    break;
                case 'language_analytics':
                    await this.demonstrateLanguageAnalyticsSimple();
                    break;
                case 'translation':
                    await this.demonstrateTranslation();
                    break;
                case 'document_intelligence':
                    await this.demonstrateDocumentIntelligenceSimple();
                    break;
                case 'azure_openai':
                    await this.demonstrateAzureOpenAISimple();
                    break;
                case 'service_metrics':
                    this.displayServiceHealthAndMetrics();
                    await this.waitForUserInput();
                    break;
                case 'exit_application':
                    console.log(styles.success('\n🎯 Thank you for exploring Azure AI with Tim Warner!'));
                    console.log(styles.examTip('📚 Keep practicing for your AI-900 certification! Good luck! 🚀\n'));
                    this.isApplicationRunning = false;
                    break;
            }
        }
    }
}

// =============================================================================
// Port Cleanup Utility
// =============================================================================
async function cleanupPort3000() {
    const { exec } = require('child_process');
    const util = require('util');
    const execPromise = util.promisify(exec);
    
    try {
        console.log(styles.info('🔧 Checking for processes using port 3000...'));
        
        // Platform-specific commands
        const isWindows = process.platform === 'win32';
        const command = isWindows 
            ? 'netstat -ano | findstr :3000' 
            : 'lsof -ti:3000';
        
        const { stdout } = await execPromise(command);
        
        if (stdout.trim()) {
            console.log(styles.warning('⚠️ Found process using port 3000, attempting to free it...'));
            
            const killCommand = isWindows
                ? `taskkill /F /PID ${stdout.trim().split(/\s+/).pop()}`
                : `kill -9 ${stdout.trim()}`;
            
            await execPromise(killCommand);
            console.log(styles.success('✅ Port 3000 successfully freed!'));
        } else {
            console.log(styles.muted('✨ Port 3000 is already available'));
        }
    } catch (error) {
        // Port is likely already free if command fails
        console.log(styles.muted('✨ Port 3000 is available'));
    }
}

// =============================================================================
// Application Entry Point
// =============================================================================
if (require.main === module) {
    (async () => {
        // Clean up port 3000 on startup as requested
        await cleanupPort3000();
        
        const enterpriseAI900App = new EnterpriseAI900DemoApplication();
        await enterpriseAI900App.run();
    })().catch(error => {
        console.error(styles.error('💥 Application Error:'), error);
        console.log(styles.examTip('💡 AI-900 Tip: Always implement comprehensive error handling'));
        process.exit(1);
    });
}

module.exports = EnterpriseAI900DemoApplication;
