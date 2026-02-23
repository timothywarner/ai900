# Fact-Check Report: Domains 1-2

## Summary
- Items checked: 10
- Issues found: 1
- Items requiring correction: None (issue is minor and advisory only)

All 10 practice items across both domains are factually accurate per current Microsoft Learn documentation. Correct answers are verified, terminology is current, distractors are plausible but definitively wrong, and reference URLs resolve to valid Microsoft Learn pages.

---

## Domain 1: AI Workloads and Considerations

### Item 1: PASS
- **Correct answer verified:** Yes -- "Document processing workload" (C) is correct. The AI-900 study guide (updated May 2, 2025) explicitly lists "Identify document processing workloads" as an objective under Domain 1. Azure AI Document Intelligence is the service designed to extract key-value pairs, tables, and fields from forms, invoices, receipts, and scanned documents. Confirmed via Microsoft Learn search results for Document Intelligence and the AI-900 study guide.
- **Terminology current:** Yes -- Uses "Azure AI Document Intelligence" (the current name). Does not use the deprecated "Form Recognizer" name.
- **Distractors valid:** Yes -- NLP (A) deals with language understanding not structured field extraction; image classification (B) categorizes whole images not extracts fields; generative AI (D) creates new content not extracts from existing documents. All are plausible but definitively wrong for this scenario.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-900` resolves correctly and contains the study guide with "Identify document processing workloads" listed.
- **Stem quality:** Good -- Presents a realistic workplace scenario (insurance company processing claim forms) rather than a definition-in-disguise.

### Item 2: PASS
- **Correct answer verified:** Yes -- "Fairness" (B) is correct. Microsoft's Responsible AI documentation states: "Fairness -- We make sure AI systems treat everyone fairly and avoid affecting similarly situated groups of people in different ways." A resume screening tool that systematically favors candidates from certain universities over equally qualified candidates is a textbook fairness violation. Confirmed via `https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai`.
- **Terminology current:** Yes -- Uses the current six-principle framework (fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability).
- **Distractors valid:** Yes -- Transparency (A) is about openness in decision-making processes, not bias; accountability (C) is about human oversight; privacy/security (D) is about data protection. Each distractor addresses a different RAI principle and is clearly distinguishable from fairness.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai` was fetched and confirmed to contain detailed descriptions of all six Responsible AI principles including fairness.
- **Stem quality:** Good -- Realistic HR scenario with a specific manifestation of bias (university favoritism).

