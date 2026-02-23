"""
Azure AI Language Service Demo - AI-900
This script demonstrates using Azure AI Language service for:
1. Sentiment analysis
2. Key phrase extraction
3. Entity recognition
4. Language detection
5. Text translation

Requirements:
- Azure subscription
- Azure AI Language resource
- Azure AI Translator resource
"""

import os
import requests
import uuid
import json
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Add your Language service key and endpoint
import os

language_key = os.getenv("TWAI900LANGSERVICE1_KEY")
language_endpoint = os.getenv("TWAI900LANGSERVICE1_ENDPOINT")

# Add your Translator service key and endpoint
translator_key = os.getenv("TWAI900TRANSLATOR1_KEY")
translator_endpoint = os.getenv("TWAI900TRANSLATOR1_ENDPOINT")
translator_location = "eastus"  # Update if needed

# Initialize the Language client
text_analytics_client = TextAnalyticsClient(
    endpoint=language_endpoint, credential=AzureKeyCredential(language_key)
)


# ------ Sentiment Analysis Example ------
def analyze_sentiment(documents):
    """Analyze sentiment in text"""
    print("\n===== Sentiment Analysis =====")

    # Analyze sentiment
    result = text_analytics_client.analyze_sentiment(documents=documents)
    docs = [doc for doc in result if not doc.is_error]

    for idx, doc in enumerate(docs):
        print(f"\nDocument {idx + 1}:")
        print(f"- Text: {documents[idx]}")
        print(f"- Overall sentiment: {doc.sentiment}")
        print(
            f"- Scores: Positive={doc.confidence_scores.positive:.2f}, Neutral={doc.confidence_scores.neutral:.2f}, Negative={doc.confidence_scores.negative:.2f}"
        )

        # Analyze sentiment by sentence
        for sentence_idx, sentence in enumerate(doc.sentences):
            print(f"  Sentence {sentence_idx + 1}: '{sentence.text}'")
            print(f"  - Sentiment: {sentence.sentiment}")
            print(
                f"  - Scores: Positive={sentence.confidence_scores.positive:.2f}, Neutral={sentence.confidence_scores.neutral:.2f}, Negative={sentence.confidence_scores.negative:.2f}"
            )


# ------ Key Phrase Extraction Example ------
def extract_key_phrases(documents):
    """Extract key phrases from text"""
    print("\n===== Key Phrase Extraction =====")

    # Extract key phrases
    result = text_analytics_client.extract_key_phrases(documents=documents)
    docs = [doc for doc in result if not doc.is_error]

    for idx, doc in enumerate(docs):
        print(f"\nDocument {idx + 1}:")
        print(f"- Text: {documents[idx]}")
        print(f"- Key phrases: {', '.join(doc.key_phrases)}")


# ------ Entity Recognition Example ------
def recognize_entities(documents):
    """Recognize entities in text"""
    print("\n===== Entity Recognition =====")

    # Recognize entities
    result = text_analytics_client.recognize_entities(documents=documents)
    docs = [doc for doc in result if not doc.is_error]

    for idx, doc in enumerate(docs):
        print(f"\nDocument {idx + 1}:")
        print(f"- Text: {documents[idx]}")
        for entity in doc.entities:
            print(
                f"- Entity: {entity.text} (Category: {entity.category}, Subcategory: {entity.subcategory}, Confidence: {entity.confidence_score:.2f})"
            )


# ------ Language Detection Example ------
def detect_language(documents):
    """Detect language of text"""
    print("\n===== Language Detection =====")

    # Detect language
    result = text_analytics_client.detect_language(documents=documents)
    docs = [doc for doc in result if not doc.is_error]

    for idx, doc in enumerate(docs):
        print(f"\nDocument {idx + 1}:")
        print(f"- Text: {documents[idx]}")
        print(
            f"- Detected language: {doc.primary_language.name} ({doc.primary_language.iso6391_name})"
        )
        print(f"- Confidence score: {doc.primary_language.confidence_score:.2f}")


# ------ Text Translation Example ------
def translate_text(text, target_language):
    """Translate text to another language"""
    print("\n===== Text Translation =====")

    # Endpoint for the Translator Text API
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"

    # Set up the request parameters
    params = {"api-version": "3.0", "to": target_language}

    # Set up the request headers
    headers = {
        "Ocp-Apim-Subscription-Key": translator_key,
        "Ocp-Apim-Subscription-Region": translator_location,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }

    # Set up the request body
    body = [{"text": text}]

    # Make the request
    response = requests.post(endpoint, params=params, headers=headers, json=body)
    result = response.json()

    # Print the result
    print(f"\nOriginal text: {text}")
    print(f"Target language: {target_language}")
    print(f"Translated text: {result[0]['translations'][0]['text']}")

    return result[0]["translations"][0]["text"]


def main():
    """Main function to run all demos"""
    # Sample documents for analysis
    documents = [
        "I had a wonderful experience! The rooms were wonderful and the staff was helpful.",
        "The restaurant was not good. The food was bland and overpriced.",
        "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, in Albuquerque, New Mexico.",
    ]

    # Run language analysis demos
    analyze_sentiment(documents)
    extract_key_phrases(documents)
    recognize_entities(documents)
    detect_language(documents)

    # Sample text for translation
    text_to_translate = "This is a demonstration of the Azure AI Translator service."
    target_language = "es"  # Spanish
    translate_text(text_to_translate, target_language)

    print("\nLanguage analysis demo completed!")


if __name__ == "__main__":
    main()
