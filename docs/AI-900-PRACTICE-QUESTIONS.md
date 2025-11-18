# 🎯 AI-900 Practice Questions by Segment

## Exam-Realistic Single Answer Multiple Choice Items

**Created:** November 2025
**Aligned with:** May 2, 2025 Exam Objectives
**Format:** 10 questions per segment × 4 segments = 40 total questions

---

## SEGMENT 1: Machine Learning on Azure (15-20%)

### Question 1

You are building a machine learning model to predict the number of units a product will sell next month based on historical sales data, advertising spend, and seasonal factors. Which type of machine learning technique should you use?

a. Classification
b. Regression
c. Clustering
d. Reinforcement learning

**Correct answer: b. Regression**

**Explanation:**
- **b. Regression (CORRECT)** - Regression predicts continuous numeric values. Predicting sales units (a number) is a classic regression problem.
  - Reference: [What is machine learning? - Regression](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#regression)

- **a. Classification (INCORRECT)** - Classification predicts categories or classes (e.g., spam/not spam, pass/fail), not continuous numbers.
  - Reference: [What is machine learning? - Classification](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#classification)

- **c. Clustering (INCORRECT)** - Clustering groups similar data points together without predefined labels. It doesn't predict specific values.
  - Reference: [What is machine learning? - Clustering](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#clustering)

- **d. Reinforcement learning (INCORRECT)** - Reinforcement learning trains agents to make decisions through trial and error with rewards/penalties, not for prediction tasks.
  - Reference: [Reinforcement learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-reinforcement-learning)

---

### Question 2

A healthcare organization needs to train a machine learning model to detect whether an X-ray image shows signs of pneumonia. They have 10,000 labeled X-ray images (5,000 with pneumonia, 5,000 without). What type of machine learning is this?

a. Unsupervised learning
b. Supervised learning
c. Semi-supervised learning
d. Reinforcement learning

**Correct answer: b. Supervised learning**

**Explanation:**
- **b. Supervised learning (CORRECT)** - This scenario uses labeled training data (images marked as pneumonia/no pneumonia) to train the model, which is the definition of supervised learning.
  - Reference: [Supervised learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#supervised-machine-learning)

- **a. Unsupervised learning (INCORRECT)** - Unsupervised learning works with unlabeled data to find patterns. This scenario has labeled images.
  - Reference: [Unsupervised learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#unsupervised-machine-learning)

- **c. Semi-supervised learning (INCORRECT)** - Semi-supervised uses a mix of labeled and unlabeled data. This scenario has fully labeled data.
  - Reference: [Machine learning fundamentals](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/)

- **d. Reinforcement learning (INCORRECT)** - Reinforcement learning learns through interaction with an environment and feedback, not from labeled datasets.
  - Reference: [Reinforcement learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-reinforcement-learning)

---

### Question 3

You are using Azure Machine Learning to train a classification model. After training, you notice the model performs extremely well on the training data (99% accuracy) but poorly on the test data (65% accuracy). What problem is your model experiencing?

a. Underfitting
b. Overfitting
c. Data imbalance
d. Feature scaling issues

**Correct answer: b. Overfitting**

**Explanation:**
- **b. Overfitting (CORRECT)** - When a model memorizes training data patterns (high training accuracy) but fails to generalize to new data (low test accuracy), it's overfitting.
  - Reference: [Prevent overfitting and imbalanced data](https://learn.microsoft.com/en-us/azure/machine-learning/concept-manage-ml-pitfalls)

- **a. Underfitting (INCORRECT)** - Underfitting occurs when a model performs poorly on both training and test data because it's too simple to capture patterns.
  - Reference: [Prevent overfitting and imbalanced data](https://learn.microsoft.com/en-us/azure/machine-learning/concept-manage-ml-pitfalls)

- **c. Data imbalance (INCORRECT)** - While data imbalance can cause problems, the symptom described (high training, low test accuracy) is specifically overfitting.
  - Reference: [Handle imbalanced data](https://learn.microsoft.com/en-us/azure/machine-learning/concept-manage-ml-pitfalls#handle-imbalanced-data)

- **d. Feature scaling issues (INCORRECT)** - Feature scaling affects model convergence and performance but wouldn't cause this specific training/test accuracy gap.
  - Reference: [Prepare data for machine learning](https://learn.microsoft.com/en-us/training/modules/introduction-to-data-for-machine-learning/)

---

### Question 4

Which Azure Machine Learning feature allows you to automatically try multiple algorithms and hyperparameters to find the best model for your dataset without writing code?

a. Azure Machine Learning designer
b. Automated Machine Learning (AutoML)
c. Azure Machine Learning notebooks
d. Azure Machine Learning pipelines

**Correct answer: b. Automated Machine Learning (AutoML)**

**Explanation:**
- **b. Automated Machine Learning (AutoML) (CORRECT)** - AutoML automatically trains and tunes multiple models to find the best one, requiring minimal configuration.
  - Reference: [What is automated machine learning?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml)

- **a. Azure Machine Learning designer (INCORRECT)** - Designer is a drag-and-drop tool for building ML pipelines, but you still choose algorithms manually.
  - Reference: [What is Azure Machine Learning designer?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer)

- **c. Azure Machine Learning notebooks (INCORRECT)** - Notebooks provide a code environment (Jupyter) where you write Python/R code; they don't automatically select algorithms.
  - Reference: [Run Jupyter notebooks in your workspace](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks)

- **d. Azure Machine Learning pipelines (INCORRECT)** - Pipelines automate ML workflows but don't automatically select and tune algorithms.
  - Reference: [What are Azure Machine Learning pipelines?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines)

---

### Question 5

In a machine learning dataset, what is a "feature"?

a. The value you want the model to predict
b. An input variable used to make predictions
c. A row in the dataset
d. The algorithm used for training

**Correct answer: b. An input variable used to make predictions**

**Explanation:**
- **b. An input variable used to make predictions (CORRECT)** - Features are the input columns/variables that the model uses to learn patterns and make predictions.
  - Reference: [Machine learning fundamentals - Features and labels](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/3-features-labels)

- **a. The value you want the model to predict (INCORRECT)** - This describes a "label" or "target variable," not a feature.
  - Reference: [Machine learning fundamentals - Features and labels](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/3-features-labels)

- **c. A row in the dataset (INCORRECT)** - A row represents a single observation or sample, not a feature. Features are columns.
  - Reference: [Prepare data for machine learning](https://learn.microsoft.com/en-us/training/modules/introduction-to-data-for-machine-learning/)

- **d. The algorithm used for training (INCORRECT)** - The algorithm is the mathematical approach used to learn from features, not the features themselves.
  - Reference: [Machine learning fundamentals](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/)

---

### Question 6

You need to group customers into segments based on their purchasing behavior without any predefined categories. Which machine learning technique should you use?

a. Classification
b. Regression
c. Clustering
d. Deep learning

**Correct answer: c. Clustering**

**Explanation:**
- **c. Clustering (CORRECT)** - Clustering is an unsupervised learning technique that groups similar data points without predefined labels, perfect for customer segmentation.
  - Reference: [What is automated ML? - Clustering](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#clustering)

- **a. Classification (INCORRECT)** - Classification requires predefined categories/labels. The scenario states there are no predefined categories.
  - Reference: [Classification models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#classification)

- **b. Regression (INCORRECT)** - Regression predicts continuous numeric values, not groups or segments.
  - Reference: [Regression models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#regression)

- **d. Deep learning (INCORRECT)** - Deep learning is a technique that can be used for various tasks but isn't specific to grouping without labels. Clustering is the appropriate approach.
  - Reference: [Deep learning vs machine learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-deep-learning-vs-machine-learning)

---

### Question 7

What is the purpose of splitting data into training, validation, and test datasets in machine learning?

a. To reduce storage costs by using smaller datasets
b. To ensure the model can generalize to new, unseen data
c. To speed up the training process
d. To meet regulatory compliance requirements

**Correct answer: b. To ensure the model can generalize to new, unseen data**

**Explanation:**
- **b. To ensure the model can generalize to new, unseen data (CORRECT)** - Data splitting allows you to train on one set, tune on validation, and test final performance on unseen data to verify generalization.
  - Reference: [Training and validation data](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/4-model-training-validation)

- **a. To reduce storage costs by using smaller datasets (INCORRECT)** - Data splitting doesn't reduce storage; you still store all the data. The purpose is validation, not cost reduction.
  - Reference: [Machine learning fundamentals](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/)

- **c. To speed up the training process (INCORRECT)** - Training on a subset might be faster, but that's not the purpose. In fact, proper validation can increase total time.
  - Reference: [Training and validation data](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/4-model-training-validation)

- **d. To meet regulatory compliance requirements (INCORRECT)** - While some regulations require model validation, data splitting is a fundamental ML practice for model quality, not primarily for compliance.
  - Reference: [Responsible AI principles](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)

---

### Question 8

Which deep learning technique is specifically designed to process and analyze image data using layers that detect visual features?

a. Recurrent Neural Networks (RNN)
b. Convolutional Neural Networks (CNN)
c. Transformer networks
d. Long Short-Term Memory (LSTM) networks

**Correct answer: b. Convolutional Neural Networks (CNN)**

**Explanation:**
- **b. Convolutional Neural Networks (CNN) (CORRECT)** - CNNs use convolutional layers to detect spatial patterns and features in images, making them ideal for computer vision tasks.
  - Reference: [Deep learning vs machine learning - CNNs](https://learn.microsoft.com/en-us/azure/machine-learning/concept-deep-learning-vs-machine-learning#convolutional-neural-networks)

- **a. Recurrent Neural Networks (RNN) (INCORRECT)** - RNNs process sequential data (time series, text) by maintaining memory of previous inputs, not specifically designed for images.
  - Reference: [Deep learning vs machine learning - RNNs](https://learn.microsoft.com/en-us/azure/machine-learning/concept-deep-learning-vs-machine-learning#recurrent-neural-networks)

- **c. Transformer networks (INCORRECT)** - Transformers use attention mechanisms and excel at NLP tasks. While vision transformers exist, CNNs are the traditional and most common choice for image processing.
  - Reference: [What is a transformer model?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-transformer-models)

- **d. Long Short-Term Memory (LSTM) networks (INCORRECT)** - LSTMs are a type of RNN for sequential data, not primarily for image analysis.
  - Reference: [Deep learning architectures](https://learn.microsoft.com/en-us/training/modules/introduction-to-deep-learning/)

---

### Question 9

You want to deploy a trained machine learning model as a web service so applications can send data and receive predictions in real-time. Which Azure Machine Learning capability should you use?

a. Azure Machine Learning dataset
b. Azure Machine Learning experiment
c. Azure Machine Learning endpoint
d. Azure Machine Learning compute cluster

**Correct answer: c. Azure Machine Learning endpoint**

**Explanation:**
- **c. Azure Machine Learning endpoint (CORRECT)** - Endpoints (managed or Kubernetes) host deployed models as web services that accept REST API requests for real-time predictions.
  - Reference: [Deploy machine learning models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints)

- **a. Azure Machine Learning dataset (INCORRECT)** - Datasets are data sources used for training and testing, not for deploying models.
  - Reference: [Work with data in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-data)

- **b. Azure Machine Learning experiment (INCORRECT)** - Experiments track training runs and model development, not deployment.
  - Reference: [Track experiments](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics)

- **d. Azure Machine Learning compute cluster (INCORRECT)** - Compute clusters provide processing power for training, not for hosting deployed models as web services.
  - Reference: [Azure Machine Learning compute targets](https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target)

---

### Question 10

What is a key characteristic of the Transformer architecture that has made it foundational for modern large language models like GPT?

a. It uses convolutional layers to process images
b. It processes sequences recursively one element at a time
c. It uses self-attention mechanisms to process entire sequences in parallel
d. It requires less training data than other approaches

**Correct answer: c. It uses self-attention mechanisms to process entire sequences in parallel**

**Explanation:**
- **c. It uses self-attention mechanisms to process entire sequences in parallel (CORRECT)** - Transformers use self-attention to weigh the importance of different parts of the input simultaneously, enabling parallel processing and capturing long-range dependencies.
  - Reference: [What is a transformer model?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-transformer-models)

- **a. It uses convolutional layers to process images (INCORRECT)** - Convolutional layers are characteristic of CNNs, not transformers. Transformers use attention mechanisms.
  - Reference: [Deep learning architectures](https://learn.microsoft.com/en-us/training/modules/introduction-to-deep-learning/)

- **b. It processes sequences recursively one element at a time (INCORRECT)** - This describes RNNs. Transformers process sequences in parallel, which is one of their key advantages.
  - Reference: [What is a transformer model?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-transformer-models)

- **d. It requires less training data than other approaches (INCORRECT)** - Transformers typically require large amounts of training data. Their advantage is in parallel processing and capturing long-range dependencies, not data efficiency.
  - Reference: [Transformer models overview](https://learn.microsoft.com/en-us/training/modules/introduction-to-generative-ai/)

---

## SEGMENT 2: Computer Vision on Azure (15-20%)

### Question 11

A retail company wants to automatically categorize product images into predefined categories such as "Electronics," "Clothing," "Home & Garden," and "Toys." Which type of computer vision solution should they implement?

a. Image classification
b. Object detection
c. Semantic segmentation
d. Facial recognition

**Correct answer: a. Image classification**

**Explanation:**
- **a. Image classification (CORRECT)** - Image classification assigns entire images to predefined categories, which exactly matches the requirement to categorize products.
  - Reference: [Image classification](https://learn.microsoft.com/en-us/training/modules/analyze-images/2-image-classification)

- **b. Object detection (INCORRECT)** - Object detection locates and identifies multiple objects within an image using bounding boxes, not categorizing the entire image.
  - Reference: [Object detection](https://learn.microsoft.com/en-us/training/modules/analyze-images/3-object-detection)

- **c. Semantic segmentation (INCORRECT)** - Semantic segmentation classifies individual pixels into categories, used for detailed scene understanding, not overall image categorization.
  - Reference: [Computer vision models](https://learn.microsoft.com/en-us/training/modules/analyze-images/)

- **d. Facial recognition (INCORRECT)** - Facial recognition identifies or verifies people based on faces, not relevant for product categorization.
  - Reference: [Face detection and analysis](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/)

---

### Question 12

You need to detect and locate multiple cars in a parking lot image, drawing bounding boxes around each vehicle and identifying their positions. Which computer vision technique should you use?

a. Image classification
b. Object detection
c. Optical character recognition
d. Facial analysis

**Correct answer: b. Object detection**

**Explanation:**
- **b. Object detection (CORRECT)** - Object detection identifies and localizes multiple objects (cars) within an image using bounding boxes with coordinates.
  - Reference: [Object detection](https://learn.microsoft.com/en-us/training/modules/analyze-images/3-object-detection)

- **a. Image classification (INCORRECT)** - Image classification only assigns a category to the whole image (e.g., "parking lot"), not locating individual objects.
  - Reference: [Image classification](https://learn.microsoft.com/en-us/training/modules/analyze-images/2-image-classification)

- **c. Optical character recognition (INCORRECT)** - OCR extracts text from images, not detecting objects like cars.
  - Reference: [Optical character recognition](https://learn.microsoft.com/en-us/training/modules/read-text-computer-vision/)

- **d. Facial analysis (INCORRECT)** - Facial analysis detects and analyzes faces, not vehicles.
  - Reference: [Face detection and analysis](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/)

---

### Question 13

A company needs to extract printed and handwritten text from scanned documents and images. Which Azure AI service capability should they use?

a. Azure AI Vision - Image Analysis
b. Azure AI Vision - Read API (OCR)
c. Azure AI Custom Vision
d. Azure AI Face

**Correct answer: b. Azure AI Vision - Read API (OCR)**

**Explanation:**
- **b. Azure AI Vision - Read API (OCR) (CORRECT)** - The Read API performs optical character recognition on both printed and handwritten text in images and PDFs.
  - Reference: [Read text from images with OCR](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-ocr)

- **a. Azure AI Vision - Image Analysis (INCORRECT)** - Image Analysis identifies objects, scenes, and activities in images but doesn't specifically extract text as its primary function.
  - Reference: [Image Analysis](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis)

- **c. Azure AI Custom Vision (INCORRECT)** - Custom Vision trains custom image classification and object detection models, not for text extraction.
  - Reference: [What is Custom Vision?](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)

- **d. Azure AI Face (INCORRECT)** - Azure AI Face detects and analyzes faces, not text.
  - Reference: [What is Azure AI Face?](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-identity)

---

### Question 14

You want to train a custom image classification model to identify specific types of defects in manufacturing parts. You have thousands of labeled images. Which Azure service should you use?

a. Azure AI Vision
b. Azure AI Custom Vision
c. Azure Machine Learning
d. Azure AI Face

**Correct answer: b. Azure AI Custom Vision**

**Explanation:**
- **b. Azure AI Custom Vision (CORRECT)** - Custom Vision is specifically designed to train custom image classification and object detection models with your own labeled images without requiring ML expertise.
  - Reference: [What is Custom Vision?](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)

- **a. Azure AI Vision (INCORRECT)** - Azure AI Vision provides pre-built computer vision capabilities but doesn't allow training custom models for specific scenarios.
  - Reference: [What is Azure AI Vision?](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview)

- **c. Azure Machine Learning (INCORRECT)** - While Azure ML can train custom models, Custom Vision is the purpose-built, simpler solution for custom image classification without requiring data science expertise.
  - Reference: [What is Azure Machine Learning?](https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning)

- **d. Azure AI Face (INCORRECT)** - Azure AI Face is specialized for facial detection and recognition, not general defect detection.
  - Reference: [What is Azure AI Face?](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-identity)

---

### Question 15

Which Azure AI Face service capability determines whether two face images belong to the same person?

a. Face detection
b. Face verification
c. Face identification
d. Face grouping

**Correct answer: b. Face verification**

**Explanation:**
- **b. Face verification (CORRECT)** - Face verification compares two faces to determine if they belong to the same person (1:1 matching).
  - Reference: [Face detection and verification](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/3-face-analysis)

- **a. Face detection (INCORRECT)** - Face detection locates faces in images and returns bounding boxes but doesn't compare faces for identity.
  - Reference: [Face detection](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-face-detection)

- **c. Face identification (INCORRECT)** - Face identification matches a face against a database of known faces (1:many matching), not comparing two specific faces.
  - Reference: [Face recognition](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/4-face-recognition)

- **d. Face grouping (INCORRECT)** - Face grouping organizes unknown faces into groups based on similarity, not verifying if two specific faces match.
  - Reference: [Face service concepts](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-face-recognition)

---

### Question 16

A security system needs to identify specific individuals from a database of 10,000 employees when they appear at building entrances. Which Azure AI Face capability should be used?

a. Face detection
b. Face verification
c. Face identification
d. Facial attribute analysis

**Correct answer: c. Face identification**

**Explanation:**
- **c. Face identification (CORRECT)** - Face identification performs 1:many matching to find a specific person within a database of known faces.
  - Reference: [Face recognition](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/4-face-recognition)

- **a. Face detection (INCORRECT)** - Face detection only locates faces in images; it doesn't identify who the person is.
  - Reference: [Face detection](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-face-detection)

- **b. Face verification (INCORRECT)** - Face verification checks if two faces are the same person (1:1), not searching a database.
  - Reference: [Face verification](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/3-face-analysis)

- **d. Facial attribute analysis (INCORRECT)** - Facial attribute analysis detects characteristics like age, emotion, glasses, etc., but doesn't identify individuals.
  - Reference: [Face detection and analysis](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/)

---

### Question 17

You are analyzing images and need to determine the dominant foreground and background colors, identify image categories (like "outdoor" or "people"), and detect brands and landmarks. Which Azure AI Vision feature provides this comprehensive analysis?

a. Custom Vision
b. Azure AI Vision - Image Analysis
c. Azure AI Vision - Read API
d. Azure AI Face

**Correct answer: b. Azure AI Vision - Image Analysis**

**Explanation:**
- **b. Azure AI Vision - Image Analysis (CORRECT)** - Image Analysis provides comprehensive image understanding including objects, tags, descriptions, colors, categories, brands, landmarks, and more.
  - Reference: [Image Analysis overview](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis)

- **a. Custom Vision (INCORRECT)** - Custom Vision trains domain-specific classification/detection models, not providing pre-built general image analysis.
  - Reference: [What is Custom Vision?](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)

- **c. Azure AI Vision - Read API (INCORRECT)** - Read API specializes in OCR text extraction, not general image content analysis.
  - Reference: [Read API overview](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-ocr)

- **d. Azure AI Face (INCORRECT)** - Azure AI Face only analyzes faces and facial attributes, not general image content.
  - Reference: [Face service overview](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-identity)

---

### Question 18

A document processing system needs to extract text from invoices, receipts, and forms while understanding the structure and relationships between fields (like invoice number, date, total amount). Which Azure service is most appropriate?

a. Azure AI Vision - Read API
b. Azure AI Document Intelligence
c. Azure AI Custom Vision
d. Azure AI Language

**Correct answer: b. Azure AI Document Intelligence**

**Explanation:**
- **b. Azure AI Document Intelligence (CORRECT)** - Document Intelligence (formerly Form Recognizer) extracts text and understands document structure, key-value pairs, and tables from forms and invoices.
  - Reference: [What is Azure AI Document Intelligence?](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview)

- **a. Azure AI Vision - Read API (INCORRECT)** - Read API extracts text but doesn't understand document structure or field relationships.
  - Reference: [Read API overview](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-ocr)

- **c. Azure AI Custom Vision (INCORRECT)** - Custom Vision trains image classification/detection models, not document understanding.
  - Reference: [Custom Vision overview](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)

- **d. Azure AI Language (INCORRECT)** - Azure AI Language processes natural language text but doesn't extract text from images or understand document layouts.
  - Reference: [What is Azure AI Language?](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)

---

### Question 19

You need to detect faces in images and analyze attributes such as age estimation, emotion, facial hair, and whether the person is wearing glasses. Which Azure service provides these capabilities?

a. Azure AI Vision - Image Analysis
b. Azure AI Custom Vision
c. Azure AI Face
d. Azure AI Video Indexer

**Correct answer: c. Azure AI Face**

**Explanation:**
- **c. Azure AI Face (CORRECT)** - Azure AI Face detects faces and analyzes facial attributes including age, emotion, accessories, hair, makeup, and more.
  - Reference: [Face detection and attributes](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-face-detection)

- **a. Azure AI Vision - Image Analysis (INCORRECT)** - Image Analysis can detect people in images but doesn't provide detailed facial attribute analysis.
  - Reference: [Image Analysis](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis)

- **b. Azure AI Custom Vision (INCORRECT)** - Custom Vision trains custom models for specific scenarios, not pre-built facial analysis.
  - Reference: [Custom Vision](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)

- **d. Azure AI Video Indexer (INCORRECT)** - Video Indexer analyzes video content including faces, but Azure AI Face is the dedicated service for facial attribute analysis in images.
  - Reference: [Video Indexer](https://learn.microsoft.com/en-us/azure/azure-video-indexer/video-indexer-overview)

---

### Question 20

Which capability is specifically provided by Custom Vision but NOT by the pre-built Azure AI Vision service?

a. Detecting common objects in images
b. Training models with your own labeled image dataset
c. Extracting text from images using OCR
d. Generating image descriptions and captions

**Correct answer: b. Training models with your own labeled image dataset**

**Explanation:**
- **b. Training models with your own labeled image dataset (CORRECT)** - Custom Vision allows you to train custom classification and object detection models using your own labeled images for domain-specific scenarios.
  - Reference: [Train a Custom Vision model](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/getting-started-build-a-classifier)

- **a. Detecting common objects in images (INCORRECT)** - Pre-built Azure AI Vision already detects common objects; this isn't unique to Custom Vision.
  - Reference: [Azure AI Vision capabilities](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview)

- **c. Extracting text from images using OCR (INCORRECT)** - OCR is provided by Azure AI Vision's Read API, not Custom Vision.
  - Reference: [OCR with Azure AI Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-ocr)

- **d. Generating image descriptions and captions (INCORRECT)** - Image captioning is a feature of Azure AI Vision, not Custom Vision.
  - Reference: [Image captions](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-describe-images-40)

---

## SEGMENT 3: Natural Language Processing on Azure (15-20%)

### Question 21

A customer service application needs to analyze customer feedback emails and determine whether each message expresses positive, negative, neutral, or mixed emotions. Which Azure AI Language feature should be used?

a. Key phrase extraction
b. Sentiment analysis
c. Entity recognition
d. Language detection

**Correct answer: b. Sentiment analysis**

**Explanation:**
- **b. Sentiment analysis (CORRECT)** - Sentiment analysis evaluates text and returns sentiment labels (positive, negative, neutral, mixed) with confidence scores.
  - Reference: [Sentiment analysis and opinion mining](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/overview)

- **a. Key phrase extraction (INCORRECT)** - Key phrase extraction identifies main topics and concepts in text, not emotional sentiment.
  - Reference: [Key phrase extraction](https://learn.microsoft.com/en-us/azure/ai-services/language-service/key-phrase-extraction/overview)

- **c. Entity recognition (INCORRECT)** - Entity recognition identifies and categorizes entities (people, places, organizations), not sentiment.
  - Reference: [Named entity recognition](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/overview)

- **d. Language detection (INCORRECT)** - Language detection identifies what language text is written in, not emotional content.
  - Reference: [Language detection](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-detection/overview)

---

### Question 22

You need to extract mentions of people, organizations, locations, dates, and quantities from news articles. Which Azure AI Language capability should you use?

a. Sentiment analysis
b. Key phrase extraction
c. Named entity recognition (NER)
d. Text translation

**Correct answer: c. Named entity recognition (NER)**

**Explanation:**
- **c. Named entity recognition (NER) (CORRECT)** - NER identifies and classifies named entities like persons, organizations, locations, dates, quantities, and more.
  - Reference: [Named entity recognition](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/overview)

- **a. Sentiment analysis (INCORRECT)** - Sentiment analysis determines emotional tone, not entity extraction.
  - Reference: [Sentiment analysis](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/overview)

- **b. Key phrase extraction (INCORRECT)** - Key phrase extraction identifies main topics but doesn't classify specific entity types like people or locations.
  - Reference: [Key phrase extraction](https://learn.microsoft.com/en-us/azure/ai-services/language-service/key-phrase-extraction/overview)

- **d. Text translation (INCORRECT)** - Translation converts text between languages, not extracting entities.
  - Reference: [Azure AI Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/translator-overview)

---

### Question 23

A multinational company receives customer support tickets in various languages. You need to automatically identify which language each ticket is written in before routing it to the appropriate support team. Which Azure AI Language feature should you use?

a. Azure AI Translator
b. Language detection
c. Named entity recognition
d. Custom text classification

**Correct answer: b. Language detection**

**Explanation:**
- **b. Language detection (CORRECT)** - Language detection identifies the language of input text, supporting over 100 languages.
  - Reference: [Language detection](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-detection/overview)

- **a. Azure AI Translator (INCORRECT)** - Translator translates text between languages but requires knowing the source language or auto-detecting it as part of translation, not as a standalone detection service.
  - Reference: [Azure AI Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/translator-overview)

- **c. Named entity recognition (INCORRECT)** - NER extracts entities from text but doesn't identify the language.
  - Reference: [Named entity recognition](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/overview)

- **d. Custom text classification (INCORRECT)** - Custom text classification categorizes text into custom categories you define, not language identification.
  - Reference: [Custom text classification](https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-text-classification/overview)

---

### Question 24

You are building a chatbot that needs to understand user intents (like "BookFlight," "CancelReservation," "CheckWeather") and extract relevant entities (like dates, locations, names) from conversational input. Which Azure service should you use?

a. Azure AI Language - Sentiment Analysis
b. Azure AI Language - Key Phrase Extraction
c. Conversational Language Understanding (CLU)
d. Custom Question Answering

**Correct answer: c. Conversational Language Understanding (CLU)**

**Explanation:**
- **c. Conversational Language Understanding (CLU) (CORRECT)** - CLU (formerly LUIS) is designed to extract intents and entities from conversational user input for chatbots and virtual assistants.
  - Reference: [Conversational Language Understanding](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

- **a. Azure AI Language - Sentiment Analysis (INCORRECT)** - Sentiment analysis determines emotional tone, not intents and entities.
  - Reference: [Sentiment analysis](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/overview)

- **b. Azure AI Language - Key Phrase Extraction (INCORRECT)** - Key phrase extraction identifies main topics but isn't designed for intent classification and entity extraction in conversations.
  - Reference: [Key phrase extraction](https://learn.microsoft.com/en-us/azure/ai-services/language-service/key-phrase-extraction/overview)

- **d. Custom Question Answering (INCORRECT)** - Custom Question Answering creates FAQ-style Q&A systems, not intent/entity extraction for conversations.
  - Reference: [Custom question answering](https://learn.microsoft.com/en-us/azure/ai-services/language-service/question-answering/overview)

---

### Question 25

A company wants to create a knowledge base from their existing FAQ documentation and website content that can automatically answer customer questions. Which Azure service should they use?

a. Conversational Language Understanding (CLU)
b. Custom Question Answering
c. Azure AI Language - Sentiment Analysis
d. Azure OpenAI Service

**Correct answer: b. Custom Question Answering**

**Explanation:**
- **b. Custom Question Answering (CORRECT)** - Custom Question Answering (formerly QnA Maker) builds knowledge bases from FAQs, documents, and URLs to provide automatic answers to questions.
  - Reference: [Custom question answering](https://learn.microsoft.com/en-us/azure/ai-services/language-service/question-answering/overview)

- **a. Conversational Language Understanding (CLU) (INCORRECT)** - CLU extracts intents and entities from conversational input, not providing answers from a knowledge base.
  - Reference: [Conversational Language Understanding](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

- **c. Azure AI Language - Sentiment Analysis (INCORRECT)** - Sentiment analysis determines emotional tone, not answering questions.
  - Reference: [Sentiment analysis](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/overview)

- **d. Azure OpenAI Service (INCORRECT)** - While Azure OpenAI can answer questions, Custom Question Answering is specifically designed for FAQ scenarios and is simpler to set up with existing documentation.
  - Reference: [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

---

### Question 26

Which Azure service converts spoken audio into written text (speech-to-text)?

a. Azure AI Language
b. Azure AI Speech
c. Azure AI Translator
d. Azure OpenAI Service

**Correct answer: b. Azure AI Speech**

**Explanation:**
- **b. Azure AI Speech (CORRECT)** - Azure AI Speech provides speech-to-text, text-to-speech, speech translation, and speaker recognition capabilities.
  - Reference: [What is Azure AI Speech?](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview)

- **a. Azure AI Language (INCORRECT)** - Azure AI Language processes written text for NLP tasks, not audio conversion.
  - Reference: [Azure AI Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)

- **c. Azure AI Translator (INCORRECT)** - Translator converts text between languages, not speech to text.
  - Reference: [Azure AI Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/translator-overview)

- **d. Azure OpenAI Service (INCORRECT)** - Azure OpenAI includes Whisper for speech transcription, but Azure AI Speech is the dedicated service for speech-to-text.
  - Reference: [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

---

### Question 27

You need to convert written text into natural-sounding spoken audio in multiple languages and voices. Which Azure AI Speech capability should you use?

a. Speech recognition
b. Speech synthesis (text-to-speech)
c. Speech translation
d. Speaker recognition

**Correct answer: b. Speech synthesis (text-to-speech)**

**Explanation:**
- **b. Speech synthesis (text-to-speech) (CORRECT)** - Speech synthesis converts written text into spoken audio with various voices, languages, and speaking styles.
  - Reference: [Text-to-speech overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech)

- **a. Speech recognition (INCORRECT)** - Speech recognition converts spoken audio to text (speech-to-text), the opposite direction.
  - Reference: [Speech-to-text overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text)

- **c. Speech translation (INCORRECT)** - Speech translation translates spoken audio from one language to another, not converting text to speech.
  - Reference: [Speech translation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-translation)

- **d. Speaker recognition (INCORRECT)** - Speaker recognition identifies or verifies speakers based on their voice characteristics, not generating speech from text.
  - Reference: [Speaker recognition](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speaker-recognition-overview)

---

### Question 28

A company needs to translate customer emails written in various languages into English for their support team. Which Azure service should they use?

a. Azure AI Language
b. Azure AI Speech
c. Azure AI Translator
d. Conversational Language Understanding

**Correct answer: c. Azure AI Translator**

**Explanation:**
- **c. Azure AI Translator (CORRECT)** - Azure AI Translator provides text translation between over 100 languages, perfect for translating written communications.
  - Reference: [What is Azure AI Translator?](https://learn.microsoft.com/en-us/azure/ai-services/translator/translator-overview)

- **a. Azure AI Language (INCORRECT)** - Azure AI Language analyzes text (sentiment, entities, key phrases) but doesn't translate between languages.
  - Reference: [Azure AI Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)

- **b. Azure AI Speech (INCORRECT)** - Azure AI Speech handles audio translation, not written text translation.
  - Reference: [Azure AI Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview)

- **d. Conversational Language Understanding (INCORRECT)** - CLU extracts intents and entities from conversational input, not translation.
  - Reference: [CLU overview](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

---

### Question 29

You want to identify and redact personally identifiable information (PII) such as social security numbers, phone numbers, and email addresses from customer support transcripts. Which Azure AI Language feature should you use?

a. Sentiment analysis
b. Key phrase extraction
c. Named entity recognition (NER) with PII detection
d. Language detection

**Correct answer: c. Named entity recognition (NER) with PII detection**

**Explanation:**
- **c. Named entity recognition (NER) with PII detection (CORRECT)** - NER includes PII entity recognition that identifies and can redact sensitive personal information.
  - Reference: [Named entity recognition with PII detection](https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/overview)

- **a. Sentiment analysis (INCORRECT)** - Sentiment analysis determines emotional tone, not identifying PII.
  - Reference: [Sentiment analysis](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/overview)

- **b. Key phrase extraction (INCORRECT)** - Key phrase extraction identifies main topics, not specifically PII entities.
  - Reference: [Key phrase extraction](https://learn.microsoft.com/en-us/azure/ai-services/language-service/key-phrase-extraction/overview)

- **d. Language detection (INCORRECT)** - Language detection identifies what language text is written in, not PII entities.
  - Reference: [Language detection](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-detection/overview)

---

### Question 30

What is the main difference between Conversational Language Understanding (CLU) and Custom Question Answering?

a. CLU is for chatbots, Custom QA is for sentiment analysis
b. CLU extracts intents/entities from conversations, Custom QA provides answers from a knowledge base
c. CLU translates languages, Custom QA detects entities
d. CLU is for speech, Custom QA is for text

**Correct answer: b. CLU extracts intents/entities from conversations, Custom QA provides answers from a knowledge base**

**Explanation:**
- **b. CLU extracts intents/entities from conversations, Custom QA provides answers from a knowledge base (CORRECT)** - CLU understands what users want to do and extracts information from their requests, while Custom QA matches questions to pre-defined answers.
  - Reference: [CLU vs Custom QA comparison](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview#available-features)

- **a. CLU is for chatbots, Custom QA is for sentiment analysis (INCORRECT)** - Both are for chatbots; Custom QA is for Q&A, not sentiment analysis.
  - Reference: [Language service features](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)

- **c. CLU translates languages, Custom QA detects entities (INCORRECT)** - Neither translates; CLU detects entities and intents, Custom QA provides answers.
  - Reference: [Conversational Language Understanding](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

- **d. CLU is for speech, Custom QA is for text (INCORRECT)** - Both work with text input (though CLU can be used with speech-to-text output).
  - Reference: [Question answering](https://learn.microsoft.com/en-us/azure/ai-services/language-service/question-answering/overview)

---

## SEGMENT 4: Generative AI & Azure OpenAI (20-25%)

### Question 31

What is Azure AI Foundry?

a. A replacement for Azure Machine Learning
b. A unified platform for building AI applications with access to a model catalog of 1,600+ models
c. A service exclusively for Azure OpenAI models
d. A tool for hardware acceleration of AI training

**Correct answer: b. A unified platform for building AI applications with access to a model catalog of 1,600+ models**

**Explanation:**
- **b. A unified platform for building AI applications with access to a model catalog of 1,600+ models (CORRECT)** - Azure AI Foundry (formerly Azure AI Studio) provides a unified development experience with access to models from Microsoft, OpenAI, Meta, Hugging Face, and other providers.
  - Reference: [What is Azure AI Foundry?](https://learn.microsoft.com/en-us/azure/ai-studio/what-is-ai-studio)

- **a. A replacement for Azure Machine Learning (INCORRECT)** - Azure AI Foundry complements and integrates with Azure ML rather than replacing it.
  - Reference: [Azure AI Foundry overview](https://learn.microsoft.com/en-us/azure/ai-studio/what-is-ai-studio)

- **c. A service exclusively for Azure OpenAI models (INCORRECT)** - It includes Azure OpenAI but also provides access to many other model families and providers.
  - Reference: [Model catalog in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/model-catalog)

- **d. A tool for hardware acceleration of AI training (INCORRECT)** - It's a development platform, not hardware acceleration.
  - Reference: [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/)

---

### Question 32

Which Azure OpenAI model family is specifically designed for generating images from text descriptions?

a. GPT-4
b. GPT-3.5-Turbo
c. DALL-E
d. Text-Embedding-Ada

**Correct answer: c. DALL-E**

**Explanation:**
- **c. DALL-E (CORRECT)** - DALL-E 2 and DALL-E 3 are image generation models that create images from natural language descriptions.
  - Reference: [Azure OpenAI DALL-E](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#dall-e-models)

- **a. GPT-4 (INCORRECT)** - GPT-4 is a large language model for text generation and understanding, not image generation.
  - Reference: [GPT-4 and GPT-4 Turbo models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#gpt-4-models)

- **b. GPT-3.5-Turbo (INCORRECT)** - GPT-3.5-Turbo is a text generation model, not for images.
  - Reference: [GPT-3.5 models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#gpt-35-models)

- **d. Text-Embedding-Ada (INCORRECT)** - Embedding models convert text into numerical vectors for similarity search and retrieval, not image generation.
  - Reference: [Embeddings](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings)

---

### Question 33

In prompt engineering, what is the purpose of "few-shot learning"?

a. Training a new model with minimal data
b. Providing examples of desired input-output pairs in the prompt
c. Reducing the token count in responses
d. Limiting the model's creativity

**Correct answer: b. Providing examples of desired input-output pairs in the prompt**

**Explanation:**
- **b. Providing examples of desired input-output pairs in the prompt (CORRECT)** - Few-shot learning involves including example questions and answers in your prompt to guide the model's response format and behavior.
  - Reference: [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)

- **a. Training a new model with minimal data (INCORRECT)** - Few-shot learning in prompting doesn't retrain the model; it provides examples in the prompt itself.
  - Reference: [Prompt engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)

- **c. Reducing the token count in responses (INCORRECT)** - Token reduction is controlled by max_tokens parameter, not few-shot learning.
  - Reference: [Completion parameters](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/completions)

- **d. Limiting the model's creativity (INCORRECT)** - Creativity is controlled by temperature parameter, not few-shot learning.
  - Reference: [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)

---

### Question 34

Which parameter in Azure OpenAI controls the randomness and creativity of model outputs, with 0 being deterministic and 1 being highly creative?

a. max_tokens
b. top_p
c. temperature
d. frequency_penalty

**Correct answer: c. temperature**

**Explanation:**
- **c. temperature (CORRECT)** - Temperature (range 0-1) controls randomness: lower values make output more focused and deterministic, higher values make it more random and creative.
  - Reference: [Completion parameters - Temperature](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/completions#temperature)

- **a. max_tokens (INCORRECT)** - max_tokens limits the length of the response, not its creativity.
  - Reference: [Completion parameters](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/completions)

- **b. top_p (INCORRECT)** - top_p (nucleus sampling) controls diversity by considering tokens with cumulative probability, but temperature is the primary creativity control.
  - Reference: [Advanced completion parameters](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/completions)

- **d. frequency_penalty (INCORRECT)** - frequency_penalty reduces repetition of tokens, not controlling creativity.
  - Reference: [Completion parameters](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/completions)

---

### Question 35

What is "grounding" in the context of generative AI?

a. Restricting the model's access to the internet
b. Connecting the model's responses to specific, verified source data
c. Training the model on your own dataset
d. Limiting token usage to reduce costs

**Correct answer: b. Connecting the model's responses to specific, verified source data**

**Explanation:**
- **b. Connecting the model's responses to specific, verified source data (CORRECT)** - Grounding provides the model with relevant factual information from trusted sources to improve accuracy and reduce hallucinations.
  - Reference: [Grounding data for Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)

- **a. Restricting the model's access to the internet (INCORRECT)** - Azure OpenAI models don't access the internet; grounding is about providing specific data sources.
  - Reference: [Azure OpenAI on your data](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)

- **c. Training the model on your own dataset (INCORRECT)** - Grounding provides data at inference time via prompts; it's not model training (fine-tuning).
  - Reference: [Use your data with Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)

- **d. Limiting token usage to reduce costs (INCORRECT)** - Cost management is separate from grounding, which focuses on accuracy.
  - Reference: [Azure OpenAI best practices](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)

---

### Question 36

What is RAG (Retrieval-Augmented Generation) in generative AI?

a. A technique that retrieves relevant information from external data sources before generating responses
b. A method to train models faster
c. A way to reduce model size
d. A content filtering mechanism

**Correct answer: a. A technique that retrieves relevant information from external data sources before generating responses**

**Explanation:**
- **a. A technique that retrieves relevant information from external data sources before generating responses (CORRECT)** - RAG combines information retrieval with generation, searching external data and using retrieved content to inform the model's response.
  - Reference: [Azure OpenAI on your data (RAG)](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)

- **b. A method to train models faster (INCORRECT)** - RAG is an inference-time technique, not a training optimization.
  - Reference: [Retrieval Augmented Generation](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)

- **c. A way to reduce model size (INCORRECT)** - RAG enhances model capability without changing model size.
  - Reference: [Azure OpenAI on your data](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)

- **d. A content filtering mechanism (INCORRECT)** - Content filtering is a separate safety feature, not RAG.
  - Reference: [Content filtering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter)

---

### Question 37

Which responsible AI consideration is specifically important for generative AI models that is less relevant to traditional AI models?

a. Data privacy
b. Hallucinations (generating false information)
c. Model training time
d. Hardware requirements

**Correct answer: b. Hallucinations (generating false information)**

**Explanation:**
- **b. Hallucinations (generating false information) (CORRECT)** - Generative models can confidently produce plausible-sounding but factually incorrect information, a unique challenge requiring mitigation strategies.
  - Reference: [Azure OpenAI responsible AI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter)

- **a. Data privacy (INCORRECT)** - Data privacy is important for all AI models, not unique to generative AI.
  - Reference: [Responsible AI principles](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)

- **c. Model training time (INCORRECT)** - Training time is a technical consideration, not a responsible AI concern.
  - Reference: [Azure OpenAI overview](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

- **d. Hardware requirements (INCORRECT)** - Hardware is a technical requirement, not a responsible AI consideration.
  - Reference: [Responsible AI with Azure OpenAI](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/transparency-note)

---

### Question 38

Azure OpenAI Service includes content filters to detect and prevent harmful content. Which of the following is NOT a default content filter category?

a. Hate and fairness
b. Sexual content
c. Copyright infringement
d. Violence

**Correct answer: c. Copyright infringement**

**Explanation:**
- **c. Copyright infringement (CORRECT - This is NOT a default category)** - Default content filters cover hate, sexual, violence, and self-harm categories, but copyright detection is not a standard content filter category.
  - Reference: [Content filtering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter)

- **a. Hate and fairness (INCORRECT - This IS a category)** - Hate speech and fairness is one of the core filter categories.
  - Reference: [Content filtering categories](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter)

- **b. Sexual content (INCORRECT - This IS a category)** - Sexual content is filtered at various severity levels.
  - Reference: [Content filtering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter)

- **d. Violence (INCORRECT - This IS a category)** - Violence is one of the core content filter categories.
  - Reference: [Content filtering categories](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter)

---

### Question 39

What are "tokens" in the context of Azure OpenAI models?

a. Security credentials for API authentication
b. Chunks of text that the model processes, with both input and output measured in tokens
c. Individual letters in the input text
d. Database records used for training

**Correct answer: b. Chunks of text that the model processes, with both input and output measured in tokens**

**Explanation:**
- **b. Chunks of text that the model processes, with both input and output measured in tokens (CORRECT)** - Tokens are pieces of words (roughly 4 characters in English); models process text as tokens, and pricing/limits are based on token count.
  - Reference: [Understanding tokens](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview#tokens)

- **a. Security credentials for API authentication (INCORRECT)** - API keys/credentials are separate from text tokens.
  - Reference: [Azure OpenAI authentication](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/authentication)

- **c. Individual letters in the input text (INCORRECT)** - Tokens are larger than individual characters, typically representing word parts.
  - Reference: [Tokens and tokenization](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview#tokens)

- **d. Database records used for training (INCORRECT)** - Tokens refer to text processing units, not training data.
  - Reference: [Understanding tokens](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview#tokens)

---

### Question 40

In Azure OpenAI, what is the purpose of a "system message" in a chat completion request?

a. To monitor system performance and errors
b. To provide instructions that guide the model's behavior and persona throughout the conversation
c. To authenticate the API request
d. To specify the model version to use

**Correct answer: b. To provide instructions that guide the model's behavior and persona throughout the conversation**

**Explanation:**
- **b. To provide instructions that guide the model's behavior and persona throughout the conversation (CORRECT)** - System messages set the assistant's behavior, tone, and constraints, influencing all subsequent responses.
  - Reference: [Chat completions - System message](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/chatgpt#use-system-messages)

- **a. To monitor system performance and errors (INCORRECT)** - System messages are part of the prompt, not monitoring infrastructure.
  - Reference: [Chat completions](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/chatgpt)

- **c. To authenticate the API request (INCORRECT)** - Authentication uses API keys, not system messages.
  - Reference: [Authentication](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/authentication)

- **d. To specify the model version to use (INCORRECT)** - Model selection is specified in the API endpoint or deployment parameter, not system messages.
  - Reference: [Chat completion API](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)

---

## 📊 Practice Questions Summary

**Total Questions:** 40 (10 per segment)

**Segment Breakdown:**
- Machine Learning on Azure: Questions 1-10
- Computer Vision: Questions 11-20
- Natural Language Processing: Questions 21-30
- Generative AI & Azure OpenAI: Questions 31-40

**Study Tips:**
1. Review incorrect answers and read the Microsoft Learn references
2. Understand WHY incorrect answers are wrong, not just memorizing correct answers
3. Focus extra time on Generative AI (20-25% of exam - highest weight)
4. Practice explaining concepts in your own words
5. Take timed practice tests to build exam stamina

**Next Steps:**
- Complete these questions untimed first to learn concepts
- Retry questions you missed after studying the reference links
- Take a full timed practice test (45 minutes for 40 questions)
- Review the [PRACTICE-QUESTIONS-GUIDE.md](./PRACTICE-QUESTIONS-GUIDE.md) for additional resources

---

*Created for AI-900 Exam Preparation | Updated: November 2025*
*All Microsoft Learn references verified as of November 2025*
