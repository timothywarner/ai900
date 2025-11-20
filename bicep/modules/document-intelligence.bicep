// ============================================================================
// Azure AI Document Intelligence Module
// ============================================================================
// Deploys Azure AI Document Intelligence (formerly Form Recognizer)
// Provides document processing capabilities:
// - Pre-built models (invoices, receipts, IDs, business cards)
// - Custom models for specific document types
// - Layout analysis and table extraction
// ============================================================================

@description('Document Intelligence account name')
param name string

@description('Azure region')
param location string

@description('Resource tags')
param tags object

@description('SKU for Document Intelligence')
@allowed(['F0', 'S0'])
param sku string = 'S0'

@description('Enable diagnostic settings')
param enableDiagnostics bool = false

@description('Log Analytics workspace ID for diagnostics')
param logAnalyticsWorkspaceId string = ''

// ============================================================================
// Resources
// ============================================================================

resource documentIntelligence 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: name
  location: location
  tags: tags
  kind: 'FormRecognizer'
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

// Diagnostic settings
resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (enableDiagnostics && !empty(logAnalyticsWorkspaceId)) {
  name: '${name}-diagnostics'
  scope: documentIntelligence
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

@description('Document Intelligence resource ID')
output id string = documentIntelligence.id

@description('Document Intelligence name')
output name string = documentIntelligence.name

@description('Document Intelligence endpoint')
output endpoint string = documentIntelligence.properties.endpoint

@description('Document Intelligence principal ID')
output principalId string = documentIntelligence.identity.principalId