### Item 3: PASS
- **Correct answer verified:** Yes -- "Computer vision workload using object detection" (A) is correct. Object detection identifies and locates specific objects within an image with bounding boxes. Detecting hard hats and safety vests on individual people requires identifying multiple distinct objects and their locations, which is object detection. Confirmed via Microsoft Learn documentation on Custom Vision capabilities: "Object detection -- Get the coordinates of an object in an image."
- **Terminology current:** Yes -- Uses current terminology (object detection, image classification). No deprecated service names used.
- **Distractors valid:** Yes -- NLP (B) processes text/speech not visual content; document processing (C) extracts data from documents; image classification (D) assigns a single label to an entire image but does not locate specific objects within it. The distinction between object detection (A) and image classification (D) is a well-known exam concept and both are plausible distractors at the right difficulty level.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-900` resolves correctly.
- **Stem quality:** Good -- Realistic workplace safety scenario (warehouse PPE detection).

### Item 4: PASS
- **Correct answer verified:** Yes -- "Provide customers with clear information about how the AI system makes credit decisions" (B) is correct. The transparency principle requires organizations to be open about how and why AI systems make decisions. Microsoft's RAI documentation states: "Transparency -- We're open about how and why we build AI systems, what their limitations are, and how the system makes decisions." Providing explanations directly addresses this.
- **Terminology current:** Yes -- All RAI principle names match current Microsoft documentation.
- **Distractors valid:** Yes -- Retraining with diverse data (A) addresses fairness; MFA (C) addresses security; manual review (D) addresses accountability. Each maps clearly to a different RAI principle, making them plausible but definitively wrong for transparency.
- **Reference URL checked:** Yes -- Same URL as Item 2, confirmed valid.
- **Stem quality:** Good -- Realistic credit decision scenario with customer complaints, requiring the candidate to apply the transparency principle to a specific business action.

### Item 5: PASS
- **Correct answer verified:** Yes -- "Generative AI workload" (C) is correct. The scenario describes two generative tasks: creating images from text descriptions (DALL-E capability) and generating email text from bullet points (GPT capability). Both are core generative AI capabilities confirmed in Microsoft Learn documentation on Azure OpenAI.
- **Terminology current:** Yes -- References DALL-E and GPT-4o in the rationale, which are current model names. Uses "Microsoft Foundry" context appropriately.
- **Distractors valid:** Yes -- NLP (A) analyzes/interprets existing text; computer vision (B) analyzes existing images; document processing (D) extracts from existing documents. All are clearly about processing existing content, not creating new content.
- **Reference URL checked:** Yes -- Study guide URL confirmed valid.
- **Stem quality:** Good -- Realistic marketing department scenario combining both image generation and text generation.

---

## Domain 2: Fundamental Principles of Machine Learning on Azure

### Item 1: PASS
- **Correct answer verified:** Yes -- "Regression" (C) is correct. Regression predicts continuous numeric values. Predicting a home selling price in dollars is a classic regression scenario. Confirmed via the Microsoft Learn module "Regression" at `https://learn.microsoft.com/training/modules/fundamentals-machine-learning/4-regression`, which states: "Regression models are trained to predict numeric label values based on training data."
- **Terminology current:** Yes -- Uses standard ML terminology (regression, classification, clustering, CNN).
- **Distractors valid:** Yes -- Classification (A) predicts categorical labels not continuous values; clustering (B) is unsupervised and groups data without predicting a target; CNN/deep learning (D) is primarily for image tasks. All are plausible ML techniques but wrong for this specific scenario.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/training/modules/fundamentals-machine-learning/4-regression` was fetched and confirmed to contain detailed regression explanation with examples of predicting numeric values.
- **Stem quality:** Good -- Realistic real estate valuation scenario with specific features listed.

### Item 2: PASS
- **Correct answer verified:** Yes -- "Clustering" (C) is correct. Clustering is unsupervised ML that discovers natural groupings in unlabeled data. Confirmed via `https://learn.microsoft.com/training/modules/fundamentals-machine-learning/7-clustering`, which states: "Clustering is a form of unsupervised machine learning in which observations are grouped into clusters based on similarities in their data values, or features."
- **Terminology current:** Yes -- Standard ML terminology used throughout.
- **Distractors valid:** Yes -- Binary classification (A) requires predefined two-category labels; regression (B) predicts numeric values; multiclass classification (D) requires predefined multi-category labels. The stem explicitly states "does not have predefined categories," which eliminates both classification options cleanly.
- **Reference URL checked:** Yes -- Clustering module URL fetched and confirmed valid with detailed K-means clustering explanation.
- **Stem quality:** Good -- Realistic retail marketing scenario with clear business rationale for discovering segments.

