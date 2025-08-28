# Analyze Image (Node + REST) Quickstart

Simple REST call to Computer Vision Analyze API using Node.js.

## Prerequisites
- Node.js 14+
- Azure Cognitive Services endpoint and key

## Setup
```bash
cd apps/analyze-image-node-rest
cp .env.example .env
# Edit .env with COGNITIVE_ENDPOINT and COGNITIVE_KEY
# Install minimal deps locally
npm init -y && npm install request dotenv
node analyze-image.js
```

The script reads endpoint/key from env, posts a sample image URL, and prints the JSON response.
