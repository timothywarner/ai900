#!/usr/bin/env python3
"""
Advanced Prompt Engineering Patterns for Azure OpenAI
====================================================

This demo showcases prompt engineering techniques that bridge AI-900 to AI-102.
Learn patterns that improve accuracy, reduce hallucinations, and enable complex reasoning.

Prerequisites:
    pip install openai
    pip install python-dotenv
    pip install tiktoken

Azure Setup:
    1. Create Azure OpenAI resource
    2. Deploy GPT-4 or GPT-3.5-turbo model
    3. Update credentials below

Techniques Covered:
    1. Chain-of-Thought (CoT) Prompting
    2. Few-Shot Learning with Examples
    3. Self-Consistency Checking
    4. Role-Based Prompting
    5. Structured Output Generation
    6. Meta-Prompting (prompts about prompts)

AI-102 Preview:
    These patterns are essential for production AI systems where
    accuracy, consistency, and reliability are critical.
"""

import os
import json
import sys
from openai import AzureOpenAI

# Load configuration from environment variables
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
KEY = os.getenv("AZURE_OPENAI_KEY")
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")

# Validate environment variables
if not ENDPOINT or not KEY:
    print("❌ Error: Missing required environment variables!")
    print("Please set the following environment variables:")
    print("  - AZURE_OPENAI_ENDPOINT")
    print("  - AZURE_OPENAI_KEY")
    print("  - AZURE_OPENAI_DEPLOYMENT_NAME (optional, defaults to gpt-4o-mini)")
    print("  - AZURE_OPENAI_API_VERSION (optional, defaults to 2024-02-01)")
    print("\nRefer to tim-env.txt for setup instructions.")
    sys.exit(1)

# Initialize client
client = AzureOpenAI(
    api_key=KEY,
    api_version=API_VERSION,
    azure_endpoint=ENDPOINT
)


def basic_prompt(question):
    """Basic zero-shot prompt - starting point"""
    print("\n🔵 BASIC ZERO-SHOT PROMPT")
    print("=" * 60)
    print(f"Question: {question}")
    
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "user", "content": question}
        ],
        temperature=0.7
    )
    
    print(f"Answer: {response.choices[0].message.content}")
    return response.choices[0].message.content


def chain_of_thought_prompt(question):
    """Chain-of-Thought prompting for complex reasoning"""
    print("\n🧠 CHAIN-OF-THOUGHT PROMPT")
    print("=" * 60)
    print(f"Question: {question}")
    
    cot_prompt = f"""Please solve this step-by-step.

Question: {question}

Let's think through this carefully:
1. First, identify what we're looking for
2. Break down the problem into smaller parts
3. Solve each part
4. Combine the results
5. Verify the answer makes sense

Show your reasoning at each step."""
    
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that explains your reasoning step by step."},
            {"role": "user", "content": cot_prompt}
        ],
        temperature=0.3  # Lower temperature for reasoning tasks
    )
    
    print(f"Answer with reasoning:\n{response.choices[0].message.content}")
    return response.choices[0].message.content


def few_shot_learning(task, examples, new_input):
    """Few-shot learning with examples"""
    print("\n📚 FEW-SHOT LEARNING")
    print("=" * 60)
    print(f"Task: {task}")
    
    # Build the prompt with examples
    prompt = f"{task}\n\nExamples:\n"
    
    for i, example in enumerate(examples, 1):
        prompt += f"\nExample {i}:\nInput: {example['input']}\nOutput: {example['output']}\n"
    
    prompt += f"\nNow solve this:\nInput: {new_input}\nOutput:"
    
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "Follow the pattern shown in the examples exactly."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    
    print(f"\nExamples provided: {len(examples)}")
    print(f"New input: {new_input}")
    print(f"Generated output: {response.choices[0].message.content}")
    return response.choices[0].message.content


def self_consistency_check(question, num_samples=3):
    """Generate multiple answers and check consistency"""
    print("\n🔄 SELF-CONSISTENCY CHECK")
    print("=" * 60)
    print(f"Question: {question}")
    print(f"Generating {num_samples} independent answers...")
    
    answers = []
    
    for i in range(num_samples):
        response = client.chat.completions.create(
            model=DEPLOYMENT,
            messages=[
                {"role": "system", "content": "Provide a clear, concise answer."},
                {"role": "user", "content": question}
            ],
            temperature=0.8,  # Higher temperature for diversity
            seed=i  # Different seed for variation
        )
        answer = response.choices[0].message.content
        answers.append(answer)
        print(f"\nAnswer {i+1}: {answer}")
    
    # Ask the model to synthesize
    synthesis_prompt = f"""Given these {num_samples} answers to the question "{question}":

{chr(10).join([f"Answer {i+1}: {ans}" for i, ans in enumerate(answers)])}

Please:
1. Identify common elements across all answers
2. Note any contradictions
3. Provide a final, synthesized answer that represents the consensus
4. Rate your confidence (Low/Medium/High) based on answer consistency"""
    
    final_response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You are an expert at analyzing and synthesizing information."},
            {"role": "user", "content": synthesis_prompt}
        ],
        temperature=0.2
    )
    
    print(f"\n🎯 Synthesized Answer:\n{final_response.choices[0].message.content}")
    return final_response.choices[0].message.content


