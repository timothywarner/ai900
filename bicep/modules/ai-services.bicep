// ============================================================================
// Azure AI Services (Multi-Service) Module
// ============================================================================
// Deploys a multi-service Azure AI resource providing:
// - Azure AI Vision (Image Analysis, OCR, Face)
// - Azure AI Language (Sentiment, NER, Key Phrases, etc.)
// - Azure AI Speech (Speech-to-Text, Text-to-Speech)
// - Azure AI Translator
//
// This is ideal for AI-900 learning as it provides access to multiple
// AI capabilities through a single endpoint and key.
// ============================================================================

@description('AI Services account name')
param name string

@description('Azure region')
param location string

@description('Resource tags')
param tags object

@description('SKU for the AI Services account')
@allowed(['F0', 'S0'])
param sku string = 'S0'

@description('Enable diagnostic settings')
param enableDiagnostics bool = false

@description('Log Analytics workspace ID for diagnostics')
param logAnalyticsWorkspaceId string = ''

// ============================================================================
// Resources
// ============================================================================

resource aiServices 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: name
  location: location
  tags: tags
  kind: 'CognitiveServices'  // Multi-service account
  sku: {
    name: sku
  }
  identity: {
    type: 'SystemAssigned'  // CAF: Use managed identity
  }
  properties: {
    customSubDomainName: name
    publicNetworkAccess: 'Enabled'  // Allow for learning; restrict in prod
    networkAcls: {
      defaultAction: 'Allow'
    }
    // Responsible AI: Accept terms
    apiProperties: {
      statisticsEnabled: false
    }
  }
}

// Diagnostic settings
resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (enableDiagnostics && !empty(logAnalyticsWorkspaceId)) {
  name: '${name}-diagnostics'
  scope: aiServices
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

@description('AI Services resource ID')
output id string = aiServices.id

@description('AI Services name')
output name string = aiServices.name

@description('AI Services endpoint')
output endpoint string = aiServices.properties.endpoint

@description('AI Services principal ID (managed identity)')
output principalId string = aiServices.identity.principalId
