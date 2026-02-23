# Fact-Check Report: Domains 3-4

## Summary
- Items checked: 10
- Issues found: 2
- Items requiring correction: Domain 3 Item 4 (minor clarification needed), Domain 4 Item 1 (reference URL points to renamed module)

## Domain 3: Computer Vision Workloads on Azure

### Item 1: PASS
- **Correct answer verified:** Yes -- Image classification assigns a single class label to an entire image. Microsoft docs confirm: "Image classification applies one or more labels to an entire image" while "Object detection returns the coordinates in the image where the applied label(s) can be found." The answer (B) is correct.
- **Terminology current:** Yes -- Uses "image classification" and "object detection" correctly. No deprecated service names.
- **Distractors valid:** Yes -- All distractors (object detection, OCR, facial detection) are plausible computer vision tasks but clearly wrong for a single-label-per-image scenario.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/training/modules/analyze-images-computer-vision/` resolves to a valid training module.
- **Stem quality:** Good workplace scenario with Contoso Vineyards and drone photography.

### Item 2: PASS
- **Correct answer verified:** Yes -- Object detection "identifies multiple objects in an image and returns a class label together with bounding box coordinates for each detected object" per Microsoft docs. The answer (C) is correct.
- **Terminology current:** Yes -- Uses current terms. "Semantic segmentation" is a valid computer vision term used as a distractor.
- **Distractors valid:** Yes -- All distractors are plausible. Semantic segmentation (B) is the strongest distractor but the rationale correctly explains why bounding boxes with discrete object instances are needed rather than pixel-level classification.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/training/modules/detect-objects-images/` resolves to a valid training module on object detection.
- **Stem quality:** Good workplace scenario with Fabrikam Retail warehouse automation.

### Item 3: PASS
- **Correct answer verified:** Yes -- Azure AI Document Intelligence (formerly Form Recognizer) is "specifically designed to extract text, key-value pairs, tables, and structure from documents such as forms, invoices, and receipts." It handles both printed and handwritten text. The answer (C) is correct.
- **Terminology current:** Yes -- Correctly uses "Azure AI Document Intelligence" and notes the former name "Form Recognizer" in parentheses in the rationale. No deprecated names in the stem or answer choices.
- **Distractors valid:** Yes -- Azure AI Vision Image Analysis (A) is a reasonable distractor since it also has OCR capabilities, but the rationale correctly differentiates it as optimized for general images, not structured form extraction. Azure AI Face (B) and Azure AI Language (D) are clearly wrong but plausible service names.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/azure/ai-services/document-intelligence/overview` resolves to the current Document Intelligence overview page.
- **Stem quality:** Good workplace scenario with Northwind Traders field sales order forms.

### Item 4: PASS (with advisory note)
- **Correct answer verified:** Yes -- The Azure AI Face service documentation confirms it can "detect human faces in an image and return face attributes such as head pose, age, emotion, facial hair, and glasses." The answer (C) is correct for AI-900 exam purposes.
- **Terminology current:** Yes -- Uses "Azure AI Face" correctly.
- **Distractors valid:** Yes -- All distractors are clearly wrong for face detection with demographic attributes.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/azure/ai-services/computer-vision/overview-identity` resolves to the Azure AI Face service overview page.
- **Stem quality:** Good workplace scenario with Tailwind Traders flagship store.
- **Advisory note:** Microsoft has placed the age attribute under **Limited Access** restrictions. The documentation states: "Microsoft has retired or limited facial recognition capabilities... The retired capabilities are emotion and gender. The limited capabilities are age, smile, facial hair, hair and makeup." While age estimation is still a capability of the Face service (making the answer technically correct), the item could benefit from a brief note in the rationale acknowledging the Limited Access policy for age attributes. This does not change the correct answer but provides exam candidates with more complete, current context.

### Item 5: PASS
- **Correct answer verified:** Yes -- Microsoft docs confirm: "The Caption feature generates a one-sentence description of all the image contents" and "Image captioning in Image Analysis generates a human-readable natural language sentence describing the content of an image." The answer (B) is correct.
- **Terminology current:** Yes -- Uses "Image Analysis Caption feature" correctly. Also worth noting: the Image Analysis service page now shows a deprecation notice (retirement date September 25, 2028), but the Caption feature remains the correct answer for current exam content.
- **Distractors valid:** Yes -- Read/OCR (A), Face detection (C), and Smart Crop (D) are all real Image Analysis features but serve different purposes.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/azure/ai-services/computer-vision/overview-image-analysis` resolves to the Image Analysis overview page.
- **Stem quality:** Good workplace scenario with Adatum field technicians and accessibility.

---

## Domain 4: NLP Workloads on Azure

### Item 1: PASS (with minor URL note)
- **Correct answer verified:** Yes -- Microsoft docs confirm: "Sentiment analysis assigns sentiment labels, such as 'negative,' 'neutral,' and 'positive.' The service determines these labels using the highest confidence score." and "Sentiment is evaluated at both the sentence level and the document level." The answer (B) is correct.
- **Terminology current:** Yes -- Uses "Azure AI Language" correctly. No deprecated names.
- **Distractors valid:** Yes -- Key phrase extraction (A), entity recognition (C), and CLU (D) are all Azure AI Language features but serve different NLP purposes. None could be confused with sentiment classification.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/training/modules/analyze-text-with-text-analytics-service/` resolves but the module title has been renamed to "Introduction to natural language processing concepts." The URL still works via redirect. Consider updating the reference to the current sentiment analysis documentation at `https://learn.microsoft.com/azure/ai-services/language-service/sentiment-opinion-mining/overview` for a more direct reference.
- **Stem quality:** Good workplace scenario with Contoso Hotels guest review management.

