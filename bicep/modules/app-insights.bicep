// ============================================================================
// Application Insights Module
// ============================================================================
// Monitoring and telemetry for Azure Machine Learning workspace
// ============================================================================

@description('Application Insights name')
param name string

@description('Azure region')
param location string

@description('Resource tags')
param tags object

@description('Log Analytics workspace ID')
param logAnalyticsWorkspaceId string

// ============================================================================
// Resources
// ============================================================================

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: name
  location: location
  tags: tags
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalyticsWorkspaceId
    IngestionMode: 'LogAnalytics'
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
    RetentionInDays: 30
  }
}

// ============================================================================
// Outputs
// ============================================================================

@description('Application Insights resource ID')
output id string = appInsights.id

@description('Application Insights name')
output name string = appInsights.name

@description('Instrumentation key')
output instrumentationKey string = appInsights.properties.InstrumentationKey

@description('Connection string')
output connectionString string = appInsights.properties.ConnectionString
