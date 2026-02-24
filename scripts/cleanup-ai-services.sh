#!/usr/bin/env bash
# =============================================================================
# AI-900 Demo Infrastructure - Cleanup (Destroy Everything)
# =============================================================================
# Deletes the entire resource group, removing all AI services at once.
# This is the single-command teardown for the training environment.
#
# Usage:
#   chmod +x scripts/cleanup-ai-services.sh
#   ./scripts/cleanup-ai-services.sh
# =============================================================================

set -euo pipefail

RESOURCE_GROUP="AI900-Feb2026"

echo "==========================================="
echo " AI-900 Cleanup - Deleting $RESOURCE_GROUP"
echo "==========================================="
echo ""
echo "This will PERMANENTLY delete all resources in the resource group."
echo "Press Ctrl+C within 5 seconds to cancel..."
sleep 5

echo "Deleting resource group (async)..."
az group delete \
  --name "$RESOURCE_GROUP" \
  --yes \
  --no-wait

echo ""
echo "Deletion initiated. The resource group will be removed in ~2-5 minutes."
echo "Monitor progress: az group show --name $RESOURCE_GROUP --query provisioningState -o tsv"
echo ""
