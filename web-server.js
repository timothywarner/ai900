#!/usr/bin/env node
'use strict';

// 🌐 AI-900 Web Interface Server
// Contoso Corporation AI Portal
// =============================

require('dotenv').config();
const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs').promises;
const morgan = require('morgan');

const app = express();
const PORT = process.env.PORT || 3000;

// 📁 Configure file upload
const upload = multer({
    dest: 'uploads/',
    limits: { fileSize: 10 * 1024 * 1024 } // 10MB limit
});

// 🎨 Middleware
app.use(morgan('dev'));
app.use(express.json({ limit: '10mb' }));
app.use(express.static('public'));
app.use('/assets', express.static('assets'));

// 🏠 Home route - Contoso AI Portal
app.get('/', (req, res) => {
    res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoso AI Portal - Azure AI-900 Demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --contoso-blue: #0078d4;
            --contoso-dark: #106ebe;
            --contoso-light: #e1f5fe;
        }

        body {
            background: linear-gradient(135deg, var(--contoso-blue) 0%, var(--contoso-dark) 100%);
            min-height: 100vh;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .hero-section {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            margin: 2rem 0;
            padding: 3rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        .service-card {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
            border: 2px solid transparent;
        }

        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
            border-color: var(--contoso-blue);
        }

        .service-icon {
            font-size: 3rem;
            color: var(--contoso-blue);
            margin-bottom: 1rem;
        }

        .contoso-logo {
            color: var(--contoso-blue);
            font-weight: bold;
            font-size: 2.5rem;
        }

        .demo-section {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            display: none;
        }

        .demo-section.active {
            display: block;
            animation: fadeIn 0.5s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .btn-contoso {
            background: var(--contoso-blue);
            border: none;
            padding: 0.75rem 2rem;
            border-radius: 25px;
            color: white;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .btn-contoso:hover {
            background: var(--contoso-dark);
            transform: translateY(-2px);
            color: white;
        }

        .result-box {
            background: var(--contoso-light);
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 4px solid var(--contoso-blue);
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="hero-section text-center">
            <h1 class="contoso-logo">
                <i class="fas fa-brain"></i> Contoso AI Portal
            </h1>
            <p class="lead text-muted">Innovation Through Intelligence</p>
            <p class="text-muted">Azure AI-900 Demonstration Suite by Tim Warner</p>
        </div>

        <!-- Service Cards -->
        <div class="row" id="serviceCards">
            <div class="col-md-4">
                <div class="service-card text-center" onclick="showDemo('vision')">
                    <div class="service-icon">
                        <i class="fas fa-eye"></i>
                    </div>
                    <h4>Computer Vision</h4>
                    <p class="text-muted">Analyze images, detect objects, extract text</p>
                </div>
            </div>

            <div class="col-md-4">
                <div class="service-card text-center" onclick="showDemo('language')">
                    <div class="service-icon">
                        <i class="fas fa-comments"></i>
                    </div>
                    <h4>Language Service</h4>
                    <p class="text-muted">Sentiment analysis, language detection, key phrases</p>
                </div>
            </div>

            <div class="col-md-4">
                <div class="service-card text-center" onclick="showDemo('document')">
                    <div class="service-icon">
                        <i class="fas fa-file-alt"></i>
                    </div>
                    <h4>Document Intelligence</h4>
                    <p class="text-muted">Extract data from receipts, invoices, forms</p>
                </div>
            </div>

            <div class="col-md-4">
                <div class="service-card text-center" onclick="showDemo('speech')">
                    <div class="service-icon">
                        <i class="fas fa-microphone"></i>
                    </div>
                    <h4>Speech Services</h4>
                    <p class="text-muted">Speech-to-text, text-to-speech, translation</p>
                </div>
            </div>

            <div class="col-md-4">
                <div class="service-card text-center" onclick="showDemo('openai')">
                    <div class="service-icon">
                        <i class="fas fa-robot"></i>
                    </div>
                    <h4>Azure OpenAI</h4>
                    <p class="text-muted">GPT models, chat completions, generative AI</p>
                </div>
            </div>

            <div class="col-md-4">
                <div class="service-card text-center" onclick="showDemo('search')">
                    <div class="service-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <h4>Cognitive Search</h4>
                    <p class="text-muted">AI-powered search and knowledge mining</p>
                </div>
            </div>
        </div>

        <!-- Computer Vision Demo -->
        <div id="visionDemo" class="demo-section">
            <h3><i class="fas fa-eye text-primary"></i> Computer Vision Demo</h3>
            <p>Upload an image to analyze with Contoso's AI vision capabilities.</p>

            <div class="mb-3">
                <input type="file" class="form-control" id="visionFile" accept="image/*">
            </div>
            <button class="btn btn-contoso" onclick="analyzeImage()">
                <i class="fas fa-search"></i> Analyze Image
            </button>
            <div id="visionResults" class="result-box" style="display: none;"></div>
        </div>

        <!-- Language Service Demo -->
        <div id="languageDemo" class="demo-section">
            <h3><i class="fas fa-comments text-success"></i> Language Service Demo</h3>
            <p>Analyze text for sentiment, language, and key phrases.</p>

            <div class="mb-3">
                <textarea class="form-control" id="languageText" rows="4"
                    placeholder="Enter customer feedback about Contoso products..."></textarea>
            </div>
            <button class="btn btn-contoso" onclick="analyzeText()">
                <i class="fas fa-brain"></i> Analyze Text
            </button>
            <div id="languageResults" class="result-box" style="display: none;"></div>
        </div>

        <!-- Document Intelligence Demo -->
        <div id="documentDemo" class="demo-section">
            <h3><i class="fas fa-file-alt text-warning"></i> Document Intelligence Demo</h3>
            <p>Upload a receipt, invoice, or business card for data extraction.</p>

            <div class="mb-3">
                <input type="file" class="form-control" id="documentFile" accept=".pdf,.jpg,.jpeg,.png">
            </div>
            <button class="btn btn-contoso" onclick="analyzeDocument()">
                <i class="fas fa-extract"></i> Extract Data
            </button>
            <div id="documentResults" class="result-box" style="display: none;"></div>
        </div>

        <!-- Speech Services Demo -->
        <div id="speechDemo" class="demo-section">
            <h3><i class="fas fa-microphone text-info"></i> Speech Services Demo</h3>
            <p>Convert speech to text and text to speech.</p>

            <div class="mb-3">
                <textarea class="form-control" id="speechText" rows="3"
                    placeholder="Enter text to convert to speech..."></textarea>
            </div>
            <button class="btn btn-contoso" onclick="textToSpeech()">
                <i class="fas fa-volume-up"></i> Text to Speech
            </button>
            <div id="speechResults" class="result-box" style="display: none;"></div>
        </div>

        <!-- Azure OpenAI Demo -->
        <div id="openaiDemo" class="demo-section">
            <h3><i class="fas fa-robot text-danger"></i> Azure OpenAI Demo</h3>
            <p>Chat with Contoso's AI assistant powered by GPT.</p>

            <div class="mb-3">
                <textarea class="form-control" id="openaiPrompt" rows="3"
                    placeholder="Ask the Contoso AI assistant anything..."></textarea>
            </div>
            <button class="btn btn-contoso" onclick="chatWithAI()">
                <i class="fas fa-paper-plane"></i> Send Message
            </button>
            <div id="openaiResults" class="result-box" style="display: none;"></div>
        </div>

        <!-- Search Demo -->
        <div id="searchDemo" class="demo-section">
            <h3><i class="fas fa-search text-secondary"></i> Cognitive Search Demo</h3>
            <p>Search through Contoso's knowledge base with AI-powered search.</p>

            <div class="mb-3">
                <input type="text" class="form-control" id="searchQuery"
                    placeholder="Search for products, documents, or information...">
            </div>
            <button class="btn btn-contoso" onclick="performSearch()">
                <i class="fas fa-search"></i> Search
            </button>
            <div id="searchResults" class="result-box" style="display: none;"></div>
        </div>

        <!-- Back to Services Button -->
        <div class="text-center mt-4" style="display: none;" id="backButton">
            <button class="btn btn-outline-primary" onclick="showServices()">
                <i class="fas fa-arrow-left"></i> Back to Services
            </button>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        function showDemo(service) {
            // Hide service cards
            document.getElementById('serviceCards').style.display = 'none';

            // Hide all demo sections
            const demos = document.querySelectorAll('.demo-section');
            demos.forEach(demo => demo.classList.remove('active'));

            // Show selected demo
            document.getElementById(service + 'Demo').classList.add('active');

            // Show back button
            document.getElementById('backButton').style.display = 'block';
        }

        function showServices() {
            // Show service cards
            document.getElementById('serviceCards').style.display = 'flex';

            // Hide all demo sections
            const demos = document.querySelectorAll('.demo-section');
            demos.forEach(demo => demo.classList.remove('active'));

            // Hide back button
            document.getElementById('backButton').style.display = 'none';
        }

        async function analyzeImage() {
            const fileInput = document.getElementById('visionFile');
            const resultsDiv = document.getElementById('visionResults');

            if (!fileInput.files[0]) {
                alert('Please select an image file first.');
                return;
            }

            const formData = new FormData();
            formData.append('image', fileInput.files[0]);

            resultsDiv.style.display = 'block';
            resultsDiv.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing image...';

            try {
                const response = await fetch('/api/vision/analyze', {
                    method: 'POST',
                    body: formData
                });

                const result = await response.json();

                if (result.success) {
                    resultsDiv.innerHTML = \`
                        <h5>📊 Analysis Results</h5>
                        <p><strong>Description:</strong> \${result.description}</p>
                        <p><strong>Tags:</strong> \${result.tags}</p>
                        <p><strong>Objects:</strong> \${result.objects}</p>
                    \`;
                } else {
                    resultsDiv.innerHTML = '<div class="alert alert-danger">Error: ' + result.error + '</div>';
                }
            } catch (error) {
                resultsDiv.innerHTML = '<div class="alert alert-danger">Error analyzing image: ' + error.message + '</div>';
            }
        }

        async function analyzeText() {
            const text = document.getElementById('languageText').value;
            const resultsDiv = document.getElementById('languageResults');

            if (!text.trim()) {
                alert('Please enter some text to analyze.');
                return;
            }

            resultsDiv.style.display = 'block';
            resultsDiv.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing text...';

            try {
                const response = await fetch('/api/language/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text: text })
                });

                const result = await response.json();

                if (result.success) {
                    const sentimentIcon = result.sentiment === 'positive' ? '😊' :
                                        result.sentiment === 'negative' ? '😞' : '😐';

                    resultsDiv.innerHTML = \`
                        <h5>📝 Text Analysis Results</h5>
                        <p><strong>Sentiment:</strong> \${sentimentIcon} \${result.sentiment} (\${result.confidence}%)</p>
                        <p><strong>Language:</strong> 🌍 \${result.language}</p>
                        <p><strong>Key Phrases:</strong> 🔑 \${result.keyPhrases}</p>
                    \`;
                } else {
                    resultsDiv.innerHTML = '<div class="alert alert-danger">Error: ' + result.error + '</div>';
                }
            } catch (error) {
                resultsDiv.innerHTML = '<div class="alert alert-danger">Error analyzing text: ' + error.message + '</div>';
            }
        }

        async function analyzeDocument() {
            const fileInput = document.getElementById('documentFile');
            const resultsDiv = document.getElementById('documentResults');

            if (!fileInput.files[0]) {
                alert('Please select a document file first.');
                return;
            }

            const formData = new FormData();
            formData.append('document', fileInput.files[0]);

            resultsDiv.style.display = 'block';
            resultsDiv.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing document...';

            // Placeholder for document analysis
            setTimeout(() => {
                resultsDiv.innerHTML = \`
                    <h5>📄 Document Analysis Results</h5>
                    <p><strong>Document Type:</strong> Receipt/Invoice</p>
                    <p><strong>Extracted Data:</strong> Text, tables, and key-value pairs extracted</p>
                    <div class="alert alert-info">
                        <i class="fas fa-info-circle"></i>
                        Document Intelligence requires additional setup for full functionality.
                    </div>
                \`;
            }, 2000);
        }

        async function textToSpeech() {
            const text = document.getElementById('speechText').value;
            const resultsDiv = document.getElementById('speechResults');

            if (!text.trim()) {
                alert('Please enter some text to convert to speech.');
                return;
            }

            resultsDiv.style.display = 'block';
            resultsDiv.innerHTML = \`
                <h5>🎤 Speech Synthesis</h5>
                <p><strong>Text:</strong> "\${text}"</p>
                <div class="alert alert-info">
                    <i class="fas fa-info-circle"></i>
                    Speech services require additional browser permissions and setup.
                </div>
            \`;
        }

        async function chatWithAI() {
            const prompt = document.getElementById('openaiPrompt').value;
            const resultsDiv = document.getElementById('openaiResults');

            if (!prompt.trim()) {
                alert('Please enter a message for the AI assistant.');
                return;
            }

            resultsDiv.style.display = 'block';
            resultsDiv.innerHTML = '<i class="fas fa-spinner fa-spin"></i> AI is thinking...';

            try {
                const response = await fetch('/api/openai/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt: prompt })
                });

                const result = await response.json();

                if (result.success) {
                    resultsDiv.innerHTML = \`
                        <h5>🤖 Contoso AI Assistant</h5>
                        <div class="alert alert-light">
                            <strong>You:</strong> \${prompt}
                        </div>
                        <div class="alert alert-primary">
                            <strong>AI:</strong> \${result.response}
                        </div>
                    \`;
                } else {
                    resultsDiv.innerHTML = '<div class="alert alert-danger">Error: ' + result.error + '</div>';
                }
            } catch (error) {
                resultsDiv.innerHTML = '<div class="alert alert-danger">Error communicating with AI: ' + error.message + '</div>';
            }
        }

        async function performSearch() {
            const query = document.getElementById('searchQuery').value;
            const resultsDiv = document.getElementById('searchResults');

            if (!query.trim()) {
                alert('Please enter a search query.');
                return;
            }

            resultsDiv.style.display = 'block';
            resultsDiv.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Searching...';

            // Placeholder search results
            setTimeout(() => {
                resultsDiv.innerHTML = \`
                    <h5>🔍 Search Results for "\${query}"</h5>
                    <div class="list-group">
                        <div class="list-group-item">
                            <h6>Contoso Product Catalog</h6>
                            <p class="mb-1">AI-powered product recommendations and descriptions...</p>
                        </div>
                        <div class="list-group-item">
                            <h6>Customer Service Documentation</h6>
                            <p class="mb-1">Comprehensive guides and troubleshooting information...</p>
                        </div>
                        <div class="list-group-item">
                            <h6>Company Policies</h6>
                            <p class="mb-1">Internal policies and procedures related to your search...</p>
                        </div>
                    </div>
                    <div class="alert alert-info mt-3">
                        <i class="fas fa-info-circle"></i>
                        Cognitive Search requires Azure Search service setup for full functionality.
                    </div>
                \`;
            }, 1500);
        }
    </script>
</body>
</html>
    `);
});

// 🖼️ Computer Vision API endpoint
app.post('/api/vision/analyze', upload.single('image'), async (req, res) => {
    try {
        if (!req.file) {
            return res.json({ success: false, error: 'No image file provided' });
        }

        // Placeholder response - replace with actual Computer Vision API call
        res.json({
            success: true,
            description: 'A Contoso product image showing high quality and innovative design',
            tags: 'product, technology, innovation, quality',
            objects: 'device, packaging, branding elements'
        });

    } catch (error) {
        res.json({ success: false, error: error.message });
    }
});

// 📝 Language Service API endpoint
app.post('/api/language/analyze', async (req, res) => {
    try {
        const { text } = req.body;

        if (!text) {
            return res.json({ success: false, error: 'No text provided' });
        }

        // Simple sentiment analysis placeholder
        const positiveWords = ['good', 'great', 'excellent', 'amazing', 'love', 'fantastic', 'wonderful'];
        const negativeWords = ['bad', 'terrible', 'awful', 'hate', 'disappointed', 'frustrated', 'poor'];

        const words = text.toLowerCase().split(/\s+/);
        const positiveCount = words.filter(word => positiveWords.some(pw => word.includes(pw))).length;
        const negativeCount = words.filter(word => negativeWords.some(nw => word.includes(nw))).length;

        let sentiment = 'neutral';
        let confidence = 50;

        if (positiveCount > negativeCount) {
            sentiment = 'positive';
            confidence = Math.min(90, 60 + (positiveCount * 10));
        } else if (negativeCount > positiveCount) {
            sentiment = 'negative';
            confidence = Math.min(90, 60 + (negativeCount * 10));
        }

        res.json({
            success: true,
            sentiment: sentiment,
            confidence: confidence,
            language: 'English',
            keyPhrases: 'Contoso, products, customer service, quality'
        });

    } catch (error) {
        res.json({ success: false, error: error.message });
    }
});

// 🤖 Azure OpenAI API endpoint
app.post('/api/openai/chat', async (req, res) => {
    try {
        const { prompt } = req.body;

        if (!prompt) {
            return res.json({ success: false, error: 'No prompt provided' });
        }

        // Placeholder AI responses
        const responses = [
            "As Contoso's AI assistant, I'm here to help you with innovative solutions that drive your business forward.",
            "Thank you for reaching out to Contoso! Our AI-powered services are designed to transform your operations.",
            "At Contoso, we believe in the power of intelligent technology to solve complex business challenges.",
            "I'm excited to assist you with Contoso's cutting-edge AI capabilities and services."
        ];

        const randomResponse = responses[Math.floor(Math.random() * responses.length)];

        res.json({
            success: true,
            response: randomResponse
        });

    } catch (error) {
        res.json({ success: false, error: error.message });
    }
});

// 🔧 Health check endpoint
app.get('/health', (req, res) => {
    res.json({
        status: 'healthy',
        service: 'Contoso AI Portal',
        timestamp: new Date().toISOString()
    });
});

// 🚀 Start server only if run directly (not in tests)
if (require.main === module) {
    app.listen(PORT, () => {
        console.log(`
🌐 Contoso AI Portal is running!
📍 URL: http://localhost:${PORT}
🎯 Ready for AI-900 demonstrations
        `);
    });
}

module.exports = app;
