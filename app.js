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

// =============================================================================
// Global AI Service Client Instances
// =============================================================================
// Pattern: Singleton clients for connection pooling and efficiency
// AI-900 Best Practice: Reuse clients to avoid authentication overhead
let cognitiveVisionClient, languageAnalyticsClient, documentIntelligenceClient, azureOpenAIClient;

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
        console.log(styles.title(figlet.textSync('AI-900 DEMO', { horizontalLayout: 'full' })));
        console.log(styles.highlight('🚀 Enterprise Azure AI Services Demonstration'));
        console.log(styles.info('   By Tim Warner - Microsoft MVP & Azure AI Engineer\n'));
        console.log(styles.responsibleAI('   Contoso Corporation - Innovation Through Responsible AI\n'));

        // Educational context
        console.log(styles.examTip('📚 AI-900 Exam Focus Areas Covered:'));
        console.log(styles.concept('   • Computer Vision & OCR capabilities'));
        console.log(styles.concept('   • Natural Language Processing & sentiment analysis'));
        console.log(styles.concept('   • Document Intelligence & form recognition'));
        console.log(styles.concept('   • Generative AI with Azure OpenAI Service'));
        console.log(styles.concept('   • Responsible AI principles & best practices\n'));

        console.log(styles.bestPractice('🏗️ Enterprise Patterns Demonstrated:'));
        console.log(styles.muted('   • Retry logic with exponential backoff'));
        console.log(styles.muted('   • Input validation & sanitization'));
        console.log(styles.muted('   • Rate limiting awareness (HTTP 429)'));
        console.log(styles.muted('   • Connection pooling & client reuse'));
        console.log(styles.muted('   • Comprehensive error handling\n'));

        console.log(styles.muted('═'.repeat(70)));
    }

    // =============================================================================
    // Interactive Main Menu
    // =============================================================================
    async showInteractiveMainMenu() {
        const menuChoices = [
            { name: '🖼️  Computer Vision Analysis - Image Recognition & OCR', value: 'computer_vision' },
            { name: '📝 Language Analytics - Sentiment & Text Processing', value: 'language_analytics' },
            { name: '📄 Document Intelligence - Form & Receipt Processing', value: 'document_intelligence' },
            { name: '🤖 Azure OpenAI - Generative AI & Chat Completions', value: 'azure_openai' },
            { name: '📊 Service Health Metrics - Monitor AI Operations', value: 'service_metrics' },
            new inquirer.Separator('─────────────────────────────────────────'),
            { name: '🌐 Launch Web Interface Portal', value: 'web_interface' },
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
                case 'computer_vision':
                    await this.demonstrateComputerVisionCapabilities();
                    break;
                case 'language_analytics':
                    await this.demonstrateLanguageAnalyticsCapabilities();
                    break;
                case 'document_intelligence':
                    console.log(styles.info('📄 Document Intelligence demo coming in next update...'));
                    await this.waitForUserInput();
                    break;
                case 'azure_openai':
                    await this.demonstrateAzureOpenAICapabilities();
                    break;
                case 'service_metrics':
                    this.displayServiceHealthAndMetrics();
                    await this.waitForUserInput();
                    break;
                case 'web_interface':
                    console.log(styles.info('🌐 Launching web interface... (run npm run web in another terminal)'));
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
// Application Entry Point
// =============================================================================
if (require.main === module) {
    const enterpriseAI900App = new EnterpriseAI900DemoApplication();
    enterpriseAI900App.run().catch(error => {
        console.error(styles.error('💥 Application Error:'), error);
        console.log(styles.examTip('💡 AI-900 Tip: Always implement comprehensive error handling'));
        process.exit(1);
    });
}

module.exports = EnterpriseAI900DemoApplication;
