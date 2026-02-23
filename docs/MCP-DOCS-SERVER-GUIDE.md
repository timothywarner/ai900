# Using Microsoft Docs MCP Server for AI-900 Cert Prep

## What is MCP (Model Context Protocol)?

The Model Context Protocol allows AI assistants to access external data sources in real-time. The Microsoft Docs MCP server gives Claude instant access to the entire Microsoft Learn documentation library - perfect for AI-900 exam prep!

## Quick Setup Guide

### Prerequisites

- Node.js 18+ installed
- Claude for Desktop (or compatible MCP client)
- GitHub account (for MCP server installation)

### Installation Steps

**1. Install the MS Docs MCP Server**

```bash
# Clone the Microsoft Docs MCP server
npx -y @modelcontextprotocol/create-server docs --template microsoft-docs

# Or install globally
npm install -g @modelcontextprotocol/server-microsoft-docs
```

**2. Configure Claude Desktop**

Edit your Claude configuration file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add this configuration:

```json
{
  "mcpServers": {
    "microsoft-docs": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-microsoft-docs"]
    }
  }
}
```

**3. Restart Claude Desktop**

The MS Docs server will now be available!

## Using MCP for AI-900 Study

### Example Study Prompts

**1. Deep Dive on Exam Topics**

```text
Using the Microsoft Docs MCP server, explain Azure Machine Learning automated ML
capabilities as tested in AI-900. Include code examples and best practices.
```

**2. Compare Services**

```text
Search Microsoft Learn docs and compare Azure AI Vision vs Custom Vision.
When would I use each for the AI-900 exam?
```

**3. Get Latest Updates**

```text
What are the latest updates to Azure OpenAI Service documented in Microsoft Learn?
Focus on features relevant to AI-900 certification.
```

**4. Practice Scenarios**

```text
Using MS Docs, create 5 AI-900 practice scenarios for responsible AI principles
with detailed explanations from official documentation.
```

**5. Hands-On Lab Guidance**

```text
Find the official Microsoft Learn quickstart for deploying an Azure Machine Learning
model and walk me through it step-by-step.
```

## AI-900 Focused Study Strategy

### Week 1-2: Fundamentals

Use MCP to research:

- Azure AI Services overview
- Responsible AI principles (search: "responsible AI Microsoft")
- Machine Learning basics (search: "Azure ML fundamentals")

**Example prompt:**

```text
Search Microsoft Learn for "Azure AI Fundamentals" and summarize the key concepts
I need to know for each exam domain: AI workloads, machine learning, computer vision,
NLP, and generative AI.
```

### Week 3: Computer Vision & NLP

**Example prompt:**

```text
Using Microsoft Docs MCP, explain the difference between:
1. Image classification vs object detection
2. OCR vs Document Intelligence
3. Face detection vs face recognition
Include code samples and when to use each.
```

### Week 4: Generative AI & Practice

**Example prompt:**

```text
Search Microsoft Learn for the latest Azure OpenAI Service documentation.
Explain prompt engineering best practices and content filtering for AI-900.
Then create 10 practice questions with detailed answers.
```

## Advanced MCP Features for Cert Prep

### 1. Compare Exam Versions

```text
Search Microsoft Learn for "AI-900 exam" and identify what changed between
the previous exam version and the May 2025 update.
```

### 2. Find Official Practice Labs

```text
Using MS Docs MCP, find all official AI-900 practice labs and learning paths.
Provide direct links and estimated completion times.
```

### 3. Service-Specific Deep Dives

```text
I'm struggling with Azure Machine Learning deployment concepts for AI-900.
Search MS Docs for deployment tutorials and explain:
- Real-time endpoints
- Batch endpoints
- Online vs offline deployment
```

### 4. Create Custom Study Notes

```text
Using Microsoft Learn docs, create comprehensive study notes for the
"Describe features of generative AI workloads on Azure" exam domain (20-25% weight).
Include:
- Key concepts
- Azure services involved
- Code examples
- Common exam scenarios
```

## Pro Tips for AI-900 with MCP

### 1. Always Verify Documentation Dates

```text
Search for "Azure OpenAI" and show me only documentation updated after January 2025
to ensure I'm studying current content for the May 2025 exam.
```

### 2. Cross-Reference Multiple Sources

```text
Compare the official AI-900 exam guide with Microsoft Learn training modules.
What topics are emphasized in the exam but might need extra study beyond the modules?
```

### 3. Generate Practice Questions

```text
Based on Microsoft Learn documentation for Azure AI Language service,
create 15 AI-900-style multiple choice questions covering:
- Sentiment analysis
- Key phrase extraction
- Entity recognition
Include detailed explanations for each answer.
```

### 4. Understand Service Limits & Quotas

```text
Search MS Docs for Azure AI Services quotas and limits. What are the free tier
limitations I should know for the AI-900 exam?
```

## Troubleshooting MCP Setup

### MCP Server Not Appearing in Claude

**Fix:**

1. Verify Node.js version: `node --version` (should be 18+)
2. Check Claude config file has correct JSON syntax
3. Restart Claude Desktop completely
4. Check Claude logs: `~/Library/Logs/Claude/mcp*.log`

### Connection Errors

**Fix:**

```bash
# Test the MCP server directly
npx @modelcontextprotocol/server-microsoft-docs --help

# Reinstall if needed
npm uninstall -g @modelcontextprotocol/server-microsoft-docs
npm install -g @modelcontextprotocol/server-microsoft-docs
```

### Slow Response Times

**Tips:**

- Be specific in search queries (use "AI-900" or "Azure AI")
- Limit scope to relevant documentation sections
- Use date filters for recent content

## Study Schedule with MCP

### Daily Study Routine (30-60 min/day)

**Day 1-5: AI Fundamentals**

- Morning: Use MCP to read official Azure AI overview docs
- Evening: Generate 5 practice questions on the day's topic

**Day 6-10: Machine Learning**

- Focus: AutoML, Designer, model deployment
- Use MCP to find hands-on tutorials and code samples

**Day 11-15: Computer Vision**

- Practice: Image analysis, OCR, face detection scenarios
- Generate comparison tables using MS Docs

**Day 16-20: NLP**

- Deep dive: Language Understanding, Q&A, Speech
- Create flashcards from official documentation

**Day 21-25: Generative AI (HIGHEST WEIGHT!)**

- Emphasis: Azure OpenAI, prompt engineering, responsible AI
- Use MCP to find latest Azure AI Foundry documentation

**Day 26-30: Review & Practice**

- Generate full-length practice exams using MCP
- Review weak areas with targeted MS Docs searches

## MCP Commands Quick Reference

```bash
# Search for specific topic
"Search Microsoft Docs for [topic]"

# Get recent updates
"Show me Microsoft Learn updates for Azure AI from the last 3 months"

# Find code examples
"Find Python code examples for Azure Computer Vision in MS Docs"

# Compare services
"Compare Azure AI Language vs Azure OpenAI using official documentation"

# Get official learning paths
"List all Microsoft Learn paths for AI-900 certification"

# Find pricing info
"What does Microsoft Docs say about Azure AI Services pricing tiers?"
```

## Resources

- [MCP Documentation](https://modelcontextprotocol.org/)
- [Microsoft Learn AI-900](https://learn.microsoft.com/credentials/certifications/azure-ai-fundamentals/)
- [Azure AI Documentation](https://learn.microsoft.com/azure/ai-services/)
- [Claude Desktop](https://claude.ai/download)

---

**Pro Tip**: Combine MCP with traditional study methods! Use MCP to quickly find official docs, then practice with hands-on labs and practice exams.

*Last Updated: November 2025*
