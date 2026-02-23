---
exam: AI-900
domain: "Describe features of generative AI workloads on Azure"
weight: "20-25%"
item_count: 5
cognitive_level: Apply
generated: 2026-02-23
---

# Domain 5: Features of Generative AI Workloads on Azure

Practice items for AI-900 exam preparation.

---

### Item 1
**Objective:** Identify common scenarios for generative AI (natural language generation, image generation, code generation)
**Cognitive Level:** Apply

**Stem:**
Contoso Ltd. is a marketing agency that needs to rapidly produce multiple variations of promotional banner images from written campaign briefs. The creative director wants a solution where designers type a text description of the desired image and the system generates visual artwork automatically. The solution must run within the company's existing Azure environment. Which Azure OpenAI Service model should the team deploy to meet this requirement?

A) GPT-4o, because it can process both text and image inputs for multimodal analysis
B) DALL-E 3, because it generates images from natural language text prompts
C) An embeddings model, because it converts text descriptions into visual vector representations
D) Whisper, because it translates spoken campaign briefs into image assets

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because DALL-E 3 is the Azure OpenAI Service model specifically designed for text-to-image generation. It takes a natural language text prompt and produces original images that match the description. This directly satisfies the requirement of generating banner images from written campaign briefs.
- **A is incorrect** because GPT-4o is a large language model that can accept image inputs for analysis (vision capability) and generate text responses, but it does not generate images. It would be useful for describing or analyzing images, not creating them.
- **C is incorrect** because embeddings models convert text into numerical vector representations used for similarity search and retrieval tasks. They do not produce visual images from text descriptions.
- **D is incorrect** because Whisper is a speech-to-text model used for audio transcription and translation. It processes spoken audio into written text and has no image generation capability.

**Reference:** [https://learn.microsoft.com/azure/ai-foundry/openai/how-to/dall-e](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/dall-e)

</details>

---

### Item 2
**Objective:** Describe prompt engineering concepts (system messages, few-shot learning, grounding)
**Cognitive Level:** Apply

**Stem:**
Fabrikam Inc. is building a customer service chatbot using Azure OpenAI Service. The development team needs the chatbot to always respond in a professional, empathetic tone and to never provide medical or legal advice. The team wants to enforce these behavioral constraints consistently across every user interaction, regardless of what the user types. Which prompt engineering technique should the team implement to achieve this?

A) Configure a system message that defines the chatbot's persona, tone, and topic boundaries
B) Use few-shot learning by including example conversations in every user prompt
C) Increase the temperature parameter to allow the model to generate more varied responses
D) Deploy a separate embeddings model to filter user messages before they reach the chatbot

<details>
<summary>Show Answer</summary>

**Correct Answer:** A

**Rationale:**
- **A is correct** because the system message (also called the metaprompt or system prompt) is the prompt engineering mechanism specifically designed to define behavioral constraints, persona, tone, and topic boundaries for a model. It is applied to every conversation and provides persistent instructions that guide the model's responses regardless of user input. This is the standard approach recommended by Microsoft for enforcing consistent behavior.
- **B is incorrect** because few-shot learning involves providing example input-output pairs to help the model understand a desired response format or task pattern. While useful for demonstrating specific response styles, it is not the primary mechanism for enforcing persistent behavioral rules and topic restrictions across all interactions. Including examples in every user prompt would also be inefficient and consume unnecessary tokens.
- **C is incorrect** because the temperature parameter controls the randomness or creativity of model outputs. Increasing temperature would make responses more varied and potentially less predictable, which is the opposite of enforcing consistent professional behavior and topic boundaries.
- **D is incorrect** because embeddings models are used for converting text into vector representations for similarity search and retrieval. They are not designed to filter or enforce behavioral rules on a chatbot. Content filtering in Azure OpenAI is handled by built-in content filters (Guardrails), not by embeddings models.

**Reference:** [https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering)

</details>

---

### Item 3
**Objective:** Describe Retrieval-Augmented Generation (RAG) concepts (grounding with enterprise data, Azure AI Search integration)
**Cognitive Level:** Apply

**Stem:**
Northwind Traders maintains thousands of internal product specification documents, safety data sheets, and supplier contracts stored in Azure Blob Storage. The company wants employees to ask natural language questions and receive accurate answers grounded in these company-specific documents. The solution must reduce the risk of the generative AI model producing fabricated information. Which approach should Northwind Traders implement?

A) Fine-tune a GPT model by retraining it on all of the company's internal documents
B) Increase the model's token limit so it can process all company documents in a single prompt
C) Implement Retrieval-Augmented Generation (RAG) using Azure AI Search to index company documents and provide relevant content as context to the model
D) Use DALL-E 3 to convert document content into visual summaries that employees can search

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because Retrieval-Augmented Generation (RAG) is the recommended pattern for grounding generative AI responses in enterprise-specific data. In a RAG architecture, Azure AI Search indexes the company's documents, retrieves the most relevant content based on the user's query, and provides that content as context to the generative AI model. This grounds the model's responses in actual company data, significantly reducing the risk of hallucination (fabricated information). This is the standard approach described in Microsoft's documentation for building enterprise question-answering solutions.
- **A is incorrect** because fine-tuning retrains a model's weights to adjust its behavior or style, but it is not designed for injecting large volumes of frequently changing factual content. Fine-tuning is expensive, time-consuming, and does not guarantee the model will accurately recall specific document details. RAG is the recommended approach for grounding responses in enterprise data.
- **B is incorrect** because even with large token limits, it is not feasible to include thousands of documents in a single prompt. Token limits have hard caps, and sending excessive context is costly and reduces response quality. RAG solves this by retrieving only the most relevant document segments for each query.
- **D is incorrect** because DALL-E 3 is an image generation model that creates images from text prompts. It cannot convert documents into searchable visual summaries and is not relevant to a document question-answering scenario.

