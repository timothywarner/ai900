// ============================================================================
// Production Environment Parameters
// ============================================================================
// Production-ready settings with enhanced security and monitoring
// Note: Additional security hardening recommended for true production use
// ============================================================================

using '../main.bicep'

param environment = 'prod'
param projectName = 'ai900'
param deployOpenAI = true
param deployMachineLearning = true
param enableDiagnostics = true

param tags = {
  Project: 'AI-900-Production'
  Environment: 'Production'
  ManagedBy: 'Bicep'
  Purpose: 'AI-Services-Production'
  CostCenter: 'Operations'
  DataClassification: 'Internal'
}
