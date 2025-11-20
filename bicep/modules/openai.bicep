// ============================================================================
// Azure OpenAI Service Module
// ============================================================================
// Deploys Azure OpenAI Service with optional model deployments
//
// NOTE: Requires subscription to be approved for Azure OpenAI access
// Apply at: https://aka.ms/oai/access
//
// Provides access to:
// - GPT-4 and GPT-3.5 models
// - DALL-E image generation
// - Embeddings models
// - Whisper speech models
// ============================================================================

@description('Azure OpenAI account name')
param name string

@description('Azure region')
param location string

@description('Resource tags')
param tags object

@description('SKU for Azure OpenAI')
@allowed(['S0'])
param sku string = 'S0'

@description('Enable diagnostic settings')
param enableDiagnostics bool = false

@description('Log Analytics workspace ID for diagnostics')
param logAnalyticsWorkspaceId string = ''

@description('Deploy GPT-35-Turbo model')
param deployGpt35Turbo bool = true

@description('Deploy text-embedding-ada-002 model')
param deployEmbeddings bool = true

// ============================================================================
// Resources
// ============================================================================

resource openAI 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: name
  location: location
  tags: tags
  kind: 'OpenAI'
  sku: {
    name: sku
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    customSubDomainName: name
    publicNetworkAccess: 'Enabled'
    networkAcls: {
      defaultAction: 'Allow'
    }
  }
}

// GPT-3.5 Turbo deployment
resource gpt35Deployment 'Microsoft.CognitiveServices/accounts/deployments@2023-10-01-preview' = if (deployGpt35Turbo) {
  parent: openAI
  name: 'gpt-35-turbo'
  sku: {
    name: 'Standard'
    capacity: 10  // Tokens per minute (in thousands)
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-35-turbo'
      version: '0613'
    }
    raiPolicyName: 'Microsoft.Default'
  }
}

// Embeddings deployment for RAG scenarios
resource embeddingsDeployment 'Microsoft.CognitiveServices/accounts/deployments@2023-10-01-preview' = if (deployEmbeddings) {
  parent: openAI
  name: 'text-embedding-ada-002'
  sku: {
    name: 'Standard'
    capacity: 10
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: 'text-embedding-ada-002'
      version: '2'
    }
    raiPolicyName: 'Microsoft.Default'
  }
  dependsOn: [
    gpt35Deployment  // Sequential deployment to avoid conflicts
  ]
}

// Diagnostic settings
resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (enableDiagnostics && !empty(logAnalyticsWorkspaceId)) {
  name: '${name}-diagnostics'
  scope: openAI
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      {
        category: 'Audit'
        enabled: true
      }
      {
        category: 'RequestResponse'
        enabled: true
      }
    ]
    metrics: [
      {
        category: 'AllMetrics'
        enabled: true
      }
    ]
  }
}

// ============================================================================
// Outputs
// ============================================================================

@description('Azure OpenAI resource ID')
output id string = openAI.id

@description('Azure OpenAI name')
output name string = openAI.name

@description('Azure OpenAI endpoint')
output endpoint string = openAI.properties.endpoint

@description('Azure OpenAI principal ID')
output principalId string = openAI.identity.principalId
