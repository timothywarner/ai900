---
exam: AI-900
domain: "Describe fundamental principles of machine learning on Azure"
weight: "15-20%"
item_count: 5
cognitive_level: Apply
generated: 2026-02-23
---

# Domain 2: Fundamental Principles of Machine Learning on Azure

Practice items for AI-900 exam preparation.

---

### Item 1
**Objective:** Identify regression machine learning scenarios
**Cognitive Level:** Apply

**Stem:**
Contoso Real Estate is building a machine learning model to help agents provide accurate property valuations. The model will use historical sales data including square footage, number of bedrooms, neighborhood crime rate, and proximity to schools. The model must predict the expected selling price of a home as a dollar amount. A data scientist needs to select the appropriate machine learning technique.

Which type of machine learning should the data scientist use?

A) Classification
B) Clustering
C) Regression
D) Deep learning with a convolutional neural network

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because regression is a supervised learning technique that predicts a continuous numeric value. Predicting a home selling price in dollars based on input features like square footage and location attributes is a classic regression scenario.
- **A is incorrect** because classification predicts a categorical label (such as "high value" or "low value"), not a continuous numeric value like a dollar amount.
- **B is incorrect** because clustering is an unsupervised technique that groups similar data points together without predicting a specific output value. It does not predict a numeric target.
- **D is incorrect** because convolutional neural networks (CNNs) are primarily used for image-related tasks such as image classification and object detection, not for predicting numeric values from tabular features like square footage and bedroom count.

**Reference:** [https://learn.microsoft.com/training/modules/fundamentals-machine-learning/4-regression](https://learn.microsoft.com/training/modules/fundamentals-machine-learning/4-regression)

</details>

---

### Item 2
**Objective:** Identify clustering machine learning scenarios; Identify features and labels in a dataset for machine learning
**Cognitive Level:** Apply

**Stem:**
Northwind Traders operates 200 retail stores across the country. The marketing team wants to group stores into segments based on purchasing patterns, average transaction value, and foot traffic volume. The team does not have predefined categories for these segments. They plan to use Azure Machine Learning to discover natural groupings in the data and then tailor promotions to each group.

Which type of machine learning technique should the marketing team use?

A) Binary classification, because each store will be assigned to one of two categories
B) Regression, because the model needs to predict a numeric value for each store
C) Clustering, because the model needs to discover natural groupings in unlabeled data
D) Multiclass classification, because each store will be assigned to one of several predefined categories

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because clustering is an unsupervised machine learning technique that identifies natural groupings in data without requiring predefined labels. The scenario explicitly states the team does not have predefined categories and wants to discover segments, which is the defining characteristic of a clustering problem.
- **A is incorrect** because binary classification is a supervised technique that requires labeled training data with two predefined categories. The marketing team has no predefined categories.
- **B is incorrect** because regression predicts a continuous numeric value (such as revenue), not group membership. The goal is to segment stores, not predict a number.
- **D is incorrect** because multiclass classification, like binary classification, is a supervised technique that requires predefined category labels in the training data. The scenario states that no predefined categories exist.

**Reference:** [https://learn.microsoft.com/training/modules/fundamentals-machine-learning/7-clustering](https://learn.microsoft.com/training/modules/fundamentals-machine-learning/7-clustering)

</details>

---

### Item 3
**Objective:** Describe capabilities of automated machine learning
**Cognitive Level:** Apply

**Stem:**
Fabrikam Insurance has a team of business analysts who understand their claims data well but have limited data science and coding experience. They need to build a classification model that predicts whether an insurance claim is fraudulent. The team wants to evaluate multiple algorithms automatically, minimize manual model selection effort, and deploy the best-performing model to a real-time endpoint. They plan to use Azure Machine Learning.

Which Azure Machine Learning capability should the team use to train and select the best model?

A) Azure Machine Learning designer, to manually drag and drop algorithm components onto a canvas
B) Automated machine learning (AutoML), to automatically train and compare multiple models
C) Azure Machine Learning SDK v2, to write custom Python training scripts from scratch
D) Azure Machine Learning compute instances, to provision virtual machines for manual experimentation

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because automated machine learning (AutoML) automatically iterates through multiple algorithms and hyperparameter configurations, evaluates them against a primary metric, and recommends the best-performing model. It is designed for users who want to build high-quality models without extensive data science expertise, which matches the team's limited coding experience and need to minimize manual effort.
- **A is incorrect** because Azure Machine Learning designer provides a visual drag-and-drop interface for building pipelines, but it still requires the user to manually select and configure each algorithm. It does not automatically compare multiple algorithms to find the best one.
- **C is incorrect** because writing custom Python training scripts with the SDK requires significant programming and data science expertise, which the business analysts do not have.
- **D is incorrect** because compute instances are infrastructure resources (virtual machines) used to run notebooks and scripts. They are not a model training capability and do not automate algorithm selection.

