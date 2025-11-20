# AI-900 Bicep Deployment Templates

Infrastructure as Code templates for deploying a complete Azure AI learning environment, aligned with Cloud Adoption Framework (CAF) principles.

## Overview

These templates deploy the Azure AI services covered in the AI-900 certification exam:

| Service | Description | AI-900 Topic |
|---------|-------------|--------------|
| Azure AI Services | Multi-service (Vision, Language, Speech, Translator) | Computer Vision, NLP |
| Azure AI Document Intelligence | Document processing and OCR | Computer Vision |
| Azure AI Search | Full-text and vector search | Generative AI (RAG) |
| Azure OpenAI Service | GPT, DALL-E, Embeddings | Generative AI |
| Azure Machine Learning | AutoML, Designer, Notebooks | Machine Learning |

## CAF Principles Applied

These templates follow Cloud Adoption Framework best practices:

### Naming Convention
Resources use consistent naming: `{type}-{project}-{env}-{suffix}`

| Resource Type | Abbreviation | Example |
|--------------|--------------|---------|
| AI Services | `ai-` | `ai-ai900-dev-x7k9m2` |
| OpenAI | `oai-` | `oai-ai900-dev-x7k9m2` |
| ML Workspace | `mlw-` | `mlw-ai900-dev-x7k9m2` |
| Storage | `st` | `stai900devx7k9m2` |
| Key Vault | `kv-` | `kv-ai900-dev-x7k9m2` |
| Search | `srch-` | `srch-ai900-dev-x7k9m2` |
| Log Analytics | `log-` | `log-ai900-dev-x7k9m2` |

### Security
- **Managed Identities**: All services use system-assigned managed identities
- **RBAC**: Key Vault uses Azure RBAC instead of access policies
- **Encryption**: Storage uses Microsoft-managed encryption
- **TLS 1.2**: Enforced on all services
- **No Public Blobs**: Storage denies public blob access

### Governance
- **Consistent Tagging**: All resources tagged with Project, Environment, ManagedBy
- **Diagnostic Settings**: Centralized logging to Log Analytics
- **Soft Delete**: Enabled on Key Vault to prevent accidental deletion

### Cost Management
- **Development SKUs**: Uses cost-effective tiers suitable for learning
- **Daily Caps**: Log Analytics has 1GB daily cap
- **Optional Services**: OpenAI and ML are optional parameters

## Prerequisites

