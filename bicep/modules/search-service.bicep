// ============================================================================
// Azure AI Search Module
// ============================================================================
// Deploys Azure AI Search (formerly Cognitive Search)
// Provides:
// - Full-text search
// - Vector search for RAG scenarios
// - AI enrichment pipelines
// - Semantic ranking
//
// Essential for Azure OpenAI RAG (Retrieval-Augmented Generation) scenarios
// ============================================================================

@description('Search service name')
param name string

@description('Azure region')
param location string

@description('Resource tags')
param tags object

@description('SKU for Search service')
@allowed(['free', 'basic', 'standard'])
param sku string = 'basic'

@description('Number of replicas')
@minValue(1)
@maxValue(3)
param replicaCount int = 1

@description('Number of partitions')
@allowed([1, 2, 3, 4, 6, 12])
param partitionCount int = 1

@description('Enable diagnostic settings')
param enableDiagnostics bool = false

@description('Log Analytics workspace ID for diagnostics')
param logAnalyticsWorkspaceId string = ''

// ============================================================================
// Resources
// ============================================================================

resource searchService 'Microsoft.Search/searchServices@2023-11-01' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: sku
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    replicaCount: sku == 'free' ? 1 : replicaCount
    partitionCount: sku == 'free' ? 1 : partitionCount
    hostingMode: 'default'
    publicNetworkAccess: 'enabled'
    networkRuleSet: {
      ipRules: []
    }
    encryptionWithCmk: {
      enforcement: 'Unspecified'
    }
    disableLocalAuth: false  // Allow key-based auth for learning
    authOptions: {
      apiKeyOnly: {}
    }
    semanticSearch: sku == 'free' ? 'disabled' : 'free'  // Enable semantic search on paid tiers
  }
}

// Diagnostic settings
resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (enableDiagnostics && !empty(logAnalyticsWorkspaceId)) {
  name: '${name}-diagnostics'
  scope: searchService
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      {
        category: 'OperationLogs'
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

@description('Search service resource ID')
output id string = searchService.id

@description('Search service name')
output name string = searchService.name

@description('Search service endpoint')
output endpoint string = 'https://${searchService.name}.search.windows.net'

@description('Search service principal ID')
output principalId string = searchService.identity.principalId
