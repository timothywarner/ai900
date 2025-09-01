# Azure Machine Learning Step-by-Step Guide

This guide demonstrates how to use Azure Machine Learning for a complete ML workflow.

## Prerequisites

- Azure subscription
- Contributor or Owner access to the subscription
- Basic knowledge of Python and ML concepts

## 1. Set Up Your Azure ML Workspace

### Using Azure Portal

1. Sign in to the [Azure portal](https://portal.azure.com)
2. Click "Create a resource"
3. Search for "Machine Learning"
4. Select "Azure Machine Learning"
5. Fill in the details:
   - Subscription: Your subscription
   - Resource group: Create new or use existing
   - Workspace name: Choose a unique name
   - Region: Choose a region close to you
   - Storage account: Accept default
   - Key vault: Accept default
   - Application insights: Accept default
   - Container registry: None (create one later if needed)
6. Click "Review + create" and then "Create"

### Using Azure CLI

```bash
# Install the Azure CLI extension for ML
az extension add -n azure-cli-ml

# Login to Azure
az login

# Create a resource group
az group create --name rg-azureml-demo --location eastus

# Create Azure ML workspace
az ml workspace create --workspace-name aml-workspace-demo \
                       --resource-group rg-azureml-demo \
                       --location eastus
```

## 2. Explore Azure ML Studio

1. Once your workspace is created, click "Launch studio"
2. Familiarize yourself with the interface:
   - Home: Dashboard with recent activities
   - Notebooks: Create and run Jupyter notebooks
   - Automated ML: Create no-code ML models
   - Designer: Visual interface for ML workflows
   - Assets: Datasets, models, environments, etc.
   - Compute: Manage compute resources

## 3. Create a Compute Instance

1. In Azure ML Studio, go to "Compute" → "Compute instances"
2. Click "+ New"
3. Provide a name for your compute instance
4. Select a VM Size (e.g., Standard_DS3_v2)
5. Click "Create"

## 4. Upload a Dataset

### Using the Studio UI

1. Go to "Data" → "Datastores"
2. Select your default blob storage
3. Click "Upload"
4. Select your data files
5. Once uploaded, go to "Data" → "Datasets"
6. Click "+ Create dataset" → "From datastore"
7. Follow the steps to create a tabular or file dataset

### Using Python SDK

```python
from azureml.core import Workspace, Dataset, Datastore

# Connect to your workspace
ws = Workspace.from_config()

# Get default datastore
datastore = ws.get_default_datastore()

# Upload data from local path
datastore.upload(src_dir='./data',
                 target_path='dataset/tabular/iris',
                 overwrite=True)

# Create and register dataset
dataset = Dataset.Tabular.from_delimited_files(
    path=[(datastore, 'dataset/tabular/iris/*.csv')]
)
dataset = dataset.register(workspace=ws,
                         name='iris-dataset',
                         description='Iris flower dataset',
                         create_new_version=True)
```

## 5. Using Automated Machine Learning

1. In Azure ML Studio, go to "Automated ML"
2. Click "+ New automated ML run"
3. Select your dataset
4. Configure experiment:
   - Experiment name: Give it a descriptive name
   - Target column: The feature you want to predict
   - Select compute: Choose your compute instance or cluster
5. Choose a task type (Classification, Regression, Time-series forecasting)
6. Configure settings:
   - Primary metric: e.g., AUC_weighted for classification
   - Training job time: Set maximum time for the experiment
   - Max concurrent iterations: Based on your compute
   - Early stopping: Enable to save resources
7. Click "Finish" to start the experiment

## 6. Using Azure ML Designer

1. In Azure ML Studio, go to "Designer"
2. Click "+" to create a new pipeline
3. Drag and drop components from the left panel:
   - Start with a dataset
   - Add preprocessing steps (e.g., "Select Columns", "Clean Missing Data")
   - Add a training algorithm (e.g., "Train Model" + "Linear Regression")
   - Add evaluation components (e.g., "Score Model", "Evaluate Model")
4. Connect the components to create a workflow
5. Submit the pipeline to run on your compute
6. Once complete, right-click the evaluation component to visualize results

## 7. Deploy a Model as a Web Service

### From Automated ML

1. Go to your completed AutoML run
2. Select the best model from the "Models" tab
3. Click "Deploy" → "Web service"
4. Configure:
   - Name: Give your endpoint a name
   - Compute type: ACI (for testing) or AKS (for production)
   - Authentication: Enable or disable
5. Click "Deploy"

### From Designer

1. After running a designer pipeline, click "Create inference pipeline"
2. Modify the pipeline for inferencing (remove training components)
3. Submit the pipeline to validate
4. Click "Deploy" and configure similar to AutoML deployment

## 8. Consume the Deployed Endpoint

### Using Python

```python
import requests
import json

# URL for the web service
scoring_uri = 'YOUR_SCORING_URI'
# API key for the endpoint
key = 'YOUR_API_KEY'

# Test data
data = {
    "data": [
        {
            "feature1": 5.1,
            "feature2": 3.5,
            "feature3": 1.4,
            "feature4": 0.2
        }
    ]
}

# Convert to JSON string
input_data = json.dumps(data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# Add authentication header if needed
if key:
    headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
```

## 9. Monitor Model Performance

1. In Azure ML Studio, go to "Endpoints"
2. Select your deployed endpoint
3. Check the "Monitoring" tab to see:
   - Request rates
   - Response times
   - Errors
   - Data drift (if enabled)

## 10. Next Steps

- Explore MLOps with Azure DevOps integration
- Try different model algorithms and hyperparameter tuning
- Set up data drift detection
- Implement CI/CD pipelines for your ML workflows

## Resources

- [Azure ML Documentation](https://docs.microsoft.com/en-us/azure/machine-learning/)
- [Azure ML Python SDK Documentation](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py)
- [Azure ML Samples Repository](https://github.com/Azure/MachineLearningNotebooks) 