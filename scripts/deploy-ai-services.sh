#!/usr/bin/env bash
# =============================================================================
# AI-900 Demo Infrastructure - Deploy All Azure AI Services
# =============================================================================
# Deploys singleton instances of every Azure AI service needed for the
# 5-hour AI-900 certification prep course.
#
# Region:         East US (DALL-E 3 + full REST API support)
# Resource Group:  AI900-Feb2026
# Estimated Cost: ~$2-5 for a 3-day workshop (all pay-per-use)
#
# Prerequisites:
#   - Azure CLI installed and logged in (az login)
#   - Subscription approved for Azure OpenAI access
#   - Bash shell (Git Bash on Windows, or WSL)
#
# Usage:
#   chmod +x scripts/deploy-ai-services.sh
#   ./scripts/deploy-ai-services.sh
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
RESOURCE_GROUP="AI900-Feb2026"
LOCATION="eastus"
UNIQUE_SUFFIX=$(az group show --name "$RESOURCE_GROUP" --query "id" -o tsv 2>/dev/null | md5sum | cut -c1-6 || echo "feb26a")

# Resource names (descriptive, training-friendly)
AI_SERVICES_NAME="ai900-multiservice-${UNIQUE_SUFFIX}"
OPENAI_NAME="ai900-openai-${UNIQUE_SUFFIX}"
OPENAI_DALLE_NAME="ai900-openai-dalle-${UNIQUE_SUFFIX}"
DOCINTELL_NAME="ai900-docintell-${UNIQUE_SUFFIX}"
CV_TRAINING_NAME="ai900-cvtrain-${UNIQUE_SUFFIX}"
CV_PREDICTION_NAME="ai900-cvpredict-${UNIQUE_SUFFIX}"

TAGS="purpose=training owner=trainer auto-delete=true course=AI-900 delivery=Feb2026"

echo "==========================================="
echo " AI-900 Demo Infrastructure Deployment"
echo "==========================================="
echo "Resource Group: $RESOURCE_GROUP"
echo "Location:       $LOCATION"
echo "Suffix:         $UNIQUE_SUFFIX"
echo ""

# ---------------------------------------------------------------------------
# Step 0: Ensure resource group exists
# ---------------------------------------------------------------------------
echo "[0/7] Ensuring resource group exists..."
az group create \
  --name "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --tags $TAGS \
  --output none

# ---------------------------------------------------------------------------
# Step 1: Azure AI Services (multi-service account)
# Kind: CognitiveServices  |  SKU: S0 (pay-per-call, no base cost)
# Provides: Vision, Language, Speech, Face, Content Safety
# Used by: Hours 1, 3, 4
# ---------------------------------------------------------------------------
echo "[1/7] Deploying Azure AI Services (multi-service)..."
az cognitiveservices account create \
  --name "$AI_SERVICES_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --kind "CognitiveServices" \
  --sku "S0" \
  --custom-domain "$AI_SERVICES_NAME" \
  --tags $TAGS \
  --yes \
  --output none

echo "      Endpoint: $(az cognitiveservices account show --name "$AI_SERVICES_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)"

# ---------------------------------------------------------------------------
# Step 2: Azure OpenAI (for GPT-4o)
# Kind: OpenAI  |  SKU: S0  |  Pay-per-token
# Used by: Hour 5 (chat completions, prompt engineering)
# ---------------------------------------------------------------------------
echo "[2/7] Deploying Azure OpenAI (GPT-4o)..."
az cognitiveservices account create \
  --name "$OPENAI_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --kind "OpenAI" \
  --sku "S0" \
  --custom-domain "$OPENAI_NAME" \
  --tags $TAGS \
  --yes \
  --output none

echo "      Endpoint: $(az cognitiveservices account show --name "$OPENAI_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)"

# Deploy GPT-4o model
echo "      Deploying GPT-4o model..."
az cognitiveservices account deployment create \
  --name "$OPENAI_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --deployment-name "gpt-4o" \
  --model-name "gpt-4o" \
  --model-version "2024-11-20" \
  --model-format "OpenAI" \
  --sku-capacity 10 \
  --sku-name "GlobalStandard" \
  --output none

echo "      Model deployed: gpt-4o"

# ---------------------------------------------------------------------------
# Step 3: Azure OpenAI (for DALL-E 3)
# Separate resource to avoid quota conflicts during live demos
# Kind: OpenAI  |  SKU: S0  |  Pay-per-image
# Used by: Hour 5 (image generation)
# ---------------------------------------------------------------------------
echo "[3/7] Deploying Azure OpenAI (DALL-E 3)..."
az cognitiveservices account create \
  --name "$OPENAI_DALLE_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --kind "OpenAI" \
  --sku "S0" \
  --custom-domain "$OPENAI_DALLE_NAME" \
  --tags $TAGS \
  --yes \
  --output none

echo "      Endpoint: $(az cognitiveservices account show --name "$OPENAI_DALLE_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)"

# Deploy DALL-E 3 model
echo "      Deploying DALL-E 3 model..."
az cognitiveservices account deployment create \
  --name "$OPENAI_DALLE_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --deployment-name "dall-e-3" \
  --model-name "dall-e-3" \
  --model-version "3.0" \
  --model-format "OpenAI" \
  --sku-capacity 1 \
  --sku-name "Standard" \
  --output none

echo "      Model deployed: dall-e-3"

# ---------------------------------------------------------------------------
# Step 4: Azure AI Document Intelligence
# Kind: FormRecognizer  |  SKU: S0  |  Pay-per-page
# Used by: Hour 3 (invoice/receipt analysis)
# ---------------------------------------------------------------------------
echo "[4/7] Deploying Document Intelligence..."
az cognitiveservices account create \
  --name "$DOCINTELL_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --kind "FormRecognizer" \
  --sku "S0" \
  --custom-domain "$DOCINTELL_NAME" \
  --tags $TAGS \
  --yes \
  --output none

