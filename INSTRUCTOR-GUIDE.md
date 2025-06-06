# 🎓 AI-900 Instructor Guide
## Tim Warner's Ultimate Teaching Companion

**Welcome to your AI-900 teaching powerhouse!** 🚀 This guide will help you deliver an **epic** learning experience using the unified demo application.

---

## 🎯 **Quick Instructor Setup (5 Minutes)**

### 1. **Environment Setup**
```bash
# Clone and prep
git clone https://github.com/timothywarner/ai900.git
cd ai900
npm install

# Copy your actual environment
cp .env .env.backup  # Keep your real keys safe!
cp .env.example .env.instructor  # For students
```

### 2. **Pre-Class Checklist** ✅
- [ ] **Azure resources** deployed (ai900-rg + openai-rg)
- [ ] **Environment variables** loaded (use the .env we created)
- [ ] **Port 3000** is free (`npm run force-close`)
- [ ] **Demo assets** accessible (they're in `/assets/`)
- [ ] **Screen sharing** setup (console + web browser)

### 3. **Teaching Flow** 🎬
```bash
# Start with console demo
npm run dev

# When ready for web interface
npm run web
# Browser: http://localhost:3000
```

---

## 🎨 **Demo Scenarios by Exam Domain**

### **Domain 1: AI Workloads & Considerations (15-20%)**
**🎯 Learning Objective**: Understand AI types and responsible AI

**Console Demo Path**:
1. Launch app → Show main menu (demonstrates AI service breadth)
2. Pick any service → Show warnings about responsible AI
3. Emphasize **Contoso branding** (realistic business context)

**Key Teaching Points**:
- **Multi-service approach** (one endpoint, many capabilities)
- **Responsible AI** principles embedded in demos
- **Real-world scenarios** with Contoso use cases

### **Domain 2: Machine Learning on Azure (20-25%)**
**🎯 Learning Objective**: ML concepts and Azure ML Studio

**Demo Strategy**:
- Use **console app** to show ML concepts in practice
- **Computer Vision** demo → Explain supervised learning
- **Language Service** → Show classification models
- **Document Intelligence** → Demonstrate feature extraction

**Teaching Script**:
```
"Notice how our Contoso AI is making predictions with confidence scores.
This is machine learning in action - the model was trained on thousands
of similar examples to recognize patterns."
```

### **Domain 3: Computer Vision (15-20%)**
**🎯 Learning Objective**: Image analysis and OCR capabilities

**🔥 Best Demo Flow**:
1. **Console**: Computer Vision → People (celebrity recognition)
2. **Console**: Products → Carrot analysis (object detection)
3. **Console**: OCR → Business card text extraction
4. **Web**: Upload student images for live analysis

**Assets to Use**:
- `/assets/People/celebrity01.jpg` (face detection)
- `/assets/Things/Carrot1.JPG` (object detection)
- `/assets/OCR/business-card-english.jpg` (OCR)

### **Domain 4: Natural Language Processing (15-20%)**
**🎯 Learning Objective**: Text analysis and speech services

**Interactive Demo**:
1. **Console**: Language Service with pre-loaded customer reviews
2. **Web**: Let students type their own text for analysis
3. Show **sentiment analysis** with emoji feedback
4. Demonstrate **key phrase extraction**

**Student Engagement**:
```
"Let's analyze some customer feedback about Contoso products.
Type something positive... now something negative...
Watch how the AI understands emotion!"
```

### **Domain 5: Generative AI (15-20%) - HIGHEST WEIGHT!**
**🎯 Learning Objective**: Azure OpenAI and prompt engineering

**🚀 Premium Demo Experience**:
1. **Console**: Azure OpenAI demo with business scenarios
2. **Web**: Live chat with Contoso AI assistant
3. Show **prompt engineering** examples
4. Demonstrate **responsible AI** guardrails

**Sample Prompts for Live Demo**:
- "Write a professional email to apologize for a delayed shipment"
- "Create marketing copy for Contoso's new product"
- "Explain quantum computing in simple terms"

---

## 🎭 **Teaching Techniques**

### **The Contoso Story Method** 📚
Always frame demos as **real business scenarios**:
- "Contoso needs to analyze customer sentiment..."
- "Our AI helps Contoso process invoices automatically..."
- "Contoso's marketing team uses computer vision to..."

### **Progressive Complexity** 📈
1. **Start Simple**: Multi-service demos (one key, many features)
2. **Add Complexity**: Individual service configurations
3. **Real-World**: Custom scenarios with student data

### **Interactive Engagement** 🎯
- **Console demos**: Great for concepts and flow
- **Web interface**: Perfect for hands-on student participation
- **Asset library**: Pre-loaded examples + student uploads

---

## 🔧 **Troubleshooting Guide**

### **Common Issues & Fixes**

| Problem | Quick Fix | Teaching Moment |
|---------|-----------|-----------------|
| Port 3000 busy | `npm run force-close` | "Always clean up resources!" |
| Missing .env | Copy from .env.example | "Configuration management is key" |
| API rate limits | Use placeholder responses | "Production apps need throttling" |
| Service timeouts | Check Azure resource status | "Monitoring is essential" |

### **Student Environment Issues**
```bash
# Students can't get Azure resources?
# Use the placeholder/demo modes in the web interface
# They'll still learn concepts without spending money
```

### **Demo Backup Plans**
- **No internet?** Use console demos with cached responses
- **Azure issues?** Web interface has mock responses built-in
- **Time running short?** Focus on highest-weighted domain (Generative AI)

---

## 📊 **Timing Guide for 5-Hour Course**

| Hour | Domain | Demo Focus | Time Split |
|------|--------|------------|------------|
| 1 | AI Fundamentals | Console overview + responsible AI | 30min demo, 30min concept |
| 2 | Machine Learning | Computer Vision + concept explanation | 40min demo, 20min theory |
| 3 | Computer Vision | Full vision demo suite + hands-on | 45min demo, 15min Q&A |
| 4 | NLP | Language + Speech demos + interaction | 45min demo, 15min practice |
| 5 | Generative AI | OpenAI deep dive + prompt engineering | 50min demo, 10min wrap-up |

---

## 🎯 **Advanced Teaching Features**

### **Real-Time Asset Usage**
Students can upload their own:
- **Images** → Computer Vision analysis
- **Documents** → Document Intelligence extraction
- **Text** → Language Service processing

### **Contoso Scenarios Library**
Pre-built business cases:
- **Retail**: Product catalog analysis
- **Healthcare**: Document processing (mock data)
- **Manufacturing**: Quality control imaging
- **Customer Service**: Sentiment monitoring

### **Assessment Integration**
Use demos to reinforce exam concepts:
- **Show confidence scores** → Explain ML accuracy
- **Display multiple services** → Emphasize multi-service approach
- **Demonstrate failures** → Discuss limitations and responsible AI

---

## 📞 **Need Help? Tim's Got Your Back!**

**During Live Teaching**:
- Console app has built-in error handling
- Web interface gracefully handles missing services
- All demos work with or without full Azure setup

**Contact Info**:
- **Email**: tim@techtrainertim.com
- **LinkedIn**: timothywarner
- **GitHub Issues**: For technical problems

**Remember**: You're not just teaching Azure AI - you're **empowering the next generation of AI practitioners!** 🚀

---

*"The best demos don't just show what AI can do - they inspire learners to imagine what they'll build next."* - Tim Warner