**Reference:** [https://learn.microsoft.com/azure/machine-learning/concept-automated-ml?view=azureml-api-2](https://learn.microsoft.com/azure/machine-learning/concept-automated-ml?view=azureml-api-2)

</details>

---

### Item 4
**Objective:** Describe how training and validation datasets are used in machine learning
**Cognitive Level:** Apply

**Stem:**
A data scientist at Tailwind Traders is building a machine learning model to predict customer churn. She splits her labeled dataset into two subsets before training begins. She uses the first, larger subset to train the model and the second, smaller subset to evaluate model performance on data the model has never seen. She notices the model achieves 98% accuracy on the first subset but only 72% accuracy on the second subset.

What does this discrepancy most likely indicate, and which subsets is she using?

A) The model is underfitting; she is using a training dataset and a test dataset
B) The model is overfitting; she is using a training dataset and a validation dataset
C) The model performs well; the difference between training and validation accuracy is expected
D) The data is imbalanced; she should combine both subsets into a single training dataset

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because when a model performs significantly better on the data it was trained on (98%) than on a held-out evaluation subset (72%), it indicates overfitting -- the model has learned patterns specific to the training data that do not generalize well. The two subsets she created are the training dataset (used to teach the model) and the validation dataset (used to evaluate generalization).
- **A is incorrect** because underfitting occurs when a model fails to capture patterns even in the training data, resulting in poor performance on both subsets. Here, the training performance is very high (98%).
- **C is incorrect** because a 26-percentage-point gap between training and validation accuracy is a significant discrepancy that signals poor generalization, not expected behavior.
- **D is incorrect** because combining both subsets into training data would eliminate the ability to evaluate the model on unseen data and would not address the generalization problem. Data imbalance would not produce this specific pattern of high training accuracy with low validation accuracy.

**Reference:** [https://learn.microsoft.com/training/modules/fundamentals-machine-learning/2-what-is-machine-learning](https://learn.microsoft.com/training/modules/fundamentals-machine-learning/2-what-is-machine-learning)

</details>

---

### Item 5
**Objective:** Describe model management and deployment capabilities in Azure Machine Learning; Identify features of the Transformer architecture
**Cognitive Level:** Apply

**Stem:**
Adatum Corporation has used automated ML in Azure Machine Learning to train a natural language processing model that classifies customer support tickets by urgency level. The model is based on a Transformer architecture. The development team now needs to make this model available so that the company's helpdesk application can send a support ticket and receive an urgency classification in real time.

What should the team do to make the trained model available for real-time predictions?

A) Export the model as a CSV file and import it into the helpdesk application's database
B) Deploy the model to a real-time online endpoint in Azure Machine Learning
C) Schedule the model as a batch pipeline that runs every 24 hours
D) Retrain the model using Azure Machine Learning designer before any deployment is possible

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because Azure Machine Learning supports deploying trained models to managed online endpoints (real-time endpoints) that expose a REST API. The helpdesk application can send HTTP requests with support ticket text and receive urgency classification predictions in real time, which is exactly what the scenario requires.
- **A is incorrect** because a trained machine learning model cannot be meaningfully exported as a CSV file. CSV files store tabular data, not model logic or weights. This approach would not enable real-time predictions.
- **C is incorrect** because a batch pipeline processes data in bulk on a schedule and does not provide the immediate, per-request response that a real-time helpdesk application requires.
- **D is incorrect** because retraining with Azure Machine Learning designer is not a prerequisite for deployment. A model trained with automated ML can be deployed directly to an endpoint without rebuilding it in the designer.

**Reference:** [https://learn.microsoft.com/azure/machine-learning/how-to-deploy-automl-endpoint?view=azureml-api-2](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-automl-endpoint?view=azureml-api-2)

</details>

---