echo "      Endpoint: $(az cognitiveservices account show --name "$DOCINTELL_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)"

# ---------------------------------------------------------------------------
# Step 5: Custom Vision - Training
# Kind: CustomVision.Training  |  SKU: S0
# Used by: Hour 3 (image classification training)
# ---------------------------------------------------------------------------
echo "[5/7] Deploying Custom Vision (Training)..."
az cognitiveservices account create \
  --name "$CV_TRAINING_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --kind "CustomVision.Training" \
  --sku "S0" \
  --custom-domain "$CV_TRAINING_NAME" \
  --tags $TAGS \
  --yes \
  --output none

echo "      Endpoint: $(az cognitiveservices account show --name "$CV_TRAINING_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)"

# ---------------------------------------------------------------------------
# Step 6: Custom Vision - Prediction
# Kind: CustomVision.Prediction  |  SKU: S0
# Used by: Hour 3 (image classification inference)
# ---------------------------------------------------------------------------
echo "[6/7] Deploying Custom Vision (Prediction)..."
az cognitiveservices account create \
  --name "$CV_PREDICTION_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --kind "CustomVision.Prediction" \
  --sku "S0" \
  --custom-domain "$CV_PREDICTION_NAME" \
  --tags $TAGS \
  --yes \
  --output none

echo "      Endpoint: $(az cognitiveservices account show --name "$CV_PREDICTION_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)"

# ---------------------------------------------------------------------------
# Step 7: Print .env values
# ---------------------------------------------------------------------------
echo ""
echo "==========================================="
echo " Deployment Complete! Retrieving keys..."
echo "==========================================="
echo ""

AI_ENDPOINT=$(az cognitiveservices account show --name "$AI_SERVICES_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)
AI_KEY=$(az cognitiveservices account keys list --name "$AI_SERVICES_NAME" --resource-group "$RESOURCE_GROUP" --query "key1" -o tsv)

OPENAI_ENDPOINT=$(az cognitiveservices account show --name "$OPENAI_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)
OPENAI_KEY=$(az cognitiveservices account keys list --name "$OPENAI_NAME" --resource-group "$RESOURCE_GROUP" --query "key1" -o tsv)

DALLE_ENDPOINT=$(az cognitiveservices account show --name "$OPENAI_DALLE_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)
DALLE_KEY=$(az cognitiveservices account keys list --name "$OPENAI_DALLE_NAME" --resource-group "$RESOURCE_GROUP" --query "key1" -o tsv)

DOCINTELL_ENDPOINT=$(az cognitiveservices account show --name "$DOCINTELL_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)
DOCINTELL_KEY=$(az cognitiveservices account keys list --name "$DOCINTELL_NAME" --resource-group "$RESOURCE_GROUP" --query "key1" -o tsv)

CV_TRAIN_ENDPOINT=$(az cognitiveservices account show --name "$CV_TRAINING_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)
CV_TRAIN_KEY=$(az cognitiveservices account keys list --name "$CV_TRAINING_NAME" --resource-group "$RESOURCE_GROUP" --query "key1" -o tsv)

CV_PREDICT_ENDPOINT=$(az cognitiveservices account show --name "$CV_PREDICTION_NAME" --resource-group "$RESOURCE_GROUP" --query "properties.endpoint" -o tsv)
CV_PREDICT_KEY=$(az cognitiveservices account keys list --name "$CV_PREDICTION_NAME" --resource-group "$RESOURCE_GROUP" --query "key1" -o tsv)

echo "Copy these into demos/.env:"
echo "-------------------------------------------"
cat <<ENVBLOCK
# --- Azure AI Services (Multi-Service) ---
AZURE_AI_ENDPOINT=${AI_ENDPOINT}
AZURE_AI_KEY=${AI_KEY}

# --- Azure OpenAI Service (GPT-4o) ---
AZURE_OPENAI_ENDPOINT=${OPENAI_ENDPOINT}
AZURE_OPENAI_KEY=${OPENAI_KEY}
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_API_VERSION=2024-10-21

# --- Azure OpenAI Service (DALL-E 3) ---
AZURE_OPENAI_DALLE_ENDPOINT=${DALLE_ENDPOINT}
AZURE_OPENAI_DALLE_KEY=${DALLE_KEY}
AZURE_OPENAI_DALLE_DEPLOYMENT=dall-e-3

# --- Azure AI Document Intelligence ---
AZURE_DOCINTELL_ENDPOINT=${DOCINTELL_ENDPOINT}
AZURE_DOCINTELL_KEY=${DOCINTELL_KEY}

# --- Azure Custom Vision ---
AZURE_CUSTOMVISION_TRAINING_ENDPOINT=${CV_TRAIN_ENDPOINT}
AZURE_CUSTOMVISION_TRAINING_KEY=${CV_TRAIN_KEY}
AZURE_CUSTOMVISION_PREDICTION_ENDPOINT=${CV_PREDICT_ENDPOINT}
AZURE_CUSTOMVISION_PREDICTION_KEY=${CV_PREDICT_KEY}
ENVBLOCK

echo ""
echo "-------------------------------------------"
echo ""
echo "Budget safety net (recommended):"
echo "  az consumption budget create \\"
echo "    --budget-name AI900-safety-net \\"
echo "    --resource-group $RESOURCE_GROUP \\"
echo "    --amount 25 --time-grain Monthly \\"
echo "    --category Cost --start-date $(date +%Y-%m-01)"
echo ""
echo "Cleanup when done:"
echo "  az group delete --name $RESOURCE_GROUP --yes --no-wait"
echo ""
