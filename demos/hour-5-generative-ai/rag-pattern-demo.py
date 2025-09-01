#!/usr/bin/env python3
"""
Retrieval Augmented Generation (RAG) Pattern Demo
================================================

This demo shows a simple RAG pattern - combining document search with 
AI generation to answer questions using your own data.

RAG is essential for:
- Reducing hallucinations by grounding responses in real data
- Keeping information current without retraining
- Maintaining data privacy (your docs stay in your control)

Prerequisites:
    pip install openai
    pip install numpy
    pip install python-dotenv

Note: This is a simplified version. Production RAG uses:
- Azure AI Search for vector storage
- Chunking strategies for large documents
- Hybrid search (keyword + semantic)

AI-102 Preview:
    Full RAG implementation with Azure AI Search, embeddings,
    and production-grade retrieval strategies.
"""

import os
import json
import sys
import numpy as np
from openai import AzureOpenAI
from typing import List, Dict, Tuple

# Load configuration from environment variables
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
KEY = os.getenv("AZURE_OPENAI_KEY")
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-ada-002")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")

# Validate environment variables
if not ENDPOINT or not KEY:
    print("❌ Error: Missing required environment variables!")
    print("Please set the following environment variables:")
    print("  - AZURE_OPENAI_ENDPOINT")
    print("  - AZURE_OPENAI_KEY")
    print("  - AZURE_OPENAI_DEPLOYMENT_NAME (optional, defaults to gpt-4o-mini)")
    print("  - AZURE_OPENAI_EMBEDDING_DEPLOYMENT (optional, defaults to text-embedding-ada-002)")
    print("  - AZURE_OPENAI_API_VERSION (optional, defaults to 2024-02-01)")
    print("\nRefer to tim-env.txt for setup instructions.")
    sys.exit(1)

# Initialize client
client = AzureOpenAI(
    api_key=KEY,
    api_version=API_VERSION,
    azure_endpoint=ENDPOINT
)

# Sample knowledge base - In production, this would be Azure AI Search
KNOWLEDGE_BASE = [
    {
        "id": "doc1",
        "title": "Azure AI Services Overview",
        "content": "Azure AI Services (formerly Cognitive Services) provides pre-built AI models through APIs. Key services include Vision (image analysis, OCR, face detection), Language (sentiment analysis, entity recognition, translation), Speech (speech-to-text, text-to-speech), and Decision (anomaly detection, content moderation). These services require no ML expertise and can be integrated via REST APIs or SDKs.",
        "category": "overview"
    },
    {
        "id": "doc2",
        "title": "Azure Machine Learning Capabilities",
        "content": "Azure Machine Learning is a cloud platform for training, deploying, and managing ML models. It offers Automated ML for code-free model training, Designer for visual workflows, and Notebooks for code-first development. Key features include MLOps for model lifecycle management, responsible AI dashboard, and managed endpoints for deployment. Supports popular frameworks like TensorFlow, PyTorch, and scikit-learn.",
        "category": "machine-learning"
    },
    {
        "id": "doc3",
        "title": "Azure OpenAI Service",
        "content": "Azure OpenAI Service provides access to OpenAI's models including GPT-4, GPT-3.5, DALL-E 3, and Embeddings. It offers enterprise security, compliance, and responsible AI features. Key capabilities include text generation, code generation, summarization, and image creation. Supports fine-tuning for domain-specific tasks. Integrated with Azure's security and compliance frameworks including private endpoints and managed identity.",
        "category": "generative-ai"
    },
    {
        "id": "doc4",
        "title": "Responsible AI Principles",
        "content": "Microsoft's Responsible AI framework includes six principles: Fairness (AI systems should treat everyone fairly), Reliability & Safety (AI should perform reliably and safely), Privacy & Security (AI should be secure and respect privacy), Inclusiveness (AI should empower everyone), Transparency (AI systems should be understandable), and Accountability (People should be accountable for AI systems). Azure provides tools like Fairness Dashboard and Model Interpretability.",
        "category": "responsible-ai"
    },
    {
        "id": "doc5",
        "title": "Computer Vision Applications",
        "content": "Azure Computer Vision enables image analysis, OCR, and spatial analysis. Common applications include: inventory management using object detection, accessibility features using image descriptions, document digitization using OCR, safety monitoring using spatial analysis, and quality control in manufacturing. Custom Vision allows training models for specific domains without ML expertise.",
        "category": "computer-vision"
    }
]


def get_embedding(text: str) -> List[float]:
    """
    Generate embedding for text using Azure OpenAI.
    In this demo, we'll simulate embeddings for simplicity.
    """
    # In production, you would use:
    # response = client.embeddings.create(
    #     model=EMBEDDING_DEPLOYMENT,
    #     input=text
    # )
    # return response.data[0].embedding
    
    # Simulated embedding (random vector)
    np.random.seed(hash(text) % 1000)  # Consistent embeddings for same text
    return np.random.rand(384).tolist()  # 384-dim vector


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def search_documents(query: str, top_k: int = 3) -> List[Dict]:
    """
    Search for relevant documents using embeddings.
    Returns top-k most relevant documents.
    """
    print(f"\n🔍 Searching for: '{query}'")
    
    # Get query embedding
    query_embedding = get_embedding(query)
    
    # Calculate similarity scores
    scores = []
    for doc in KNOWLEDGE_BASE:
        doc_embedding = get_embedding(doc["content"])
        similarity = cosine_similarity(query_embedding, doc_embedding)
        scores.append((similarity, doc))
    
    # Sort by similarity and get top-k
    scores.sort(key=lambda x: x[0], reverse=True)
    top_docs = [doc for _, doc in scores[:top_k]]
    
    print(f"📄 Found {len(top_docs)} relevant documents:")
    for i, doc in enumerate(top_docs, 1):
        print(f"   {i}. {doc['title']} (category: {doc['category']})")
    
    return top_docs


