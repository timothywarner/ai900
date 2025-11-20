// ============================================================================
// AI-900 Learning Environment - Main Deployment Template
// ============================================================================
// This template deploys a complete Azure AI learning environment aligned with
// Cloud Adoption Framework (CAF) principles for the AI-900 certification.
//
// CAF Principles Applied:
// - Consistent naming conventions
// - Resource tagging for governance
// - Managed identities for security
// - Diagnostic settings for observability
// - Network security considerations
// ============================================================================

targetScope = 'resourceGroup'

// ============================================================================
// Parameters
// ============================================================================

@description('Environment name (dev, test, prod)')
@allowed(['dev', 'test', 'prod'])
param environment string = 'dev'

@description('Azure region for all resources')
param location string = resourceGroup().location

@description('Project name used in resource naming')
@minLength(3)
@maxLength(10)
param projectName string = 'ai900'

@description('Unique identifier for resources (use a short random string)')
@minLength(3)
@maxLength(6)
param uniqueSuffix string = substring(uniqueString(resourceGroup().id), 0, 6)

@description('Deploy Azure OpenAI Service (requires approved subscription)')
param deployOpenAI bool = false

@description('Deploy Azure Machine Learning workspace')
param deployMachineLearning bool = true

@description('Enable diagnostic settings for all resources')
param enableDiagnostics bool = true

@description('Tags to apply to all resources')
param tags object = {
  Project: 'AI-900-Learning'
  Environment: environment
  ManagedBy: 'Bicep'
  Purpose: 'AI-Fundamentals-Training'
}

// ============================================================================
// Variables - CAF Naming Convention
// ============================================================================

// Naming convention: {resource-type}-{project}-{environment}-{region}-{suffix}
var namingPrefix = '${projectName}-${environment}'
var namingSuffix = uniqueSuffix

// Resource names following CAF conventions
var aiServicesName = 'ai-${namingPrefix}-${namingSuffix}'
var openAIName = 'oai-${namingPrefix}-${namingSuffix}'
var mlWorkspaceName = 'mlw-${namingPrefix}-${namingSuffix}'
var storageAccountName = 'st${projectName}${environment}${namingSuffix}'
var keyVaultName = 'kv-${namingPrefix}-${namingSuffix}'
var logAnalyticsName = 'log-${namingPrefix}-${namingSuffix}'
var appInsightsName = 'appi-${namingPrefix}-${namingSuffix}'
var searchServiceName = 'srch-${namingPrefix}-${namingSuffix}'
var documentIntelligenceName = 'di-${namingPrefix}-${namingSuffix}'

// ============================================================================
// Modules
// ============================================================================

// Log Analytics Workspace for diagnostics
module logAnalytics 'modules/log-analytics.bicep' = if (enableDiagnostics) {
  name: 'deploy-log-analytics'
  params: {
    name: logAnalyticsName
    location: location
    tags: tags
  }
}

// Storage Account for ML workspace and data
module storageAccount 'modules/storage-account.bicep' = {
  name: 'deploy-storage'
  params: {
    name: storageAccountName
    location: location
    tags: tags
    enableDiagnostics: enableDiagnostics
    logAnalyticsWorkspaceId: enableDiagnostics ? logAnalytics.outputs.id : ''
  }
}

// Key Vault for secrets management
module keyVault 'modules/key-vault.bicep' = {
  name: 'deploy-keyvault'
  params: {
    name: keyVaultName
    location: location
    tags: tags
    enableDiagnostics: enableDiagnostics
    logAnalyticsWorkspaceId: enableDiagnostics ? logAnalytics.outputs.id : ''
  }
}

// Application Insights for ML workspace
module appInsights 'modules/app-insights.bicep' = if (deployMachineLearning) {
  name: 'deploy-appinsights'
  params: {
    name: appInsightsName
    location: location
    tags: tags
    logAnalyticsWorkspaceId: enableDiagnostics ? logAnalytics.outputs.id : ''
  }
}

// Azure AI Services (multi-service account)
module aiServices 'modules/ai-services.bicep' = {
  name: 'deploy-ai-services'
  params: {
    name: aiServicesName
    location: location
    tags: tags
    enableDiagnostics: enableDiagnostics
    logAnalyticsWorkspaceId: enableDiagnostics ? logAnalytics.outputs.id : ''
  }
}

// Azure AI Document Intelligence
module documentIntelligence 'modules/document-intelligence.bicep' = {
  name: 'deploy-document-intelligence'
  params: {
    name: documentIntelligenceName
    location: location
    tags: tags
    enableDiagnostics: enableDiagnostics
    logAnalyticsWorkspaceId: enableDiagnostics ? logAnalytics.outputs.id : ''
  }
}

// Azure AI Search
module searchService 'modules/search-service.bicep' = {
  name: 'deploy-search'
  params: {
    name: searchServiceName
    location: location
    tags: tags
    enableDiagnostics: enableDiagnostics
    logAnalyticsWorkspaceId: enableDiagnostics ? logAnalytics.outputs.id : ''
  }
}

// Azure OpenAI Service (optional - requires subscription approval)
module openAI 'modules/openai.bicep' = if (deployOpenAI) {
  name: 'deploy-openai'
  params: {
    name: openAIName
    location: location
    tags: tags
    enableDiagnostics: enableDiagnostics
    logAnalyticsWorkspaceId: enableDiagnostics ? logAnalytics.outputs.id : ''
  }
}

// Azure Machine Learning Workspace (optional)
module machineLearning 'modules/machine-learning.bicep' = if (deployMachineLearning) {
  name: 'deploy-ml-workspace'
  params: {
    name: mlWorkspaceName
    location: location
    tags: tags
    storageAccountId: storageAccount.outputs.id
    keyVaultId: keyVault.outputs.id
    appInsightsId: deployMachineLearning ? appInsights.outputs.id : ''
    enableDiagnostics: enableDiagnostics
    logAnalyticsWorkspaceId: enableDiagnostics ? logAnalytics.outputs.id : ''
  }
}

// ============================================================================
// Outputs
// ============================================================================

@description('Resource Group name')
output resourceGroupName string = resourceGroup().name

@description('Azure AI Services endpoint')
output aiServicesEndpoint string = aiServices.outputs.endpoint

@description('Azure AI Services name')
output aiServicesName string = aiServices.outputs.name

@description('Document Intelligence endpoint')
output documentIntelligenceEndpoint string = documentIntelligence.outputs.endpoint

@description('Search Service endpoint')
output searchServiceEndpoint string = searchService.outputs.endpoint

@description('Storage Account name')
output storageAccountName string = storageAccount.outputs.name

@description('Key Vault name')
output keyVaultName string = keyVault.outputs.name

@description('Azure OpenAI endpoint (if deployed)')
output openAIEndpoint string = deployOpenAI ? openAI.outputs.endpoint : 'Not deployed'

@description('Machine Learning workspace name (if deployed)')
output mlWorkspaceName string = deployMachineLearning ? machineLearning.outputs.name : 'Not deployed'

@description('Log Analytics workspace ID (if enabled)')
output logAnalyticsWorkspaceId string = enableDiagnostics ? logAnalytics.outputs.id : 'Not enabled'