1. **Azure CLI** (version 2.50+) or **Azure PowerShell**
2. **Azure subscription** with Contributor access
3. **Azure OpenAI access** (if deploying OpenAI) - [Apply here](https://aka.ms/oai/access)

## Quick Start

### 1. Clone and Navigate

```bash
git clone <repository-url>
cd ai900/bicep
```

### 2. Login to Azure

```bash
az login
az account set --subscription "<subscription-id>"
```

### 3. Create Resource Group

```bash
az group create \
  --name rg-ai900-learning \
  --location eastus
```

### 4. Deploy

**Basic deployment (no OpenAI):**
```bash
az deployment group create \
  --resource-group rg-ai900-learning \
  --template-file main.bicep \
  --parameters environment=dev projectName=ai900
```

**Full deployment (with OpenAI):**
```bash
az deployment group create \
  --resource-group rg-ai900-learning \
  --template-file main.bicep \
  --parameters environment=dev projectName=ai900 deployOpenAI=true
```

**Using parameter file:**
```bash
az deployment group create \
  --resource-group rg-ai900-learning \
  --template-file main.bicep \
  --parameters @parameters/dev.bicepparam
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `environment` | string | `dev` | Environment (dev, test, prod) |
| `location` | string | Resource group location | Azure region |
| `projectName` | string | `ai900` | Project name (3-10 chars) |
| `uniqueSuffix` | string | Auto-generated | Unique suffix (3-6 chars) |
| `deployOpenAI` | bool | `false` | Deploy Azure OpenAI |
| `deployMachineLearning` | bool | `true` | Deploy ML Workspace |
| `enableDiagnostics` | bool | `true` | Enable diagnostic settings |
| `tags` | object | See template | Resource tags |

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Resource Group                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  Log         │  │  Storage     │  │  Key Vault   │   │
│  │  Analytics   │  │  Account     │  │              │   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘   │
│         │                 │                 │            │
│         └─────────────────┼─────────────────┘            │
│                           │                              │
│  ┌────────────────────────┼────────────────────────┐    │
│  │                        ▼                        │    │
│  │  ┌──────────────┐  ┌──────────────┐            │    │
│  │  │  AI Services │  │  Document    │            │    │
│  │  │  (Multi)     │  │  Intelligence│            │    │
│  │  └──────────────┘  └──────────────┘            │    │
│  │                                                 │    │
│  │  ┌──────────────┐  ┌──────────────┐            │    │
│  │  │  AI Search   │  │  OpenAI      │ (optional) │    │
│  │  │              │  │  Service     │            │    │
│  │  └──────────────┘  └──────────────┘            │    │
│  │                                                 │    │
│  │  ┌──────────────────────────────────┐          │    │
│  │  │  Machine Learning Workspace      │(optional)│    │
│  │  │  + App Insights                  │          │    │
│  │  └──────────────────────────────────┘          │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Module Reference

### Core Services

| Module | File | Description |
|--------|------|-------------|
| AI Services | `modules/ai-services.bicep` | Multi-service cognitive account |
| Document Intelligence | `modules/document-intelligence.bicep` | Form/document processing |
| Search Service | `modules/search-service.bicep` | Full-text and vector search |
| OpenAI | `modules/openai.bicep` | GPT and embeddings models |
| Machine Learning | `modules/machine-learning.bicep` | ML workspace with AutoML |

### Supporting Services

| Module | File | Description |
|--------|------|-------------|
| Storage Account | `modules/storage-account.bicep` | Secure blob storage |
| Key Vault | `modules/key-vault.bicep` | Secrets management |
| Log Analytics | `modules/log-analytics.bicep` | Centralized logging |
| App Insights | `modules/app-insights.bicep` | ML telemetry |

## Post-Deployment Steps

### 1. Get Service Keys

```bash
# AI Services key
az cognitiveservices account keys list \
  --resource-group rg-ai900-learning \
  --name <ai-services-name>

# OpenAI key (if deployed)
az cognitiveservices account keys list \
  --resource-group rg-ai900-learning \
  --name <openai-name>

# Search Service key
az search admin-key show \
  --resource-group rg-ai900-learning \
  --service-name <search-name>
```

### 2. Access Services

- **Azure AI Services**: Use the endpoint from outputs with your key
- **Machine Learning**: Open ML Studio at `https://ml.azure.com`
- **OpenAI**: Use Azure OpenAI Studio or REST API

### 3. Store Keys Securely

```bash
# Store keys in Key Vault
az keyvault secret set \
  --vault-name <keyvault-name> \
  --name "ai-services-key" \
  --value "<key>"
```

## Cost Estimation

Estimated monthly costs (USD) for development environment:

| Service | SKU | Est. Cost |
|---------|-----|-----------|
| AI Services | S0 | $1-10 (pay per use) |
| Document Intelligence | S0 | $1-10 (pay per use) |
| AI Search | Basic | ~$75 |
| OpenAI | S0 | $0-50 (pay per use) |
| Machine Learning | Basic | $0 (compute extra) |
| Storage | Standard LRS | ~$1 |
| Key Vault | Standard | ~$0.03 |
| Log Analytics | Pay-as-you-go | ~$2-5 |

**Note**: Actual costs depend on usage. Use [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/) for estimates.

## Cleanup

Delete all resources:

```bash
az group delete --name rg-ai900-learning --yes --no-wait
```

## Troubleshooting

### Common Issues

**"Azure OpenAI is not available in this region"**
- Check [Azure OpenAI availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)
- Use `eastus`, `eastus2`, or `westeurope`

**"Subscription not approved for Azure OpenAI"**
- Apply for access at https://aka.ms/oai/access
- Set `deployOpenAI=false` to skip OpenAI deployment

**"Resource name already exists"**
- Names must be globally unique
- Change `uniqueSuffix` parameter

**"Quota exceeded"**
- Check subscription quotas in Azure Portal
- Request quota increase or use different region

## Learn More

### Microsoft Learn
- [Azure AI Services Documentation](https://learn.microsoft.com/azure/ai-services/)
- [Azure Machine Learning Documentation](https://learn.microsoft.com/azure/machine-learning/)
- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Bicep Documentation](https://learn.microsoft.com/azure/azure-resource-manager/bicep/)

### Cloud Adoption Framework
- [CAF Naming Convention](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)
- [CAF Resource Tagging](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/azure-best-practices/resource-tagging)
- [CAF Security Best Practices](https://learn.microsoft.com/azure/cloud-adoption-framework/secure/)

---

*Templates created for AI-900 learning | Updated: November 2025*
