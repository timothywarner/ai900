# 👁️ Hour 3: Computer Vision Workloads

**Duration:** 1 hour  
**Exam Weight:** 15-20%  
**Philosophy:** Make computers "see" - visual demos that wow!

## 🎓 Exam Focus Areas
- **Identify common types of computer vision solutions**
- **Identify Azure tools and services for computer vision tasks**
- **Understand image classification vs object detection**
- **Know OCR capabilities and use cases**

## 📚 Key Concepts (5 min theory)

### Service Comparison (MEMORIZE!)
| Service | Use Case | Key Feature |
|---------|----------|-------------|
| **Computer Vision** | General image analysis | Pre-built, ready to use |
| **Custom Vision** | Specific to your needs | Train with your images |
| **Face** | People & emotions | Privacy-focused |
| **Form Recognizer** | Documents & forms | Structured data extraction |

### Vision Tasks
1. **Image Classification**: What is it? (cat, dog, car)
2. **Object Detection**: Where is it? (bounding boxes)
3. **OCR**: What text is there? (printed, handwritten)
4. **Face Detection**: Who is it? (identity, emotion, age)

## 🔥 Demo Scripts

### Demo 1: Computer Vision Deep Dive (15 min)
```python
# computer-vision-demo.py
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import time

# Setup
key = "YOUR_COMPUTER_VISION_KEY"
endpoint = "YOUR_COMPUTER_VISION_ENDPOINT"
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

# Demo 1: Analyze an image
print("🔍 DEMO 1: Image Analysis")
image_url = "https://aka.ms/azureimages/mountain.jpg"

# Get image description
description = client.describe_image(image_url)
print(f"Description: {description.captions[0].text}")
print(f"Confidence: {description.captions[0].confidence:.2%}")

# Detect objects
print("\n📦 DEMO 2: Object Detection")
objects = client.detect_objects(image_url)
for obj in objects.objects:
    print(f"Found {obj.object_property} at [{obj.rectangle.x}, {obj.rectangle.y}]")
    print(f"Confidence: {obj.confidence:.2%}")

# OCR Demo
print("\n📄 DEMO 3: OCR - Read Text")
read_image_url = "https://aka.ms/azureimages/handwritten.jpg"

# Start the Read operation
read_response = client.read(read_image_url, raw=True)
operation_location = read_response.headers["Operation-Location"]
operation_id = operation_location.split("/")[-1]

# Wait for results
while True:
    result = client.get_read_result(operation_id)
    if result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print text
if result.status == OperationStatusCodes.succeeded:
    for page in result.analyze_result.read_results:
        for line in page.lines:
            print(line.text)

# Spatial Analysis teaser
print("\n🏢 DEMO 4: Spatial Analysis (Preview)")
print("Imagine: Counting people in stores, social distancing, queue management")
print("This requires Computer Vision container + edge device")
```

### Demo 2: Custom Vision Project (15 min)
```python
# custom-vision-demo.py
"""
Live Demo Script - Build a Hot Dog Classifier!

1. Go to customvision.ai
2. Create new project:
   - Name: "Hot Dog Detector"
   - Project Type: Classification
   - Classification Type: Multiclass
   - Domain: Food (compact)

3. Upload images:
   - 5-10 hot dog images (tag: "hotdog")
   - 5-10 not hot dog images (tag: "nothotdog")

4. Train:
   - Click "Train" → Quick Training
   - Watch the precision/recall metrics

5. Test:
   - Use "Quick Test" with new images
   - Show confidence scores

6. Export:
   - Show export options (TensorFlow, CoreML, ONNX)
   - Explain edge deployment scenarios
"""

# Test the trained model
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

prediction_key = "YOUR_PREDICTION_KEY"
prediction_endpoint = "YOUR_PREDICTION_ENDPOINT"
project_id = "YOUR_PROJECT_ID"
iteration_name = "YOUR_ITERATION_NAME"

predictor = CustomVisionPredictionClient(prediction_key, endpoint=prediction_endpoint)

test_image_url = "https://example.com/mystery-food.jpg"
results = predictor.classify_image_url(project_id, iteration_name, test_image_url)

for prediction in results.predictions:
    print(f"{prediction.tag_name}: {prediction.probability:.2%}")
```