### Item 3: PASS
- **Correct answer verified:** Yes -- "Automated machine learning (AutoML)" (B) is correct. AutoML automatically iterates through multiple algorithms and hyperparameter configurations to find the best model. Microsoft's AutoML documentation confirms: "Automated ML democratizes the machine learning model development process and empowers its users, regardless of their data science expertise." This matches the scenario of business analysts with limited data science experience.
- **Terminology current:** Yes -- Uses "Azure Machine Learning designer," "Automated machine learning (AutoML)," "SDK v2," and "compute instances" -- all current terminology.
- **Distractors valid:** Yes -- Designer (A) requires manual algorithm selection; SDK v2 (C) requires programming expertise; compute instances (D) are infrastructure, not a training capability. All are real Azure ML features but wrong for automated algorithm selection with minimal coding.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/azure/machine-learning/concept-automated-ml?view=azureml-api-2` was fetched and confirmed valid with comprehensive AutoML documentation.
- **Stem quality:** Good -- Realistic insurance fraud detection scenario with clear constraint (limited data science expertise).

### Item 4: PASS (with minor advisory note)
- **Correct answer verified:** Yes -- "The model is overfitting; she is using a training dataset and a validation dataset" (B) is correct. High training accuracy (98%) with significantly lower held-out accuracy (72%) is the classic indicator of overfitting. Microsoft Learn's ML fundamentals content confirms that training data is used to train the model and validation data is used to evaluate performance on unseen data.
- **Terminology current:** Yes -- Standard ML terminology (overfitting, underfitting, training/validation datasets).
- **Distractors valid:** Yes -- Underfitting (A) would show poor performance on both sets; "performs well" (C) ignores a 26-point gap; combining datasets (D) would eliminate the evaluation mechanism and not solve the problem.
- **Advisory note:** The distinction between "validation dataset" and "test dataset" can be nuanced. In practice, when data is split into two subsets (train and evaluate), the held-out portion is sometimes called a "test set" rather than a "validation set." However, the AI-900 exam context and Microsoft Learn content consistently use "validation" for the held-out subset used during model development, reserving "test" for a final independent evaluation. The item's usage is consistent with Microsoft's AI-900 training materials. This is not an error, but instructors should be aware of this distinction.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/training/modules/fundamentals-machine-learning/2-what-is-machine-learning` fetched and confirmed valid with content about features, labels, training, and inferencing.
- **Stem quality:** Good -- Realistic customer churn prediction scenario with specific accuracy numbers to analyze.

### Item 5: PASS
- **Correct answer verified:** Yes -- "Deploy the model to a real-time online endpoint in Azure Machine Learning" (B) is correct. Microsoft Learn's documentation on online endpoints states: "Online endpoints deploy models to a web server that can return predictions under the HTTP protocol. Online endpoints can operationalize models for real-time inference." The AutoML deployment documentation confirms models can be deployed directly to real-time endpoints without retraining.
- **Terminology current:** Yes -- Uses "real-time online endpoint," "managed online endpoints," "Transformer architecture" -- all current terminology. Does not use deprecated deployment terms.
- **Distractors valid:** Yes -- CSV export (A) is nonsensical for model deployment; batch pipeline (C) runs on a schedule, not real-time; retraining in designer (D) is not a prerequisite for deployment. All are plausible-sounding but definitively wrong.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/azure/machine-learning/how-to-deploy-automl-endpoint?view=azureml-api-2` was fetched and confirmed valid with step-by-step AutoML model deployment instructions including the "Real-time endpoint" option.
- **Stem quality:** Good -- Realistic helpdesk application scenario with clear real-time requirement. Mentions Transformer architecture, which aligns with the exam objective.

---

## Corrections Needed

No corrections are needed. All 10 items are factually accurate, use current terminology, have valid reference URLs, plausible distractors, and realistic workplace scenario stems.

### Minor Advisory Notes (no action required):

1. **Domain 2, Item 4 -- Validation vs. Test terminology:** The item correctly uses "validation dataset" per Microsoft Learn conventions for AI-900, but instructors should note that in industry practice, the terminology can vary. The item's rationale could optionally note this distinction, but it is not an error.

2. **Domain 1, Items 1/3/5 -- Reference URL specificity:** These three items reference the general AI-900 study guide URL rather than a specific learning module. While technically valid (the study guide confirms the objectives tested), linking to the specific training module pages would provide learners with more targeted study material. For example:
   - Item 1 could additionally reference: `https://learn.microsoft.com/training/modules/fundamentals-machine-learning/` or Document Intelligence overview pages
   - Item 3 could additionally reference: `https://learn.microsoft.com/training/modules/detect-objects-images/`
   - Item 5 could additionally reference: `https://learn.microsoft.com/training/modules/generate-images-azure-openai/`

---

*Report generated: 2026-02-23*
*Verified against: Microsoft Learn documentation (current as of February 2026)*
*Reviewer: AI-900 Exam Quality Review (automated fact-check)*