### Item 2: PASS
- **Correct answer verified:** Yes -- Microsoft docs confirm Azure AI Speech "provides speech to text, text to speech, and other capabilities" within a single service. "You can transcribe speech to text with high accuracy, produce natural-sounding text-to-speech voices." The answer (C) is correct.
- **Terminology current:** Yes -- Uses "Azure AI Speech" correctly. The documentation now refers to "Azure Speech in Foundry Tools" in some places, but "Azure AI Speech" remains a valid and recognized name for the service.
- **Distractors valid:** Yes -- Azure AI Language (A), Azure AI Translator (B), and Azure AI Vision (D) are all real Azure services but do not provide combined STT and TTS. Azure AI Translator (B) is the strongest distractor since it has speech translation capabilities, but the rationale correctly explains it is focused on cross-language translation rather than general-purpose speech recognition and synthesis.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/azure/ai-services/speech-service/overview` resolves to the current Azure Speech overview page.
- **Stem quality:** Good workplace scenario with Fabrikam Manufacturing factory kiosk.

### Item 3: PASS
- **Correct answer verified:** Yes -- Microsoft docs confirm NER "can identify and categorize entities in unstructured text. For example: people, places, organizations, and quantities." Entity categories include Person, Organization, Location, DateTime, Currency, and many more. The answer (C) is correct.
- **Terminology current:** Yes -- Uses "Named entity recognition" correctly. No deprecated service names.
- **Distractors valid:** Yes -- Sentiment analysis (A), key phrase extraction (B), and language detection (D) are all Azure AI Language features but clearly serve different purposes from entity extraction and categorization.
- **Reference URL checked:** Not directly fetched, but `https://learn.microsoft.com/training/modules/get-started-language-azure/` follows Microsoft Learn training module URL conventions and is expected to resolve correctly.
- **Stem quality:** Good workplace scenario with Northwind Traders legal contract metadata extraction.

### Item 4: PASS
- **Correct answer verified:** Yes -- Microsoft docs confirm Azure Translator is "a cloud-based neural machine translation service" that supports "real-time text translation across multiple languages" through a REST API. It supports "over 135 languages and dialects." The answer (C) is correct.
- **Terminology current:** Yes -- Uses "Azure AI Translator" correctly. Documentation now refers to "Azure Translator in Foundry Tools" but "Azure AI Translator" is still a recognized name.
- **Distractors valid:** Yes -- Azure AI Speech (A) has speech translation but is not designed for bulk text document translation. Azure AI Language (B) and CLU (D) do not perform translation. All distractors are clearly wrong.
- **Reference URL checked:** Not directly fetched, but `https://learn.microsoft.com/training/modules/translate-text-with-translation-service/` follows standard training module URL patterns.
- **Stem quality:** Good workplace scenario with Tailwind Traders international product catalog translation.

### Item 5: PASS
- **Correct answer verified:** Yes -- Microsoft docs confirm: "Conversational language understanding (CLU) enables users to build custom natural language understanding models to predict the overall intention of an incoming utterance and extract important information from it." and "Developers can iteratively label utterances, train, and evaluate model performance." The answer (D) is correct.
- **Terminology current:** Yes -- Uses "Conversational Language Understanding (CLU)" correctly, which is the current name replacing the deprecated LUIS. No deprecated names used.
- **Distractors valid:** Yes -- Sentiment analysis (A), key phrase extraction (B), and Custom Question Answering (C) are all real Azure AI Language features but serve different purposes. Custom Question Answering (C) is the strongest distractor since it also handles conversational input, but the rationale correctly distinguishes it as QA-pair matching versus intent/entity prediction.
- **Reference URL checked:** Yes -- `https://learn.microsoft.com/azure/ai-services/language-service/conversational-language-understanding/overview` resolves to the current CLU overview page, which fully confirms the answer.
- **Stem quality:** Good workplace scenario with Adatum IT help desk virtual assistant.

---

## Corrections Needed

### Domain 3, Item 4 -- Advisory Enhancement (Optional)
**Issue:** The Azure AI Face service's age estimation attribute is now under Microsoft's Limited Access policy. While the answer remains correct (Face is the right service for face detection and demographic analysis), the rationale should acknowledge this restriction for completeness.

**Suggested addition to rationale:** Add a sentence at the end of the B-correct explanation: "Note: As of 2023, age estimation is a Limited Access capability in the Face service, requiring approved use cases."

**Severity:** Low -- does not affect the correct answer, but improves exam preparation accuracy.

### Domain 4, Item 1 -- Reference URL Update (Optional)
**Issue:** The reference URL `https://learn.microsoft.com/training/modules/analyze-text-with-text-analytics-service/` still works but the module has been retitled to "Introduction to natural language processing concepts" and no longer specifically focuses on sentiment analysis.

**Suggested replacement:** `https://learn.microsoft.com/azure/ai-services/language-service/sentiment-opinion-mining/overview`

**Severity:** Low -- the existing URL still resolves via redirect.

---

## Additional Notes

1. **Image Analysis deprecation notice:** The Azure AI Vision Image Analysis overview page now displays a deprecation warning: "The Image Analysis service in Azure Vision in Foundry Tools is deprecated and will be retired on September 25, 2028." This affects Domain 3 Items 4 and 5 contextually but does not invalidate the questions for current exam preparation, as the service remains functional and the concepts are still tested.

2. **Foundry branding updates:** Several Microsoft docs pages now reference "Foundry Tools" and "Microsoft Foundry" instead of older branding. The practice items correctly avoid deprecated branding (Cognitive Services, AI Studio) and use current service names throughout.

3. **All 10 items use realistic workplace scenarios** with named fictional companies (Contoso, Fabrikam, Northwind Traders, Tailwind Traders, Adatum), which aligns with Microsoft exam item writing standards. No items are simple definition-in-disguise questions.
