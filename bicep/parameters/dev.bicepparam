// ============================================================================
// Development Environment Parameters
// ============================================================================
// Cost-optimized settings for learning and experimentation
// ============================================================================

using '../main.bicep'

param environment = 'dev'
param projectName = 'ai900'
param deployOpenAI = false          // Set to true if you have OpenAI access
param deployMachineLearning = true
param enableDiagnostics = true

param tags = {
  Project: 'AI-900-Learning'
  Environment: 'Development'
  ManagedBy: 'Bicep'
  Purpose: 'AI-Fundamentals-Training'
  CostCenter: 'Learning'
}
