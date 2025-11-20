// ============================================================================
// Key Vault Module
// ============================================================================
// Secure secrets management for AI service keys and connection strings
// Follows CAF security best practices with RBAC
// ============================================================================

@description('Key Vault name')
param name string

@description('Azure region')
param location string

@description('Resource tags')
param tags object

@description('Enable diagnostic settings')
param enableDiagnostics bool = false

@description('Log Analytics workspace ID for diagnostics')
param logAnalyticsWorkspaceId string = ''

// ============================================================================
// Resources
// ============================================================================

resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: name
  location: location
  tags: tags
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true      // CAF: Use RBAC instead of access policies
    enableSoftDelete: true             // Security: Prevent accidental deletion
    softDeleteRetentionInDays: 7       // Short retention for learning env
    enablePurgeProtection: false       // Allow purge in learning env
    enabledForDeployment: false
    enabledForDiskEncryption: false
    enabledForTemplateDeployment: true // Allow ARM/Bicep to read secrets
    publicNetworkAccess: 'Enabled'     // Allow for learning; restrict in prod
    networkAcls: {
      defaultAction: 'Allow'
      bypass: 'AzureServices'
    }
  }
}

// Diagnostic settings
resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (enableDiagnostics && !empty(logAnalyticsWorkspaceId)) {
  name: '${name}-diagnostics'
  scope: keyVault
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      {
        category: 'AuditEvent'
        enabled: true
      }
      {
        category: 'AzurePolicyEvaluationDetails'
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

@description('Key Vault resource ID')
output id string = keyVault.id

@description('Key Vault name')
output name string = keyVault.name

@description('Key Vault URI')
output uri string = keyVault.properties.vaultUri