def generate_answer(query: str, context_docs: List[Dict]) -> str:
    """
    Generate answer using retrieved documents as context.
    This is the 'Generation' part of RAG.
    """
    # Build context from retrieved documents
    context = "\n\n".join([
        f"Document: {doc['title']}\n{doc['content']}"
        for doc in context_docs
    ])
    
    # Create the RAG prompt
    system_prompt = """You are a helpful Azure AI assistant. Answer questions based ONLY on the provided context documents. 
If the answer is not in the context, say "I don't have information about that in my knowledge base."
Be concise and accurate. Cite which document you're referencing when possible."""
    
    user_prompt = f"""Context Documents:
{context}

Question: {query}

Answer based on the context above:"""
    
    # Generate response
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        max_tokens=500
    )
    
    return response.choices[0].message.content


def rag_query(query: str) -> Tuple[str, List[Dict]]:
    """
    Complete RAG pipeline: Retrieve relevant docs, then generate answer.
    """
    print("\n" + "="*60)
    print("🤖 RAG Query Processing")
    print("="*60)
    
    # Step 1: Retrieve relevant documents
    relevant_docs = search_documents(query, top_k=3)
    
    # Step 2: Generate answer using context
    print("\n✨ Generating answer...")
    answer = generate_answer(query, relevant_docs)
    
    return answer, relevant_docs


def compare_with_without_rag(query: str):
    """
    Compare responses with and without RAG to show the difference.
    """
    print("\n" + "="*80)
    print("📊 COMPARISON: With vs Without RAG")
    print("="*80)
    print(f"Question: {query}")
    
    # Without RAG (pure generation)
    print("\n❌ WITHOUT RAG (Pure Generation):")
    print("-" * 40)
    
    response_without_rag = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}
        ],
        temperature=0.3,
        max_tokens=200
    )
    print(response_without_rag.choices[0].message.content)
    
    # With RAG
    print("\n✅ WITH RAG (Grounded in Documents):")
    print("-" * 40)
    
    answer, docs = rag_query(query)
    print(f"\n💬 Answer: {answer}")
    
    print("\n📚 Sources used:")
    for doc in docs:
        print(f"  - {doc['title']}")


def interactive_demo():
    """
    Interactive Q&A using the RAG system.
    """
    print("\n" + "="*60)
    print("🎮 Interactive RAG Demo")
    print("="*60)
    print("Ask questions about Azure AI services!")
    print("Type 'quit' to exit, 'docs' to see available documents")
    
    while True:
        query = input("\n❓ Your question: ").strip()
        
        if query.lower() == 'quit':
            break
        elif query.lower() == 'docs':
            print("\n📚 Available documents:")
            for doc in KNOWLEDGE_BASE:
                print(f"  - {doc['title']} ({doc['category']})")
            continue
        elif not query:
            continue
        
        answer, sources = rag_query(query)
        print(f"\n💬 Answer: {answer}")


def main():
    """Demonstrate RAG pattern with Azure OpenAI"""
    
    print("🚀 Retrieval Augmented Generation (RAG) Demo")
    print("=" * 60)
    print("Combining search with generation for accurate, grounded responses\n")
    
    # Show available knowledge base
    print("📚 Knowledge Base Contents:")
    for doc in KNOWLEDGE_BASE:
        print(f"  - {doc['title']} ({doc['category']})")
    
    # Demo 1: Basic RAG query
    print("\n" + "="*80)
    print("DEMO 1: Basic RAG Query")
    print("="*80)
    
    answer, sources = rag_query("What are the key features of Azure Machine Learning?")
    print(f"\n💬 Answer: {answer}")
    
    # Demo 2: Compare with/without RAG
    print("\n" + "="*80)
    print("DEMO 2: Showing RAG Benefits")
    print("="*80)
    
    # Question about specific details that might hallucinate without context
    compare_with_without_rag("What are the six principles of Microsoft's Responsible AI framework?")
    
    # Demo 3: Multi-hop reasoning
    print("\n" + "="*80)
    print("DEMO 3: Multi-Document Reasoning")
    print("="*80)
    
    answer, sources = rag_query(
        "How can I use Azure services to build an AI application that analyzes images and follows responsible AI principles?"
    )
    print(f"\n💬 Answer: {answer}")
    
    # Demo 4: Handling unknown information
    print("\n" + "="*80)
    print("DEMO 4: Handling Information Not in Knowledge Base")
    print("="*80)
    
    answer, sources = rag_query("What is the pricing for Azure Quantum computing?")
    print(f"\n💬 Answer: {answer}")
    
    # Optional interactive mode
    print("\n" + "="*80)
    response = input("\n🎮 Would you like to try the interactive Q&A? (y/n): ")
    if response.lower() == 'y':
        interactive_demo()
    
    print("\n\n✅ RAG Pattern Demo Complete!")
    print("-" * 60)
    print("🎯 Key Takeaways:")
    print("  - RAG grounds AI responses in your actual data")
    print("  - Reduces hallucinations and improves accuracy")
    print("  - Keeps information current without retraining")
    print("  - Essential pattern for enterprise AI applications")
    print("\n💡 In AI-102, you'll implement production RAG with:")
    print("  - Azure AI Search for vector storage")
    print("  - Advanced chunking and retrieval strategies")
    print("  - Hybrid search combining keywords and semantics")
    print("  - Security and access control for documents")


if __name__ == "__main__":
    main()