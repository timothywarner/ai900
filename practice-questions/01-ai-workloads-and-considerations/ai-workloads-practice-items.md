---
exam: AI-900
domain: "Describe AI workloads and considerations"
weight: "15-20%"
item_count: 5
cognitive_level: Apply
generated: 2026-02-23
---

# Domain 1: Describe AI Workloads and Considerations

Practice items for AI-900 exam preparation.

---

### Item 1
**Objective:** Identify document processing workloads
**Cognitive Level:** Apply

**Stem:**
Contoso Insurance receives thousands of claim forms each week in various formats, including scanned PDFs, photographed receipts, and handwritten notes. The operations team wants to automatically extract key fields such as claim amounts, policy numbers, and dates from these documents without manually entering data. Which type of AI workload should Contoso Insurance implement?

A) Natural language processing workload
B) Computer vision workload for image classification
C) Document processing workload
D) Generative AI workload

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because document processing (document intelligence) workloads are specifically designed to extract structured information such as key-value pairs, tables, and fields from forms, invoices, receipts, and other documents. Azure AI Document Intelligence is the service built for this scenario.
- **A is incorrect** because natural language processing workloads focus on understanding and generating human language (such as sentiment analysis, entity recognition, and translation), not on extracting structured fields from scanned or photographed forms.
- **B is incorrect** because image classification identifies what category an image belongs to (such as "cat" or "dog"), but does not extract specific data fields like policy numbers and claim amounts from documents.
- **D is incorrect** because generative AI workloads focus on creating new content (text, images, code) rather than extracting structured data from existing documents.

**Reference:** https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-900

</details>

---

### Item 2
**Objective:** Describe considerations for fairness in an AI solution
**Cognitive Level:** Apply

**Stem:**
Fabrikam HR is deploying an AI-powered resume screening tool to help filter job applicants for open positions. During testing, the team discovers that the model consistently ranks applicants from certain universities higher than equally qualified applicants from other institutions. Which responsible AI principle is most directly violated by this behavior?

A) Transparency
B) Fairness
C) Accountability
D) Privacy and security

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because fairness requires that AI systems treat all people equitably and avoid affecting similarly situated groups of people in different ways. A resume screening tool that systematically favors candidates from certain universities over equally qualified candidates from other institutions exhibits bias, which is a fairness violation.
- **A is incorrect** because transparency is about being open about how an AI system works, its limitations, and how it makes decisions. While the team may also want transparency into why the model favors certain universities, the core issue described is unfair treatment of equivalent candidates, which is a fairness concern.
- **C is incorrect** because accountability refers to ensuring that people are responsible for how AI systems operate and how they affect the world. The scenario describes biased model behavior, not a lack of human oversight or responsibility structures.
- **D is incorrect** because privacy and security focus on protecting personal data and ensuring that individuals' fundamental right to privacy is preserved. The scenario does not describe a data breach or misuse of personal information.

**Reference:** https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai

</details>

---

### Item 3
**Objective:** Identify computer vision workloads
**Cognitive Level:** Apply

**Stem:**
Tailwind Traders operates a chain of retail warehouses. The safety team wants to deploy cameras at warehouse entrances that can automatically detect whether employees entering the floor are wearing required hard hats and safety vests. When a person is detected without the proper equipment, the system should trigger an alert. Which type of AI workload best addresses this requirement?

A) Computer vision workload using object detection
B) Natural language processing workload
C) Document processing workload
D) Computer vision workload using image classification

<details>
<summary>Show Answer</summary>

**Correct Answer:** A

**Rationale:**
- **A is correct** because object detection identifies and locates specific objects within an image, drawing bounding boxes around them. Detecting whether a person is wearing a hard hat and safety vest requires the system to identify and locate multiple distinct objects (person, hard hat, vest) within a single frame, which is precisely what object detection does.
- **B is incorrect** because natural language processing workloads deal with understanding and processing human language (text or speech), not analyzing visual content from camera feeds.
- **C is incorrect** because document processing workloads are designed to extract structured data from documents such as forms, invoices, and receipts, not to analyze live video or camera images for physical objects.
- **D is incorrect** because image classification assigns a single label to an entire image (for example, "safe" or "unsafe") but does not identify or locate specific objects within the image. The scenario requires detecting individual items of safety equipment on a person, which needs object-level detection, not whole-image classification.

**Reference:** https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-900

</details>

---

### Item 4
**Objective:** Describe considerations for transparency in an AI solution
**Cognitive Level:** Apply

**Stem:**
Northwind Traders uses an AI system to automatically approve or deny customer credit applications. Several customers have complained that their applications were denied without any explanation. The company wants to address these complaints while adhering to Microsoft's responsible AI principles. Which action best aligns with the transparency principle?

A) Retrain the model with a larger, more diverse dataset to improve accuracy
B) Provide customers with clear information about how the AI system makes credit decisions and the factors that influenced the denial
C) Implement multi-factor authentication to secure the credit application portal
D) Assign a dedicated team to manually review every denied application

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because the transparency principle requires organizations to be open about how and why AI systems make decisions. Providing customers with clear explanations of the factors that influenced their credit denial directly addresses this principle by making the AI system's decision-making process understandable.
- **A is incorrect** because retraining the model with more diverse data addresses the fairness principle (reducing bias) and may improve accuracy, but it does not explain to customers why their applications were denied. The complaint is about lack of explanation, not about model accuracy.
- **C is incorrect** because implementing multi-factor authentication addresses privacy and security concerns, not the transparency issue. Customers are asking for explanations of decisions, not better account security.
- **D is incorrect** because assigning a team to manually review denials addresses accountability (ensuring human oversight) but does not inherently provide customers with an explanation of how the AI arrived at its decision. Manual review alone, without communicating reasons to the customer, does not satisfy transparency.

**Reference:** https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai

</details>

---

### Item 5
**Objective:** Identify features of generative AI workloads
**Cognitive Level:** Apply

**Stem:**
Adatum Corporation wants to build an internal tool that allows employees to describe a desired marketing image in plain language and have the system produce an original image matching that description. The tool should also be able to draft promotional email text based on bullet-point input from the marketing team. Which type of AI workload is Adatum describing?

A) Natural language processing workload
B) Computer vision workload
C) Generative AI workload
D) Document processing workload

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because generative AI workloads are designed to create new, original content including text, images, code, and more based on user prompts. The scenario describes two generative tasks: creating images from text descriptions (like DALL-E) and generating email copy from bullet points (like GPT-4o), both of which are core generative AI capabilities.
- **A is incorrect** because natural language processing workloads focus on understanding, analyzing, and interpreting existing text or speech (such as sentiment analysis, key phrase extraction, or translation). While NLP may be involved in interpreting the prompt, the defining characteristic of this scenario is the creation of new content, which is generative AI.
- **B is incorrect** because computer vision workloads analyze and interpret existing images (such as classifying objects, detecting faces, or reading text from images). This scenario requires generating new images from text descriptions, not analyzing existing ones.
- **D is incorrect** because document processing workloads extract structured data from existing documents such as invoices, forms, and receipts. The scenario involves creating new marketing content, not processing existing documents.

**Reference:** https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-900

</details>

---
