# AI-900 Practice Questions - Set 2

## Exam-Realistic Single Answer Multiple Choice Items

**Created:** November 2025
**Aligned with:** May 2, 2025 Exam Objectives
**Format:** 5 questions per segment x 4 segments = 20 total questions

---

## SEGMENT 1: Machine Learning on Azure (15-20%)

### Question 41

A bank wants to predict whether a loan applicant will default on their loan based on credit score, income, employment history, and existing debt. What type of machine learning should they use?

a. Regression
b. Binary classification
c. Multi-class classification
d. Clustering

**Correct answer: b. Binary classification**

**Explanation:**
- **b. Binary classification (CORRECT)** - Predicting one of two outcomes (default/no default) is binary classification. The model learns from labeled historical data to classify new applicants.
  - Reference: [Classification in machine learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#classification)

- **a. Regression (INCORRECT)** - Regression predicts continuous numeric values (like loan amount), not categorical outcomes like yes/no decisions.
  - Reference: [Regression models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#regression)

- **c. Multi-class classification (INCORRECT)** - Multi-class predicts among three or more categories. This scenario has only two outcomes (default or not).
  - Reference: [Multi-class classification](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/)

- **d. Clustering (INCORRECT)** - Clustering groups similar data without predefined labels; this scenario requires predicting a specific outcome using labeled data.
  - Reference: [Clustering models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml#clustering)

---

### Question 42

Which evaluation metric is most appropriate for a classification model where you need to minimize false negatives, such as detecting fraudulent transactions?

a. Accuracy
b. Precision
c. Recall
d. F1 Score

**Correct answer: c. Recall**

**Explanation:**
- **c. Recall (CORRECT)** - Recall measures the proportion of actual positives correctly identified. High recall minimizes false negatives, crucial when missing a fraud case is costly.
  - Reference: [Evaluate classification models](https://learn.microsoft.com/en-us/training/modules/evaluate-classification-model/)

- **a. Accuracy (INCORRECT)** - Accuracy measures overall correct predictions but can be misleading with imbalanced datasets (most transactions aren't fraud).
  - Reference: [Classification metrics](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-understand-automated-ml#classification-metrics)

- **b. Precision (INCORRECT)** - Precision measures accuracy of positive predictions, minimizing false positives. For fraud, missing fraud (false negatives) is worse than investigating non-fraud (false positives).
  - Reference: [Precision and recall](https://learn.microsoft.com/en-us/training/modules/evaluate-classification-model/)

- **d. F1 Score (INCORRECT)** - F1 balances precision and recall. When specifically prioritizing catching all fraud cases, recall is the better choice.
  - Reference: [F1 Score](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-understand-automated-ml#classification-metrics)

---

### Question 43

What is the purpose of the validation dataset in machine learning model development?

a. To train the model on additional data
b. To tune hyperparameters and prevent overfitting during training
c. To provide the final performance evaluation after all development is complete
d. To clean and preprocess the data

**Correct answer: b. To tune hyperparameters and prevent overfitting during training**

**Explanation:**
- **b. To tune hyperparameters and prevent overfitting during training (CORRECT)** - The validation set is used during development to tune model parameters and make decisions about model configuration without touching the test set.
  - Reference: [Training, validation, and test data](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/4-model-training-validation)

- **a. To train the model on additional data (INCORRECT)** - The training set is used for model training, not the validation set.
  - Reference: [Data splits in machine learning](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/)

- **c. To provide the final performance evaluation after all development is complete (INCORRECT)** - This describes the test set, which is held out until final evaluation.
  - Reference: [Test data](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/4-model-training-validation)

- **d. To clean and preprocess the data (INCORRECT)** - Data preprocessing happens before splitting into train/validation/test sets.
  - Reference: [Prepare data](https://learn.microsoft.com/en-us/training/modules/introduction-to-data-for-machine-learning/)

---

### Question 44

In Azure Machine Learning, what is a compute instance?

a. A cluster of virtual machines for distributed training
b. A managed cloud-based workstation for data science
c. A container for deploying models as web services
d. A storage account for datasets

**Correct answer: b. A managed cloud-based workstation for data science**

**Explanation:**
- **b. A managed cloud-based workstation for data science (CORRECT)** - A compute instance is a fully configured, managed development environment in the cloud for notebooks and experimentation.
  - Reference: [What is a compute instance?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-instance)

- **a. A cluster of virtual machines for distributed training (INCORRECT)** - This describes a compute cluster, which is different from a compute instance.
  - Reference: [Compute clusters](https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target#azure-machine-learning-compute-managed)

- **c. A container for deploying models as web services (INCORRECT)** - Model deployment uses endpoints (managed online endpoints or Kubernetes), not compute instances.
  - Reference: [Deploy models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints)

- **d. A storage account for datasets (INCORRECT)** - Data storage uses Azure Storage or datastores, not compute instances.
  - Reference: [Work with data](https://learn.microsoft.com/en-us/azure/machine-learning/concept-data)

---

### Question 45

Which Azure Machine Learning feature allows you to track experiments, log metrics, and compare different model runs?

a. Azure Machine Learning pipelines
b. Azure Machine Learning experiments and MLflow
c. Azure Machine Learning datasets
d. Azure Machine Learning endpoints

**Correct answer: b. Azure Machine Learning experiments and MLflow**

**Explanation:**
- **b. Azure Machine Learning experiments and MLflow (CORRECT)** - Experiments track runs with logged metrics, parameters, and outputs. MLflow integration provides comprehensive experiment tracking and model management.
  - Reference: [Track ML experiments with MLflow](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow)

- **a. Azure Machine Learning pipelines (INCORRECT)** - Pipelines automate ML workflows but aren't specifically for experiment tracking and comparison.
  - Reference: [ML pipelines](https://learn.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines)

- **c. Azure Machine Learning datasets (INCORRECT)** - Datasets manage data assets but don't track experiments or metrics.
  - Reference: [Datasets](https://learn.microsoft.com/en-us/azure/machine-learning/concept-data)

- **d. Azure Machine Learning endpoints (INCORRECT)** - Endpoints host deployed models for inference, not experiment tracking.
  - Reference: [Endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints)

---

## SEGMENT 2: Computer Vision on Azure (15-20%)

### Question 46

A warehouse wants to identify specific products on shelves and count their quantities. They need to locate each product's position with bounding boxes and identify what product it is. Which Custom Vision project type should they use?

a. Image Classification (Multiclass)
b. Image Classification (Multilabel)
c. Object Detection
d. Image Segmentation

**Correct answer: c. Object Detection**

**Explanation:**
- **c. Object Detection (CORRECT)** - Object detection identifies and locates multiple objects in images with bounding boxes, including their class and position coordinates.
  - Reference: [Object detection with Custom Vision](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/get-started-build-detector)

- **a. Image Classification (Multiclass) (INCORRECT)** - Multiclass classification assigns one label to the entire image, not locating individual products.
  - Reference: [Image classification](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/getting-started-build-a-classifier)

- **b. Image Classification (Multilabel) (INCORRECT)** - Multilabel assigns multiple labels to an image but doesn't provide locations or counts.
  - Reference: [Custom Vision classification](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)

- **d. Image Segmentation (INCORRECT)** - Semantic segmentation classifies pixels but isn't a Custom Vision project type; it's available in other services.
  - Reference: [Custom Vision capabilities](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)

---

### Question 47

Which Azure AI Vision Image Analysis 4.0 feature can generate human-readable descriptions of image content, including dense captions for multiple objects?

a. Object detection
b. Image captioning
c. Background removal
d. Spatial analysis

**Correct answer: b. Image captioning**

**Explanation:**
- **b. Image captioning (CORRECT)** - Image Analysis 4.0 includes captioning that generates natural language descriptions, with dense captions providing descriptions for multiple detected regions.
  - Reference: [Image captions](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-describe-images-40)

- **a. Object detection (INCORRECT)** - Object detection returns object labels and bounding boxes, not human-readable descriptions.
  - Reference: [Object detection](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-object-detection-40)

- **c. Background removal (INCORRECT)** - Background removal segments foreground from background but doesn't generate descriptions.
  - Reference: [Background removal](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-background-removal)

- **d. Spatial analysis (INCORRECT)** - Spatial analysis tracks people movement in video, not image description generation.
  - Reference: [Spatial analysis](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/intro-to-spatial-analysis-public-preview)

---

### Question 48

A company needs to process thousands of multi-page PDF documents to extract text, including complex tables and handwritten signatures. Which Azure service is best suited for this task?

a. Azure AI Vision Read API
b. Azure AI Document Intelligence
c. Azure AI Custom Vision
d. Azure AI Language

**Correct answer: b. Azure AI Document Intelligence**

**Explanation:**
- **b. Azure AI Document Intelligence (CORRECT)** - Document Intelligence excels at processing complex documents with tables, forms, and handwriting while understanding document structure.
  - Reference: [Azure AI Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview)

- **a. Azure AI Vision Read API (INCORRECT)** - Read API extracts text but doesn't understand complex document structures like tables as well as Document Intelligence.
  - Reference: [Read API](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-ocr)

- **c. Azure AI Custom Vision (INCORRECT)** - Custom Vision trains image classification/detection models, not document text extraction.
  - Reference: [Custom Vision](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)

- **d. Azure AI Language (INCORRECT)** - Language processes text but doesn't extract it from images or PDFs.
  - Reference: [Azure AI Language](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)

---

### Question 49

Azure AI Video Indexer can extract insights from videos. Which of the following is NOT a capability of Video Indexer?

a. Transcribing spoken content
b. Detecting and recognizing faces
c. Training custom object detection models
d. Identifying topics and keywords

**Correct answer: c. Training custom object detection models**

**Explanation:**
- **c. Training custom object detection models (CORRECT - NOT a capability)** - Video Indexer uses pre-built models for video analysis; training custom object detection requires Custom Vision or Azure ML.
  - Reference: [Video Indexer overview](https://learn.microsoft.com/en-us/azure/azure-video-indexer/video-indexer-overview)

- **a. Transcribing spoken content (INCORRECT - IS a capability)** - Video Indexer includes automatic speech recognition for transcription.
  - Reference: [Video Indexer features](https://learn.microsoft.com/en-us/azure/azure-video-indexer/video-indexer-overview#features)

- **b. Detecting and recognizing faces (INCORRECT - IS a capability)** - Video Indexer can detect faces and recognize known individuals.
  - Reference: [Face detection in Video Indexer](https://learn.microsoft.com/en-us/azure/azure-video-indexer/video-indexer-overview)

- **d. Identifying topics and keywords (INCORRECT - IS a capability)** - Video Indexer extracts topics, keywords, and other semantic insights.
  - Reference: [Video Indexer insights](https://learn.microsoft.com/en-us/azure/azure-video-indexer/video-indexer-overview)

---

### Question 50

When training a Custom Vision model, what is the minimum recommended number of images per tag for good model performance?

a. 5 images
b. 15 images
c. 50 images
d. 500 images

**Correct answer: c. 50 images**

**Explanation:**
- **c. 50 images (CORRECT)** - Microsoft recommends at least 50 images per tag for good performance, with more images improving accuracy. The minimum is 5, but 50+ provides better results.
  - Reference: [How to improve your Custom Vision model](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/getting-started-improving-your-classifier)

- **a. 5 images (INCORRECT)** - 5 is the absolute minimum to create a tag, but it's insufficient for good model performance.
  - Reference: [Custom Vision limits](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/limits-and-quotas)

- **b. 15 images (INCORRECT)** - 15 images is better than minimum but still below the recommended threshold for reliable predictions.
  - Reference: [Improve your classifier](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/getting-started-improving-your-classifier)

- **d. 500 images (INCORRECT)** - While more images improve performance, 50 is the recommended baseline; 500 is not required.
  - Reference: [Training best practices](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/getting-started-improving-your-classifier)

---

## SEGMENT 3: Natural Language Processing on Azure (15-20%)

### Question 51

A legal firm wants to classify incoming documents into categories like "Contract," "Invoice," "Legal Brief," and "Correspondence" using their own classification scheme. Which Azure AI Language feature should they use?

a. Named entity recognition
b. Pre-built text classification
c. Custom text classification
d. Sentiment analysis

**Correct answer: c. Custom text classification**

**Explanation:**
- **c. Custom text classification (CORRECT)** - Custom text classification lets you define your own categories and train a model using your labeled documents to classify text into those categories.
  - Reference: [Custom text classification](https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-text-classification/overview)

- **a. Named entity recognition (INCORRECT)** - NER extracts entities (names, places, dates) from text but doesn't classify documents into categories.
  - Reference: [Named entity recognition](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/overview)

- **b. Pre-built text classification (INCORRECT)** - Pre-built classification uses predefined categories, not custom ones specific to the legal firm.
  - Reference: [Azure AI Language features](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)

- **d. Sentiment analysis (INCORRECT)** - Sentiment analysis determines emotional tone, not document type classification.
  - Reference: [Sentiment analysis](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/overview)

---

### Question 52

In Conversational Language Understanding (CLU), what is an "entity"?

a. The overall goal of a user's request
b. A specific piece of information to extract from user input
c. A predefined response to a question
d. A conversation turn between user and bot

**Correct answer: b. A specific piece of information to extract from user input**

**Explanation:**
- **b. A specific piece of information to extract from user input (CORRECT)** - Entities are key pieces of information in user utterances, like dates, locations, product names, or quantities that need to be extracted.
  - Reference: [CLU concepts - Entities](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/concepts/entity-components)

- **a. The overall goal of a user's request (INCORRECT)** - This describes an intent, not an entity.
  - Reference: [Intents and entities](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

- **c. A predefined response to a question (INCORRECT)** - Responses come from your application logic; CLU extracts intents and entities to determine the response.
  - Reference: [CLU overview](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

- **d. A conversation turn between user and bot (INCORRECT)** - A turn is a single exchange; entities are information pieces extracted from user messages.
  - Reference: [Conversational Language Understanding](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

---

### Question 53

Azure AI Speech offers real-time speech translation. This capability can translate spoken audio from one language into:

a. Written text in the same language only
b. Written text in another language
c. Both written text and synthesized speech in another language
d. Only synthesized speech in another language

**Correct answer: c. Both written text and synthesized speech in another language**

**Explanation:**
- **c. Both written text and synthesized speech in another language (CORRECT)** - Speech translation converts spoken audio to both translated text and optionally to synthesized speech in the target language.
  - Reference: [Speech translation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-translation)

- **a. Written text in the same language only (INCORRECT)** - This describes speech-to-text (transcription), not speech translation.
  - Reference: [Speech-to-text](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text)

- **b. Written text in another language (INCORRECT)** - Partially correct but incomplete; speech translation also supports speech output.
  - Reference: [Speech translation output](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-translation)

- **d. Only synthesized speech in another language (INCORRECT)** - Speech translation always produces text and can optionally produce speech output.
  - Reference: [Speech translation overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-translation)

---

### Question 54

What is the purpose of Azure AI Language's "Text summarization" feature?

a. To translate text into a shorter language
b. To extract key sentences or generate an abstractive summary of long documents
c. To classify text into predefined categories
d. To detect the language of input text

**Correct answer: b. To extract key sentences or generate an abstractive summary of long documents**

**Explanation:**
- **b. To extract key sentences or generate an abstractive summary of long documents (CORRECT)** - Text summarization creates concise summaries through extractive (key sentences) or abstractive (rewritten) methods.
  - Reference: [Text summarization](https://learn.microsoft.com/en-us/azure/ai-services/language-service/summarization/overview)

- **a. To translate text into a shorter language (INCORRECT)** - Translation converts between languages; summarization condenses content regardless of language.
  - Reference: [Azure AI Translator](https://learn.microsoft.com/en-us/azure/ai-services/translator/translator-overview)

- **c. To classify text into predefined categories (INCORRECT)** - This describes text classification, not summarization.
  - Reference: [Custom text classification](https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-text-classification/overview)

- **d. To detect the language of input text (INCORRECT)** - This describes language detection, a different feature.
  - Reference: [Language detection](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-detection/overview)

---

### Question 55

Which scenario is best addressed by Custom Question Answering rather than Conversational Language Understanding?

a. Booking a flight with specific dates and destinations
b. Answering frequently asked questions from product documentation
c. Controlling smart home devices with voice commands
d. Processing food delivery orders with menu items and quantities

**Correct answer: b. Answering frequently asked questions from product documentation**

**Explanation:**
- **b. Answering frequently asked questions from product documentation (CORRECT)** - Custom Question Answering is designed for FAQ scenarios where questions match to pre-defined answers from documentation.
  - Reference: [Custom question answering](https://learn.microsoft.com/en-us/azure/ai-services/language-service/question-answering/overview)

- **a. Booking a flight with specific dates and destinations (INCORRECT)** - This requires extracting multiple entities (dates, locations) and understanding intent, which is CLU's strength.
  - Reference: [CLU vs QA](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

- **c. Controlling smart home devices with voice commands (INCORRECT)** - Command understanding with entities (device, action) is better handled by CLU.
  - Reference: [Conversational Language Understanding](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

- **d. Processing food delivery orders with menu items and quantities (INCORRECT)** - Order processing requires entity extraction (items, quantities, preferences), ideal for CLU.
  - Reference: [CLU entity extraction](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/overview)

---

## SEGMENT 4: Generative AI & Azure OpenAI (20-25%)

### Question 56

What is the primary difference between GPT models and embedding models in Azure OpenAI?

a. GPT models are faster than embedding models
b. GPT models generate text while embedding models convert text to numerical vectors
c. Embedding models generate images while GPT models generate text
d. GPT models require less compute resources

**Correct answer: b. GPT models generate text while embedding models convert text to numerical vectors**

**Explanation:**
- **b. GPT models generate text while embedding models convert text to numerical vectors (CORRECT)** - GPT models generate natural language responses, while embedding models create vector representations for similarity search and retrieval.
  - Reference: [Understand embeddings](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings)

- **a. GPT models are faster than embedding models (INCORRECT)** - Speed depends on usage; embedding models are typically faster for their task but serve different purposes.
  - Reference: [Azure OpenAI models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)

- **c. Embedding models generate images while GPT models generate text (INCORRECT)** - DALL-E generates images; embeddings create vectors, not images.
  - Reference: [DALL-E models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#dall-e-models)

- **d. GPT models require less compute resources (INCORRECT)** - GPT models are generally larger and more resource-intensive than embedding models.
  - Reference: [Model comparison](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)

---

### Question 57

In Azure OpenAI, what does the "max_tokens" parameter control?

a. The maximum length of the input prompt
b. The maximum length of the model's response
c. The total cost of the API call
d. The temperature of the output

**Correct answer: b. The maximum length of the model's response**

**Explanation:**
- **b. The maximum length of the model's response (CORRECT)** - max_tokens limits how many tokens the model can generate in its response, controlling output length.
  - Reference: [Completion parameters](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/completions)

- **a. The maximum length of the input prompt (INCORRECT)** - Input length is limited by the model's context window, not max_tokens.
  - Reference: [Token limits](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)

- **c. The total cost of the API call (INCORRECT)** - Cost depends on total tokens used (input + output), not just max_tokens setting.
  - Reference: [Azure OpenAI pricing](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)

- **d. The temperature of the output (INCORRECT)** - Temperature is controlled by a separate parameter, not max_tokens.
  - Reference: [Temperature parameter](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/completions#temperature)

---

### Question 58

Which prompt engineering technique involves instructing the model to explain its reasoning step-by-step before providing a final answer?

a. Few-shot learning
b. Chain-of-thought prompting
c. Zero-shot prompting
d. Meta-prompting

**Correct answer: b. Chain-of-thought prompting**

**Explanation:**
- **b. Chain-of-thought prompting (CORRECT)** - Chain-of-thought prompting asks the model to show its reasoning process step by step, improving accuracy for complex tasks.
  - Reference: [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)

- **a. Few-shot learning (INCORRECT)** - Few-shot provides input/output examples but doesn't specifically require step-by-step reasoning.
  - Reference: [Few-shot learning](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)

- **c. Zero-shot prompting (INCORRECT)** - Zero-shot provides no examples, just direct instructions without reasoning requirements.
  - Reference: [Zero-shot prompting](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)

- **d. Meta-prompting (INCORRECT)** - This is not a standard Azure OpenAI prompt engineering technique.
  - Reference: [Prompt engineering best practices](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)

---

### Question 59

An organization wants to use Azure OpenAI to answer questions based solely on their internal company documents, ensuring the model doesn't use its general training knowledge. Which feature should they implement?

a. Fine-tuning
b. Azure OpenAI on your data
c. Content filtering
d. Function calling

**Correct answer: b. Azure OpenAI on your data**

**Explanation:**
- **b. Azure OpenAI on your data (CORRECT)** - "On your data" connects Azure OpenAI to your data sources (like Azure AI Search) and grounds responses in your specific documents.
  - Reference: [Azure OpenAI on your data](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)

- **a. Fine-tuning (INCORRECT)** - Fine-tuning adjusts model weights for style/format but doesn't restrict the model to only your documents at inference time.
  - Reference: [Fine-tuning](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/fine-tuning)

- **c. Content filtering (INCORRECT)** - Content filtering blocks harmful content but doesn't ground responses in specific documents.
  - Reference: [Content filtering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter)

- **d. Function calling (INCORRECT)** - Function calling enables the model to call external functions/APIs but doesn't specifically ground responses in documents.
  - Reference: [Function calling](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling)

---

### Question 60

Which Azure OpenAI capability allows models to request specific external actions, like searching a database or calling an API, based on user input?

a. System messages
b. Function calling
c. Content filtering
d. Embeddings

**Correct answer: b. Function calling**

**Explanation:**
- **b. Function calling (CORRECT)** - Function calling enables the model to generate structured outputs that trigger specific functions in your application, like database queries or API calls.
  - Reference: [Function calling](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling)

- **a. System messages (INCORRECT)** - System messages set behavior instructions but don't enable external action execution.
  - Reference: [System messages](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/chatgpt#use-system-messages)

- **c. Content filtering (INCORRECT)** - Content filtering screens for harmful content but doesn't enable external actions.
  - Reference: [Content filtering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter)

- **d. Embeddings (INCORRECT)** - Embeddings convert text to vectors for similarity search, not for calling external functions.
  - Reference: [Understand embeddings](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings)

---

## Practice Questions Summary

**Total Questions in Set 2:** 20 (5 per segment)

**Segment Breakdown:**
- Machine Learning on Azure: Questions 41-45
- Computer Vision: Questions 46-50
- Natural Language Processing: Questions 51-55
- Generative AI & Azure OpenAI: Questions 56-60

**Combined with Set 1:** 60 total practice questions

**Study Tips:**
1. Review both question sets for comprehensive coverage
2. Pay attention to questions you missed - they highlight knowledge gaps
3. Click through to the Microsoft Learn references for deeper understanding
4. Practice explaining concepts to solidify understanding
5. Time yourself: aim for about 1-1.5 minutes per question on the exam

---

*Created for AI-900 Exam Preparation | Updated: November 2025*
*All Microsoft Learn references verified as of November 2025*