**Reference:** [https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)

</details>

---

### Item 4
**Objective:** Identify responsible AI considerations for generative AI (content filters, hallucination risks, transparency)
**Cognitive Level:** Apply

**Stem:**
Tailwind Traders is deploying an Azure OpenAI Service-powered chatbot on their public e-commerce website. During testing, the team discovers that the chatbot occasionally generates product specifications that do not exist in the company's catalog, presenting fabricated details as facts to customers. Which combination of responsible AI mitigations should the team apply to address this risk?

A) Enable Azure OpenAI content filters and implement a system message that instructs the model to only answer based on provided product data
B) Switch from GPT-4o to an older GPT-3.5 model, which produces shorter responses with fewer errors
C) Remove the system message to give the model maximum flexibility in responding to customers
D) Disable content filtering to avoid blocking any product-related responses that customers might need

<details>
<summary>Show Answer</summary>

**Correct Answer:** A

**Rationale:**
- **A is correct** because this combines two recommended responsible AI mitigations. Azure OpenAI content filters (Guardrails) help prevent harmful or inappropriate content from being generated. The system message serves as a metaprompt-level mitigation that instructs the model to only respond based on provided grounding data (product catalog information), reducing the risk of hallucination. Microsoft's responsible AI guidance specifically recommends both platform-level mitigations (content filters) and application-level mitigations (prompt engineering with system messages) as a layered defense approach.
- **B is incorrect** because switching to an older model does not address the fundamental problem of hallucination. All generative AI models can produce fabricated content regardless of version. The solution requires proper grounding and mitigation strategies, not a model downgrade.
- **C is incorrect** because removing the system message eliminates a critical mitigation layer. Without a system message defining behavioral boundaries and grounding instructions, the model is more likely to generate fabricated information, not less. This directly contradicts Microsoft's responsible AI recommendations.
- **D is incorrect** because disabling content filtering removes an important safety layer that helps prevent harmful, inappropriate, or misleading content. Microsoft requires content filtering to be enabled for Azure OpenAI Service deployments, and disabling it would increase risk rather than mitigate it.

**Reference:** [https://learn.microsoft.com/azure/ai-foundry/responsible-ai/openai/overview](https://learn.microsoft.com/azure/ai-foundry/responsible-ai/openai/overview)

</details>

---

### Item 5
**Objective:** Describe features and capabilities of Microsoft Foundry and the Microsoft Foundry model catalog
**Cognitive Level:** Apply

**Stem:**
Adatum Corporation's AI team needs to evaluate multiple large language models from different providers before selecting one for a new document summarization project. The team wants a centralized Azure portal experience where they can browse available models, compare their capabilities, test models interactively with sample prompts, and then deploy the chosen model to a managed endpoint. Which Azure service provides this capability?

A) Azure Machine Learning designer, which provides a drag-and-drop interface for building custom machine learning pipelines
B) Microsoft Foundry with its model catalog, which enables browsing, testing, comparing, and deploying models from multiple providers
C) Azure AI Search, which indexes and retrieves content from enterprise data sources for AI applications
D) Azure AI Language service, which provides prebuilt NLP capabilities such as sentiment analysis and entity recognition

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because Microsoft Foundry (at ai.azure.com) is Microsoft's unified platform for building generative AI applications. The Microsoft Foundry model catalog allows teams to browse models from multiple providers (including OpenAI, Meta, Mistral, and others), compare model capabilities, test models interactively in a playground with sample prompts, and deploy selected models to managed endpoints. This matches all of Adatum's requirements for evaluating and deploying a document summarization model.
- **A is incorrect** because Azure Machine Learning designer is a visual tool for building and training custom machine learning pipelines using drag-and-drop components. It is designed for creating traditional ML workflows (regression, classification, clustering), not for browsing and comparing pre-built large language models from multiple providers.
- **C is incorrect** because Azure AI Search is a search and retrieval service that indexes enterprise data sources for use in AI applications, particularly in RAG patterns. It does not provide a model catalog for browsing, testing, or deploying large language models.
- **D is incorrect** because Azure AI Language service provides prebuilt NLP capabilities such as sentiment analysis, key phrase extraction, entity recognition, and text summarization. While it can perform summarization, it is a fixed-capability service, not a platform for browsing and comparing multiple models from different providers.

**Reference:** [https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview](https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview)

</details>

---

*Generated from official Microsoft Learn documentation for AI-900 exam preparation. Domain 5 objectives last updated May 2, 2025.*
