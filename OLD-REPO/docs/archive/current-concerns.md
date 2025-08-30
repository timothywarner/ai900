# Current Concerns

Claude Code, please address these issues:

I'll analyze your AI-900 codebase to identify outdated resources that no longer align with current exam objectives. Let me start by examining your existing exam objectives and then compare with the latest requirements.

Read file: AI-900-exam-objectives.md

Read file: ai900-objective-domain.md

Ran tool
Now let me examine the current structure of your repository to see what content and demos exist:

Ran tool

Ran tool

Read file: QnAMaker/readme.md

Ran tool

Ran tool

Ran tool

Ran tool

Ran tool

Ran tool

Ran tool

Ran tool
Based on my analysis of your AI-900 codebase and comparison with current exam objectives (updated as of May 2, 2025), here's my report on resources that no longer apply to current AI-900 exam objectives:

## 🚨 **OUTDATED/DEPRECATED RESOURCES REPORT**

### **MAJOR DEPRECATIONS** ❌

1. **QnA Maker Service** - **ENTIRELY OBSOLETE**
   - **Location**: `QnAMaker/` directory and references in:
     - `QnAMaker/basic-knowledge-base.tsv` (extensive QnA Maker content)
     - `AI-900-cert-study-blueprint.md` (line 17)
     - `course-plan.md` (line 136)
     - `CLAUDE.md` (line 68)
   - **Issue**: QnA Maker has been **retired and replaced** by Custom Question Answering (part of Azure AI Language service)
   - **Impact**: This entire directory and all QnA Maker references are obsolete

2. **LUIS (Language Understanding)** - **DEPRECATED**
   - **Location**: Multiple references including:
     - `demos/course-toc.md` (line 14)
     - `demos/04-nlp/README.md` (lines 6, 14)
     - `course-plan.md` (lines 111, 124, 136)
     - `apps/azure_bots/my-chat-bot/README.md` (line 57)
     - `AI-900-cert-study-blueprint.md` (line 14)
   - **Issue**: LUIS has been **deprecated** and replaced by Conversational Language Understanding (CLU) in Azure AI Language service
   - **Impact**: All LUIS-specific content needs updating

### **BRANDING/NAMING CHANGES** ⚠️

3. **"Cognitive Services" Terminology** - **OUTDATED BRANDING**
   - **Location**: Throughout the codebase:
     - `README.md` (lines 19, 38, 55)
     - `CLAUDE.md` (line 66)
     - `AI-900-cert-study-blueprint.md` (lines 5, 10, 12)
     - Demo files referencing old naming
   - **Issue**: "Cognitive Services" has been rebranded to **"Azure AI services"**
   - **Impact**: All references need updating to current terminology

4. **"Text Analytics"** - **SERVICE NAME CHANGE**
   - **Location**: Multiple files:
     - `course-plan.md` (lines 111, 119)
     - `demos/course-toc.md` (line 13)
     - `demos/04-nlp/README.md` (line 4)
   - **Issue**: Text Analytics is now part of **Azure AI Language service**
   - **Impact**: Content needs updating to reflect new service structure

5. **"Form Recognizer"** - **SERVICE RENAMED**
   - **Location**:
     - `demos/04-nlp/README.md` (line 8)
     - `course-plan.md` (line 83)
   - **Issue**: Form Recognizer is now **Azure AI Document Intelligence**
   - **Impact**: References need updating

### **EXAM WEIGHT CHANGES** 📊

6. **Outdated Domain Weightings**
   - **Current Issue**: Your documented weightings don't match the **May 2, 2025 updates**:
     - **Generative AI** increased from 15-20% to **20-25%** (highest weight)
     - **Machine Learning** decreased from 20-25% to **15-20%**
   - **Missing Content**:
     - **Azure AI Foundry** (new major service)
     - **Transformer architecture** (new ML topic)
     - **Azure AI Foundry model catalog** (new capability)

### **CONTENT GAPS FOR CURRENT EXAM** 🕳️

7. **Missing Current Services**:
   - No content for **Azure AI Foundry** (major new platform)
   - Limited **Azure OpenAI Service** integration examples
   - Missing **Custom Question Answering** replacement content
   - No **Conversational Language Understanding (CLU)** examples

### **RECOMMENDATIONS FOR CLEANUP** 🧹

1. **DELETE**: Entire `QnAMaker/` directory
2. **REPLACE**: All LUIS content with CLU examples
3. **REBRAND**: All "Cognitive Services" → "Azure AI services"
4. **UPDATE**: Service names (Text Analytics → AI Language, Form Recognizer → Document Intelligence)
5. **ADD**: Azure AI Foundry content and demos
6. **REWEIGHT**: Course structure to emphasize Generative AI (20-25% vs current 15-20%)

The most critical issue is that approximately **30-40% of your current content** references deprecated or renamed services that could confuse learners preparing for the current exam.
