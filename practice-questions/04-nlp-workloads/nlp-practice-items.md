---
exam: AI-900
domain: "Describe features of NLP workloads on Azure"
weight: "15-20%"
item_count: 5
cognitive_level: Apply
generated: 2026-02-23
---

# Domain 4: Features of NLP Workloads on Azure

Practice items for AI-900 exam preparation.

---

### Item 1
**Objective:** Identify features and uses for sentiment analysis
**Cognitive Level:** Apply

**Stem:**
Contoso Hotels operates a chain of 200 properties worldwide. The customer experience team receives thousands of guest reviews each day across multiple online platforms. Management wants to automatically determine whether each review expresses a positive, negative, or neutral opinion so they can prioritize responses to dissatisfied guests. A developer needs to recommend the appropriate Azure AI capability to implement this solution.

Which Azure AI Language feature should the developer use?

A) Key phrase extraction
B) Sentiment analysis
C) Entity recognition
D) Conversational Language Understanding (CLU)

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because sentiment analysis in Azure AI Language evaluates text and returns sentiment scores and labels (positive, negative, neutral, or mixed) for each sentence and the document as a whole. This directly addresses the need to classify guest reviews by overall opinion.
- **A is incorrect** because key phrase extraction identifies the main topics or talking points in text, but does not determine whether the opinion expressed is positive, negative, or neutral.
- **C is incorrect** because entity recognition identifies and categorizes entities such as people, places, organizations, and quantities in text. It does not assess the emotional tone of a review.
- **D is incorrect** because Conversational Language Understanding (CLU) is used to build custom natural language understanding models that predict intents and extract entities from conversational utterances, such as those used in chatbot dialogs. It is not designed for bulk sentiment scoring of reviews.

**Reference:** [https://learn.microsoft.com/azure/ai-services/language-service/sentiment-opinion-mining/overview](https://learn.microsoft.com/azure/ai-services/language-service/sentiment-opinion-mining/overview)

</details>

---

### Item 2
**Objective:** Identify features and uses for speech recognition and synthesis; Describe capabilities of the Azure AI Speech service
**Cognitive Level:** Apply

**Stem:**
Fabrikam Manufacturing is building an interactive kiosk for its factory floor. Workers wearing gloves cannot use a keyboard or touchscreen. The kiosk must listen to spoken commands from workers, process the requests, and then read the responses aloud. The development team needs to select the Azure service that provides both speech-to-text and text-to-speech capabilities in a single service.

Which Azure service should the team use?

A) Azure AI Language
B) Azure AI Translator
C) Azure AI Speech
D) Azure AI Vision

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because Azure AI Speech provides both speech-to-text (speech recognition) and text-to-speech (speech synthesis) capabilities within a single service. Speech-to-text converts the workers' spoken commands into text for processing, and text-to-speech converts the system's text responses into natural-sounding audio output.
- **A is incorrect** because Azure AI Language provides text analytics capabilities such as sentiment analysis, key phrase extraction, entity recognition, and conversational language understanding. It processes text input but does not convert speech to text or text to speech.
- **B is incorrect** because Azure AI Translator is designed for translating text or speech between different languages. While it can work with speech translation scenarios, it is not the primary service for general-purpose speech recognition and synthesis within a single language.
- **D is incorrect** because Azure AI Vision is used for image analysis, object detection, optical character recognition, and facial analysis. It does not provide any speech-related capabilities.

**Reference:** [https://learn.microsoft.com/azure/ai-services/speech-service/overview](https://learn.microsoft.com/azure/ai-services/speech-service/overview)

</details>

---

### Item 3
**Objective:** Identify features and uses for key phrase extraction and entity recognition; Describe capabilities of the Azure AI Language service
**Cognitive Level:** Apply

**Stem:**
Northwind Traders publishes a large volume of product descriptions and supplier contracts. The legal team wants to automatically scan these documents and extract specific named items such as company names, locations, dates, and monetary amounts so they can quickly index and search contract metadata. A solutions architect needs to identify the correct Azure AI Language feature for this requirement.

Which Azure AI Language feature should the architect recommend?

A) Sentiment analysis
B) Key phrase extraction
C) Named entity recognition
D) Language detection

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because named entity recognition (NER) in Azure AI Language identifies and categorizes entities in text into predefined categories such as person, organization, location, date/time, and quantity. This directly addresses the need to extract company names, locations, dates, and monetary amounts from contracts.
- **A is incorrect** because sentiment analysis determines the emotional tone (positive, negative, or neutral) of text. It does not extract specific named entities like company names or dates.
- **B is incorrect** because key phrase extraction identifies the main concepts and talking points in a document. While it surfaces important terms, it does not categorize them into entity types such as organization, location, or monetary value.
- **D is incorrect** because language detection identifies the language in which a given text is written. It does not extract or categorize entities within the text.