### Demo 3: Face API Features (10 min)
```python
# face-api-demo.py
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

# Setup
face_key = "YOUR_FACE_KEY"
face_endpoint = "YOUR_FACE_ENDPOINT"
face_client = FaceClient(face_endpoint, CognitiveServicesCredentials(face_key))

# Detect faces with attributes
print("😊 Face Detection with Emotions")
image_url = "https://aka.ms/azureimages/happy-family.jpg"

faces = face_client.face.detect_with_url(
    url=image_url,
    return_face_attributes=['age', 'gender', 'emotion', 'glasses', 'hair']
)

for i, face in enumerate(faces):
    print(f"\nPerson {i+1}:")
    print(f"  Age: {face.face_attributes.age}")
    print(f"  Gender: {face.face_attributes.gender}")
    print(f"  Glasses: {face.face_attributes.glasses}")
    
    # Find dominant emotion
    emotions = face.face_attributes.emotion
    emotion_dict = {
        'anger': emotions.anger,
        'contempt': emotions.contempt,
        'disgust': emotions.disgust,
        'fear': emotions.fear,
        'happiness': emotions.happiness,
        'neutral': emotions.neutral,
        'sadness': emotions.sadness,
        'surprise': emotions.surprise
    }
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    print(f"  Emotion: {dominant_emotion} ({emotion_dict[dominant_emotion]:.1%})")

# Face Verification demo
print("\n🔍 Face Verification: Are these the same person?")
# Compare two faces - returns confidence they're the same person
```

## 💡 Exam Tips & Tricks

### ⚡ Service Selection Guide
**"Which service should I use?"** - Common exam question!

| Scenario | Service | Why |
|----------|---------|-----|
| Read street signs | Computer Vision OCR | Pre-built, works immediately |
| Identify company logos | Custom Vision | Need to train on specific logos |
| Verify employee identity | Face API | Designed for face verification |
| Extract data from invoices | Form Recognizer | Structured document data |
| Analyze store traffic | Spatial Analysis | People counting & movement |

### 🎯 Key Differentiators
1. **Computer Vision vs Custom Vision**
   - Computer Vision: 86+ categories pre-trained
   - Custom Vision: You define categories, min 5 images each

2. **Face Detection vs Face Recognition**
   - Detection: Find faces, get attributes
   - Recognition: Match faces to identities (requires training)

3. **OCR vs Form Recognizer**
   - OCR: Just extract text
   - Form Recognizer: Understand document structure

### 📝 Practice Questions

**Q1:** You need to count people entering a store. Which service?
- A) Face API
- B) Custom Vision
- C) Computer Vision with Spatial Analysis ✅
- D) Form Recognizer

**Q2:** What's the minimum number of images needed per tag in Custom Vision?
- A) 1
- B) 5 ✅
- C) 10
- D) 50

**Q3:** You want to extract text from handwritten notes. Which feature?
- A) Computer Vision Image Analysis
- B) Computer Vision OCR/Read API ✅
- C) Custom Vision
- D) Face API

**Q4:** A company wants to verify that the person using a keycard matches their photo ID. Which service?
- A) Computer Vision
- B) Custom Vision
- C) Face API ✅
- D) Form Recognizer

## 🚀 Hands-on Challenge
**Vision Scavenger Hunt:**
1. Take a photo with your phone
2. Upload to Computer Vision
3. Find the most unusual object/tag detected
4. Share with the class!

## 📌 Remember
- Always show visual results - this is COMPUTER VISION!
- Emphasize privacy/ethics when using Face API
- Custom Vision is perfect for domain-specific needs
- AI-900 loves "which service for which scenario" questions

## 🔗 Resources
- [Computer Vision Documentation](https://docs.microsoft.com/azure/cognitive-services/computer-vision/)
- [Custom Vision Portal](https://customvision.ai)
- [Face API Documentation](https://docs.microsoft.com/azure/cognitive-services/face/)
- [OCR Language Support](https://docs.microsoft.com/azure/cognitive-services/computer-vision/language-support) 