def structured_output_generation(data_description):
    """Generate structured data (JSON) reliably"""
    print("\n📊 STRUCTURED OUTPUT GENERATION")
    print("=" * 60)
    print(f"Generating structured data for: {data_description}")
    
    prompt = f"""Generate structured data for: {data_description}

Requirements:
1. Output must be valid JSON
2. Include relevant fields based on the description
3. Use appropriate data types (string, number, boolean, array)
4. Add realistic sample values

Output format:
```json
{{
  "field1": "value1",
  "field2": 123,
  "field3": true,
  "field4": ["item1", "item2"]
}}
```

Generate the JSON now:"""
    
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You are a JSON generator. Output only valid JSON without any markdown formatting or explanations."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        response_format={"type": "json_object"}  # Ensures JSON output
    )
    
    output = response.choices[0].message.content
    print(f"\nGenerated JSON:\n{output}")
    
    # Validate it's proper JSON
    try:
        parsed = json.loads(output)
        print("\n✅ Valid JSON generated!")
        print(f"Fields: {list(parsed.keys())}")
    except json.JSONDecodeError:
        print("\n❌ Invalid JSON generated")
    
    return output


def meta_prompting_optimization(task, initial_prompt):
    """Use AI to improve prompts - meta-prompting"""
    print("\n🔮 META-PROMPTING (AI improving prompts)")
    print("=" * 60)
    print(f"Task: {task}")
    print(f"Initial prompt: {initial_prompt}")
    
    optimization_prompt = f"""You are an expert prompt engineer. 

Task: {task}
Current prompt: "{initial_prompt}"

Please improve this prompt by:
1. Making instructions clearer and more specific
2. Adding constraints to prevent common errors
3. Including output format specifications
4. Adding examples if helpful
5. Optimizing for accuracy and consistency

Provide:
1. The improved prompt
2. Brief explanation of key improvements
3. Expected quality improvement (Low/Medium/High)"""
    
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You are an expert at crafting effective prompts for large language models."},
            {"role": "user", "content": optimization_prompt}
        ],
        temperature=0.4
    )
    
    print(f"\n🚀 Optimized Prompt:\n{response.choices[0].message.content}")
    return response.choices[0].message.content


def role_based_expert_prompting(question, role):
    """Role-based prompting for domain expertise"""
    print("\n👔 ROLE-BASED EXPERT PROMPTING")
    print("=" * 60)
    print(f"Question: {question}")
    print(f"Expert Role: {role}")
    
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": f"You are {role}. Answer based on your expertise, citing relevant principles and best practices from your field."},
            {"role": "user", "content": question}
        ],
        temperature=0.5
    )
    
    print(f"\nExpert Answer:\n{response.choices[0].message.content}")
    return response.choices[0].message.content


def main():
    """Demonstrate advanced prompt engineering patterns"""
    
    print("🚀 Advanced Prompt Engineering Demo")
    print("=" * 60)
    print("Exploring patterns that improve AI accuracy and reliability\n")
    
    # Demo 1: Chain of Thought
    math_question = "If a bakery sells 120 cookies on Monday, 150% more on Tuesday, and then half of Tuesday's amount on Wednesday, how many cookies were sold in total?"
    
    print("\n" + "="*80)
    print("COMPARISON: Basic vs Chain-of-Thought")
    print("="*80)
    
    basic_prompt(math_question)
    chain_of_thought_prompt(math_question)
    
    # Demo 2: Few-Shot Learning
    print("\n" + "="*80)
    print("FEW-SHOT LEARNING DEMO")
    print("="*80)
    
    sentiment_examples = [
        {"input": "This product exceeded my expectations!", "output": "Positive"},
        {"input": "Completely disappointed with the service.", "output": "Negative"},
        {"input": "It's okay, nothing special but does the job.", "output": "Neutral"}
    ]
    
    few_shot_learning(
        task="Classify the sentiment of customer reviews as Positive, Negative, or Neutral.",
        examples=sentiment_examples,
        new_input="The quality is amazing but the price is too high for what you get."
    )
    
    # Demo 3: Self-Consistency
    print("\n" + "="*80)
    print("SELF-CONSISTENCY DEMO")
    print("="*80)
    
    complex_question = "What are the three most important factors to consider when designing a scalable microservices architecture?"
    self_consistency_check(complex_question)
    
    # Demo 4: Structured Output
    print("\n" + "="*80)
    print("STRUCTURED OUTPUT DEMO")
    print("="*80)
    
    structured_output_generation("A customer order for an e-commerce platform including customer info, items, and shipping details")
    
    # Demo 5: Meta-Prompting
    print("\n" + "="*80)
    print("META-PROMPTING DEMO")
    print("="*80)
    
    meta_prompting_optimization(
        task="Extract key facts from news articles",
        initial_prompt="Summarize this article"
    )
    
    # Demo 6: Role-Based Expertise
    print("\n" + "="*80)
    print("ROLE-BASED EXPERTISE DEMO")
    print("="*80)
    
    technical_question = "How can we reduce latency in a distributed system?"
    
    role_based_expert_prompting(
        question=technical_question,
        role="a senior distributed systems architect with 20 years of experience at major tech companies"
    )
    
    print("\n\n✅ Advanced Prompt Engineering Demo Complete!")
    print("-" * 60)
    print("🎯 Key Takeaways:")
    print("  - Chain-of-Thought improves complex reasoning")
    print("  - Few-shot examples guide model behavior")
    print("  - Self-consistency reduces hallucinations")
    print("  - Structured outputs enable system integration")
    print("  - Meta-prompting optimizes prompt quality")
    print("  - Role-based prompting adds domain expertise")
    print("\n💡 These patterns are essential for AI-102 production systems!")


if __name__ == "__main__":
    main()