**Reference:** [https://learn.microsoft.com/training/modules/get-started-language-azure/](https://learn.microsoft.com/training/modules/get-started-language-azure/)

</details>

---

### Item 4
**Objective:** Identify features and uses for translation; Describe capabilities of the Azure AI Language service and Azure AI Speech service
**Cognitive Level:** Apply

**Stem:**
Tailwind Traders is expanding into new international markets and needs to translate its product catalog, which contains over 50,000 text-based product descriptions, from English into French, German, and Japanese. The translations must preserve the original formatting and be processed programmatically through an API. The team needs to select the appropriate Azure service to perform real-time text translation at scale.

Which Azure service should the team use?

A) Azure AI Speech
B) Azure AI Language
C) Azure AI Translator
D) Conversational Language Understanding (CLU)

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because Azure AI Translator is specifically designed for real-time text translation across multiple languages. It supports over 100 languages, can translate text programmatically through a REST API, and can handle large-scale translation workloads. It is the purpose-built service for translating text content between languages.
- **A is incorrect** because Azure AI Speech provides speech-to-text, text-to-speech, and speech translation capabilities. While it can translate spoken audio, it is not the appropriate service for translating large volumes of written text documents.
- **B is incorrect** because Azure AI Language provides text analytics features such as sentiment analysis, entity recognition, and key phrase extraction. It analyzes text but does not translate text between languages.
- **D is incorrect** because Conversational Language Understanding (CLU) is a feature of Azure AI Language that builds custom models to predict intents and extract entities from conversational utterances. It is not a translation service.

**Reference:** [https://learn.microsoft.com/training/modules/translate-text-with-translation-service/](https://learn.microsoft.com/training/modules/translate-text-with-translation-service/)

</details>

---

### Item 5
**Objective:** Identify features and uses for language modeling; Describe capabilities of the Azure AI Language service
**Cognitive Level:** Apply

**Stem:**
Adatum Corporation is developing a virtual assistant for its internal IT help desk. Employees will type or speak requests such as "I need to reset my password" or "My laptop won't connect to the VPN." The virtual assistant must understand the intent behind each request (for example, password reset versus VPN troubleshooting) and extract relevant details (such as the device type or the specific application mentioned). The development team needs to build a custom model that maps employee utterances to predefined intents and entities.

Which Azure AI Language feature should the team use?

A) Sentiment analysis
B) Key phrase extraction
C) Custom Question Answering
D) Conversational Language Understanding (CLU)

<details>
<summary>Show Answer</summary>

**Correct Answer:** D

**Rationale:**
- **D is correct** because Conversational Language Understanding (CLU) is a feature of Azure AI Language that enables developers to build custom natural language understanding models. CLU predicts the overall intent of an incoming utterance and extracts important entities from it. Developers can iteratively label utterances, train, and evaluate model performance. This is the correct choice for mapping employee requests to specific intents (password reset, VPN troubleshooting) and extracting entities (device type, application name).
- **A is incorrect** because sentiment analysis determines whether text is positive, negative, or neutral. It does not identify intents or extract structured entities from conversational input.
- **B is incorrect** because key phrase extraction identifies the main talking points in text. While it could surface terms like "password" or "VPN," it does not map utterances to predefined intents or extract typed entities.
- **C is incorrect** because Custom Question Answering is designed to create a knowledge base of question-and-answer pairs from existing content such as FAQs or documentation. It returns the best matching answer to a question but does not predict user intents or extract entities from conversational utterances the way CLU does.

**Reference:** [https://learn.microsoft.com/azure/ai-services/language-service/conversational-language-understanding/overview](https://learn.microsoft.com/azure/ai-services/language-service/conversational-language-understanding/overview)

</details>

---
