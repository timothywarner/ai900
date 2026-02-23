"""
Content Moderation Demo - AI-900
This script demonstrates using Azure AI Content Moderator to:
1. Screen text for profanity, PII, and inappropriate content
2. Moderate image content for adult or racy content

Requirements:
- Azure subscription
- Content Moderator resource
"""

import os
from azure.ai.contentmoderator import ContentModeratorClient
from azure.core.credentials import AzureKeyCredential
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw

# Add your Content Moderator key and endpoint
content_moderator_key = "YOUR_CONTENT_MODERATOR_KEY"
content_moderator_endpoint = "YOUR_CONTENT_MODERATOR_ENDPOINT"

# Create client
client = ContentModeratorClient(endpoint=content_moderator_endpoint, 
                               credentials=CognitiveServicesCredentials(content_moderator_key))

# ------ Text Moderation Example ------
def moderate_text():
    print("\n=== Text Moderation Example ===")
    
    # Example text with potential issues
    text = "Is this a crap email address: test@example.com. Phone: 425-555-1212. Address: 1 Microsoft Way, Redmond, WA 98052."
    
    # Moderate text
    screen = client.text_moderation.screen_text(
        text_content_type="text/plain",
        text_content=text,
        language="eng"
    )
    
    # Print results
    if screen.pii:
        print("Personal Information found:")
        for item in screen.pii.email:
            print(f"- Email: {item}")
        for item in screen.pii.phone:
            print(f"- Phone: {item}")
        for item in screen.pii.address:
            print(f"- Address: {item}")
    
    if hasattr(screen, 'terms') and screen.terms:
        print("\nPotentially offensive terms found:")
        for term in screen.terms:
            print(f"- Term: {term.term} (confidence: {term.term_confidence})")
    else:
        print("\nNo offensive terms found")

# ------ Image Moderation Example ------
def moderate_image(image_url):
    print("\n=== Image Moderation Example ===")
    
    # Download the image to analyze
    image_data = requests.get(image_url).content
    
    # Evaluate for adult/racy content
    evaluation = client.image_moderation.evaluate_for_adult_racy_content_with_http_info(
        image=image_data,
        raw=True
    )[0]
    
    # Print results
    print(f"Adult content: {evaluation.adult_classification_score} score, {evaluation.is_adult_content}")
    print(f"Racy content: {evaluation.racy_classification_score} score, {evaluation.is_racy_content}")

    # Check for text in image (OCR)
    ocr_result = client.image_moderation.ocr(
        language="eng",
        image=image_data,
        raw=True
    )[0]
    
    if ocr_result.text:
        print("Text detected in image:")
        print(ocr_result.text)

def main():
    # Run text moderation example
    moderate_text()
    
    # Run image moderation example (use an appropriate test image)
    sample_image = "https://moderatorsampleimages.blob.core.windows.net/samples/sample.jpg"
    moderate_image(sample_image)
    
    print("\nContent moderation demo completed!")

if __name__ == "__main__":
    main() 