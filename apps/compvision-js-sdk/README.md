# Computer Vision JS SDK Quickstart

A minimal Node.js sample using Azure Computer Vision.

## Prerequisites
- Node.js 14+
- Azure Cognitive Services (Computer Vision) resource

## Setup
```bash
cd apps/compvision-js-sdk
cp .env.example .env
# Edit .env with your endpoint/key
npm install
node ComputerVisionQuickstart.js
```

Environment variables supported:
- `COMPUTER_VISION_ENDPOINT` and `COMPUTER_VISION_SUBSCRIPTION_KEY`
- Or generic: `COGNITIVE_ENDPOINT` and `COGNITIVE_KEY`

The script downloads sample images on demand and prints analysis to the console.
