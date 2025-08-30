# 🤖 Hour 2: Machine Learning on Azure

**Duration:** 1 hour  
**Exam Weight:** 20-25% (HIGHEST!)  
**Philosophy:** Zero to hero - deploy a real ML model in 45 minutes!

## 🎓 Exam Focus Areas
- **Identify common machine learning techniques**
- **Identify Azure tools and services for machine learning**
- **Identify features of AutoML**
- **Identify regression, classification, and clustering workloads**

## 📚 Key Concepts (10 min theory)

### 1. ML Types (KNOW THE DIFFERENCE!)
- **Supervised Learning**: Has labeled training data
  - Classification: Predict categories (spam/not spam)
  - Regression: Predict numbers (house prices)
- **Unsupervised Learning**: No labels
  - Clustering: Find groups (customer segments)
- **Reinforcement Learning**: Learn through rewards

### 2. Azure ML Options
- **Automated ML**: No-code, automatic algorithm selection
- **Designer**: Drag-and-drop visual interface
- **Notebooks**: Code-first approach for data scientists

### 3. ML Workflow
1. **Data** → 2. **Train** → 3. **Evaluate** → 4. **Deploy** → 5. **Monitor**

### 4. Deep Learning & Transformers (NEW for May 2025!)
- **Deep Learning**: Neural networks with multiple hidden layers
  - CNNs: Convolutional Neural Networks (images)
  - RNNs: Recurrent Neural Networks (sequences)
  - Transformers: Attention-based architecture
  
- **Transformer Architecture** (Foundation of GPT, BERT):
  - Self-attention mechanism: "Paying attention to relevant parts"
  - Parallel processing: Much faster than RNNs
  - Powers modern NLP: ChatGPT, Azure OpenAI, etc.

## 🔥 Demo Scripts

### Demo 1: Azure ML Workspace Setup (5 min)
```bash
# Quick setup in Azure Portal
# 1. Create Resource > Machine Learning
# 2. Name: ai900-ml-demo
# 3. Show workspace components:
#    - Compute (for training)
#    - Datastores (for data)
#    - Models (trained models)
#    - Endpoints (deployments)
```

### Demo 2: Automated ML Classification (20 min)
```python
# titanic-automl.py
# Use this narrative while clicking through Azure ML Studio

"""
STORY: "Let's predict Titanic survival - a classic ML problem!"

1. Navigate to ml.azure.com
2. Upload titanic.csv dataset
3. Create AutoML experiment:
   - Task type: Classification
   - Target column: Survived
   - Compute: Create new (Standard_DS11_v2)
   
4. While it trains, explain:
   - Feature engineering happening automatically
   - Multiple algorithms being tested
   - Cross-validation for accuracy
   
5. Show results:
   - Best model (usually Random Forest or Voting Ensemble)
   - Confusion matrix
   - Feature importance
   
6. Deploy model:
   - Real-time endpoint
   - Test with sample data
"""

# Test endpoint with Python
import urllib.request
import json

# Endpoint URL (from deployment)
url = 'YOUR_ENDPOINT_URL'
api_key = 'YOUR_API_KEY'

# Test data (passenger info)
data = {
    "Inputs": {
        "data": [{
            "PassengerId": 1,
            "Pclass": 1,
            "Sex": "female",
            "Age": 30,
            "SibSp": 1,
            "Parch": 0,
            "Fare": 100,
            "Embarked": "S"
        }]
    }
}

body = str.encode(json.dumps(data))
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)
response = urllib.request.urlopen(req)
result = json.loads(response.read())
print(f"Survival prediction: {result['Results'][0]}")
```

### Demo 3: Designer Pipeline (10 min)
```python
# designer-demo-narrative.py
"""
Quick Designer Demo - Visual ML Pipeline

1. Open Designer in Azure ML Studio
2. Start with Sample: "Regression - Automobile Price Prediction"
3. Show drag-and-drop components:
   - Import Data
   - Select Columns
   - Clean Missing Data
   - Split Data
   - Train Model (Linear Regression)
   - Score Model
   - Evaluate Model

4. Key Points:
   - No coding required
   - Each module is configurable
   - Can convert to Python code
   - Great for learning ML workflow
"""
```

## 💡 Exam Tips & Tricks

### ⚡ Algorithm Selection Guide
Know when to use what:
- **Classification**: Predict categories
  - Binary: Yes/No, True/False
  - Multiclass: Red/Blue/Green
  - Examples: Spam detection, disease diagnosis
  
- **Regression**: Predict numbers
  - Linear: Straight-line relationships
  - Polynomial: Curved relationships
  - Examples: Price prediction, temperature forecast
  
- **Clustering**: Find natural groups
  - K-Means: Specify number of clusters
  - Hierarchical: Tree of clusters
  - Examples: Customer segmentation, anomaly detection

### 📊 Metrics to Know
- **Classification Metrics**:
  - Accuracy: Overall correctness
  - Precision: Of predicted positives, how many correct?
  - Recall: Of actual positives, how many found?
  - F1 Score: Balance of precision and recall

- **Regression Metrics**:
  - MAE: Mean Absolute Error (average error size)
  - RMSE: Root Mean Square Error (penalizes large errors)
  - R²: How well model fits (0-1, higher better)

### 📝 Practice Questions

**Q1:** You need to predict customer churn (will they leave? yes/no). Which ML type?
- A) Regression
- B) Binary Classification ✅
- C) Clustering
- D) Multiclass Classification

**Q2:** What's the main benefit of Automated ML?
- A) It's always more accurate
- B) It automatically selects and tunes algorithms ✅
- C) It requires no data
- D) It's free to use

**Q3:** You have sales data and want to predict next month's revenue. Which algorithm type?
- A) Classification
- B) Clustering
- C) Regression ✅
- D) Reinforcement Learning

**Q4:** In Azure ML Designer, what must you do before training a model?
- A) Deploy the model
- B) Split the data into training and testing sets ✅
- C) Create a real-time endpoint
- D) Export to Python

**Q5:** What is the key innovation of Transformer architecture? (NEW!)
- A) It uses convolution layers
- B) It processes sequences recursively
- C) It uses self-attention mechanisms ✅
- D) It requires less training data

**Q6:** Which models are based on Transformer architecture?
- A) Decision Trees and Random Forests
- B) GPT and BERT ✅
- C) Linear and Logistic Regression
- D) K-Means and DBSCAN

## 🚀 Hands-on Challenge
**The 10-Minute Model Challenge:**
1. Use AutoML to create a model predicting diabetes
2. Deploy it as a web service
3. First person to successfully call their endpoint wins!

## 📌 Remember
- AutoML is PERFECT for demos - it's visual and fast
- Always explain what's happening "behind the scenes"
- Connect everything to real-world use cases
- Emphasize that AI-900 loves AutoML questions

## 🔗 Resources
- [Azure ML Documentation](https://docs.microsoft.com/azure/machine-learning/)
- [AutoML Tutorial](https://docs.microsoft.com/azure/machine-learning/tutorial-first-experiment-automated-ml)
- [ML Algorithm Cheat Sheet](https://docs.microsoft.com/azure/machine-learning/algorithm-cheat-sheet) 