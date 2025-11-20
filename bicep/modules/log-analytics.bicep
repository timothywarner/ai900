// ============================================================================
// Log Analytics Workspace Module
// ============================================================================
// Provides centralized logging and monitoring for all AI services
// ============================================================================

@description('Name of the Log Analytics workspace')
param name string

@description('Azure region')
param location string

@description('Resource tags')
param tags object

@description('Retention period in days')
@minValue(30)
@maxValue(730)
param retentionInDays int = 30

// ============================================================================
// Resources
// ============================================================================

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: name
  location: location
  tags: tags
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: retentionInDays
    features: {
      enableLogAccessUsingOnlyResourcePermissions: true
    }
    workspaceCapping: {
      dailyQuotaGb: 1  // Cost control for learning environment
    }
  }
}

// ============================================================================
// Outputs
// ============================================================================

@description('Log Analytics workspace resource ID')
output id string = logAnalytics.id

@description('Log Analytics workspace name')
output name string = logAnalytics.name
