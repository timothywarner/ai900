# 🎯 Hour 1: AI Fundamentals & Azure AI Platform

**Duration:** 1 hour  
**Exam Weight:** 15-20%  
**Philosophy:** Start with a bang! Show the power of Azure AI in the first hour.

## 🎓 Exam Focus Areas
- **Identify features of common AI workloads**
- **Identify guiding principles for responsible AI**
- **Identify common types of AI workloads**
- **Identify Azure services for AI workloads**

## 📚 Key Concepts (10 min theory)
1. **AI vs ML vs Deep Learning**
   - AI: Simulation of human intelligence
   - ML: Algorithms that learn from data
   - Deep Learning: Neural networks with multiple layers

2. **Azure AI Services Categories**
   - Vision: See and understand
   - Language: Read and comprehend
   - Speech: Hear and speak
   - Decision: Make smart choices
   - OpenAI: Generate creative content

3. **Responsible AI Principles** (MEMORIZE THESE!)
   - ✅ Fairness
   - ✅ Reliability & Safety
   - ✅ Privacy & Security
   - ✅ Inclusiveness
   - ✅ Transparency
   - ✅ Accountability

## 🔥 Demo Scripts

### Demo 1: Azure Portal Tour (10 min)
```bash
# No code needed - Portal walkthrough
# 1. Navigate to portal.azure.com
# 2. Create Resource > AI + Machine Learning
# 3. Show all available AI services
# 4. Create a Computer Vision resource
# 5. Show Keys and Endpoint
# 6. Explain pricing tiers
```

### Demo 2: Multi-Service Demo (15 min)
```python
# multi-service-demo.py
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

# Setup (replace with your values)
cv_key = "YOUR_COMPUTER_VISION_KEY"
cv_endpoint = "YOUR_COMPUTER_VISION_ENDPOINT"
face_key = "YOUR_FACE_KEY"
face_endpoint = "YOUR_FACE_ENDPOINT"

# Initialize clients
cv_client = ComputerVisionClient(cv_endpoint, CognitiveServicesCredentials(cv_key))
face_client = FaceClient(face_endpoint, CognitiveServicesCredentials(face_key))

# Demo image
image_url = "https://aka.ms/ai900-images/people.jpg"

print("🔍 Computer Vision Analysis:")
# Analyze image
analysis = cv_client.analyze_image(image_url, visual_features=["Categories", "Description", "Objects"])
print(f"Description: {analysis.description.captions[0].text}")
print(f"Confidence: {analysis.description.captions[0].confidence:.2%}")

print("\n👤 Face Detection:")
# Detect faces
faces = face_client.face.detect_with_url(image_url, detection_model='detection_03', 
                                         return_face_attributes=['age', 'emotion'])
for face in faces:
    print(f"Age: {face.face_attributes.age}")
    print(f"Primary emotion: {max(face.face_attributes.emotion.__dict__, 
                                key=face.face_attributes.emotion.__dict__.get)}")
```

### Demo 3: Responsible AI Dashboard (5 min)
```python
# responsible-ai-demo.py
# This is a conceptual demo - explain while showing Azure ML Studio

"""
Key Points to Cover:
1. Model fairness metrics
2. Error analysis
3. Model interpretability
4. What-if scenarios

Navigate to: Azure ML Studio > Models > Select a model > Responsible AI dashboard
"""

print("🛡️ Responsible AI Checklist:")
checklist = [
    "✓ Is the model fair across different demographics?",
    "✓ Can we explain the model's decisions?",
    "✓ Have we tested for edge cases?",
    "✓ Is user privacy protected?",
    "✓ Do we have a feedback mechanism?"
]
for item in checklist:
    print(item)
```

## 💡 Exam Tips & Tricks

### ⚡ Quick Wins
1. **Service Selection**: Know which service for which task
   - Text in images? → Computer Vision OCR
   - Chatbot? → Bot Service + LUIS/QnA Maker
   - Translation? → Translator service
   - Content moderation? → Content Moderator

2. **Responsible AI Scenarios**: Common exam questions
   - "A loan approval system denies more loans to certain zip codes" → **Fairness** issue
   - "A medical diagnosis AI can't explain its decision" → **Transparency** issue
   - "A hiring AI only trained on male resumes" → **Inclusiveness** issue

3. **Cost Optimization**: Always mention in scenarios
   - Free tier available for most services
   - Pay-per-transaction model
   - Reserved capacity for high volume

### 📝 Practice Questions

**Q1:** Which Azure service would you use to extract text from scanned invoices?
- A) Azure Machine Learning
- B) Computer Vision OCR ✅
- C) Translator
- D) Bot Service

**Q2:** An AI system for hiring recommendations shows bias against certain groups. Which responsible AI principle is violated?
- A) Reliability
- B) Fairness ✅
- C) Privacy
- D) Accountability

**Q3:** What distinguishes Deep Learning from traditional Machine Learning?
- A) Deep Learning uses neural networks with multiple layers ✅
- B) Deep Learning is always more accurate
- C) Deep Learning requires less data
- D) Deep Learning is faster to train

## 🚀 Hands-on Challenge
Give learners 5 minutes to:
1. Create their own Computer Vision resource
2. Test it with a personal image
3. Share the most interesting insight the AI found

## 📌 Remember
- Keep energy HIGH - this sets the tone!
- Use real-world examples they can relate to
- Emphasize that AI-900 tests practical application, not theory
- Share your excitement about Azure AI capabilities

## 🔗 Resources
- [Azure AI Services Documentation](https://docs.microsoft.com/azure/cognitive-services/)
- [Responsible AI Principles](https://www.microsoft.com/ai/responsible-ai)
- [AI-900 Skills Measured](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE4wGpB)