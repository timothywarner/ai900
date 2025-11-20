// ============================================================================
// Azure Machine Learning Workspace Module
// ============================================================================
// Deploys Azure Machine Learning workspace with:
// - Integration with Storage, Key Vault, and Application Insights
// - Managed identity for secure access
// - Diagnostic settings for monitoring
//
// Provides capabilities for:
// - AutoML (Automated Machine Learning)
// - Designer (drag-and-drop ML)
// - Notebooks for custom code
// - MLflow experiment tracking
// ============================================================================

@description('Machine Learning workspace name')
param name string

@description('Azure region')
param location string

@description('Resource tags')
param tags object

@description('Storage account resource ID')
param storageAccountId string

@description('Key Vault resource ID')
param keyVaultId string

@description('Application Insights resource ID')
param appInsightsId string

@description('Enable diagnostic settings')
param enableDiagnostics bool = false

@description('Log Analytics workspace ID for diagnostics')
param logAnalyticsWorkspaceId string = ''

// ============================================================================
// Resources
// ============================================================================

resource mlWorkspace 'Microsoft.MachineLearningServices/workspaces@2023-10-01' = {
  name: name
  location: location
  tags: tags
  identity: {
    type: 'SystemAssigned'
  }
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  properties: {
    friendlyName: name
    storageAccount: storageAccountId
    keyVault: keyVaultId
    applicationInsights: appInsightsId
    hbiWorkspace: false  // Not high business impact for learning
    v1LegacyMode: false
    publicNetworkAccess: 'Enabled'
    // Managed network for secure training (optional for learning)
    managedNetwork: {
      isolationMode: 'Disabled'  // Allow all for learning; use AllowInternetOutbound in prod
    }
  }
}

// Diagnostic settings
resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (enableDiagnostics && !empty(logAnalyticsWorkspaceId)) {
  name: '${name}-diagnostics'
  scope: mlWorkspace
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      {
        category: 'AmlComputeClusterEvent'
        enabled: true
      }
      {
        category: 'AmlComputeJobEvent'
        enabled: true
      }
      {
        category: 'AmlRunStatusChangedEvent'
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

@description('Machine Learning workspace resource ID')
output id string = mlWorkspace.id

@description('Machine Learning workspace name')
output name string = mlWorkspace.name

@description('Machine Learning workspace URL')
output workspaceUrl string = 'https://ml.azure.com/?wsid=${mlWorkspace.id}'

@description('Machine Learning principal ID')
output principalId string = mlWorkspace.identity.principalId
