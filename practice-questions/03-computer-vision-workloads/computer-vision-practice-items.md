---
exam: AI-900
domain: "Describe features of computer vision workloads on Azure"
weight: "15-20%"
item_count: 5
cognitive_level: Apply
generated: 2026-02-23
---

# Domain 3: Features of Computer Vision Workloads on Azure

Practice items for AI-900 exam preparation.

---

### Item 1
**Objective:** Identify features of image classification solutions
**Cognitive Level:** Apply

**Stem:**
Contoso Vineyards grows three grape varieties across 500 acres. The viticulture team wants to build an AI solution that analyzes drone photographs of vine rows and determines which grape variety is growing in each section. The model should assign a single label per image indicating the grape variety. Which type of computer vision solution should Contoso use?

A) Object detection
B) Image classification
C) Optical character recognition
D) Facial detection

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because image classification assigns a single class label to an entire image. Contoso needs each drone photo labeled with the grape variety it depicts, which is the definition of an image classification task.
- **A is incorrect** because object detection identifies and locates multiple objects within an image using bounding boxes. Contoso does not need to locate individual objects -- they need a single label per image.
- **C is incorrect** because optical character recognition (OCR) extracts printed or handwritten text from images. There is no text extraction requirement in this scenario.
- **D is incorrect** because facial detection identifies human faces in images. This scenario involves identifying grape varieties, not people.

**Reference:** https://learn.microsoft.com/training/modules/analyze-images-computer-vision/

</details>

---

### Item 2
**Objective:** Identify features of object detection solutions; Describe capabilities of the Azure AI Vision service
**Cognitive Level:** Apply

**Stem:**
Fabrikam Retail is deploying smart cameras in its warehouse. The operations team needs a solution that can identify each type of product on the shelves and provide the exact location of every item within the camera frame so that inventory robots know where to pick items. Which type of computer vision solution best meets this requirement?

A) Image classification
B) Semantic segmentation
C) Object detection
D) Optical character recognition

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because object detection identifies multiple objects in an image and returns a class label together with bounding box coordinates for each detected object. This gives the inventory robots both the product type and the precise location within the frame.
- **A is incorrect** because image classification assigns a single label to the entire image. It would tell Fabrikam what product category dominates the image but would not provide the location of individual items.
- **B is incorrect** because semantic segmentation classifies every pixel in an image into a category. While it can show object boundaries, it does not inherently provide discrete object instances with bounding boxes, which is what the robots need for pick-and-place operations.
- **D is incorrect** because OCR extracts text from images. The scenario requires identifying and locating physical products, not reading text.

**Reference:** https://learn.microsoft.com/training/modules/detect-objects-images/

</details>

---

### Item 3
**Objective:** Identify features of optical character recognition solutions; Describe capabilities of the Azure AI Vision service
**Cognitive Level:** Apply

**Stem:**
Northwind Traders receives thousands of handwritten order forms daily from field sales representatives. The logistics team needs to digitize these forms by extracting the handwritten text so it can be imported into their order management system. The forms contain structured fields such as customer name, order number, and line items. Which Azure service should Northwind Traders use?

A) Azure AI Vision Image Analysis
B) Azure AI Face
C) Azure AI Document Intelligence
D) Azure AI Language

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because Azure AI Document Intelligence (formerly Form Recognizer) is specifically designed to extract text, key-value pairs, tables, and structure from documents such as forms, invoices, and receipts. It handles both printed and handwritten text in structured documents, making it the best fit for digitizing order forms with defined fields.
- **A is incorrect** because Azure AI Vision Image Analysis provides OCR for general images like photos of signs or labels. While it can extract text, it is optimized for lightweight, non-document scenarios and does not provide structured field extraction from forms.
- **B is incorrect** because Azure AI Face detects and analyzes human faces in images. It does not extract text from documents.
- **D is incorrect** because Azure AI Language provides natural language processing capabilities such as sentiment analysis and entity recognition. It processes existing text but does not extract text from images or scanned documents.

**Reference:** https://learn.microsoft.com/azure/ai-services/document-intelligence/overview

</details>

---

### Item 4
**Objective:** Identify features of facial detection and facial analysis solutions; Describe capabilities of the Azure AI Face detection service
**Cognitive Level:** Apply

**Stem:**
Tailwind Traders is building a customer experience application for its flagship store. The application uses cameras at the entrance to detect when customers arrive and estimate demographic attributes such as approximate age to personalize digital signage. The application does NOT need to identify specific individuals. Which Azure service should Tailwind Traders use?

A) Azure AI Document Intelligence
B) Azure AI Vision Image Analysis with the Read feature
C) Azure AI Face
D) Azure AI Language

<details>
<summary>Show Answer</summary>

**Correct Answer:** C

**Rationale:**
- **C is correct** because the Azure AI Face service can detect human faces in images and return face attributes such as estimated age, head pose, and other facial characteristics. Tailwind Traders needs face detection with age estimation, which is a core capability of this service. Note: Age estimation is currently a Limited Access attribute in the Face service, meaning approved use cases are required to access this capability.
- **A is incorrect** because Azure AI Document Intelligence extracts text and structure from documents. It has no face detection or analysis capabilities.
- **B is incorrect** because the Read feature of Azure AI Vision Image Analysis is an OCR capability that extracts text from images. While Image Analysis can detect people, the dedicated Face service provides the demographic attribute analysis that Tailwind Traders requires.
- **D is incorrect** because Azure AI Language processes natural language text for tasks like sentiment analysis and entity recognition. It does not analyze visual content or detect faces.

**Reference:** https://learn.microsoft.com/azure/ai-services/computer-vision/overview-identity

</details>

---

### Item 5
**Objective:** Describe capabilities of the Azure AI Vision service
**Cognitive Level:** Apply

**Stem:**
Adatum Corporation is developing a mobile app for its field technicians. When a technician photographs a piece of industrial equipment, the app should generate a natural language description of the image so that technicians with visual impairments can understand what is shown. The images are general photographs, not documents. Which feature of the Azure AI Vision service should Adatum use?

A) The Read (OCR) feature
B) The Image Analysis Caption feature
C) The Face detection feature
D) The Smart Crop feature

<details>
<summary>Show Answer</summary>

**Correct Answer:** B

**Rationale:**
- **B is correct** because the Caption feature of Azure AI Vision Image Analysis generates a human-readable natural language sentence describing the content of an image. This directly addresses the requirement to provide a text description of equipment photographs for accessibility purposes.
- **A is incorrect** because the Read (OCR) feature extracts printed or handwritten text that already exists within an image. Adatum needs a description of visual content, not extraction of existing text.
- **C is incorrect** because Face detection identifies and analyzes human faces in images. The scenario involves photographs of industrial equipment, not people.
- **D is incorrect** because Smart Crop generates cropped thumbnails of images based on the area of interest. It does not produce natural language descriptions of image content.

**Reference:** https://learn.microsoft.com/azure/ai-services/computer-vision/overview-image-analysis

</details>
