"""
Azure Computer Vision Demo - AI-900
This script demonstrates using Azure AI Vision service for:
1. Image classification and tagging
2. Object detection
3. OCR (text recognition)
4. Face detection

Requirements:
- Azure subscription
- Azure AI Vision resource
"""

import os
import time
import io
from PIL import Image, ImageDraw, ImageFont
import requests
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import (
    VisualFeatureTypes,
    Details,
)
from msrest.authentication import CognitiveServicesCredentials

# Add your Computer Vision subscription key and endpoint
import os

vision_key = os.getenv("TWAI900COMPUTERVISION1_KEY")
vision_endpoint = os.getenv("TWAI900COMPUTERVISION1_ENDPOINT")

# Initialize the client
vision_client = ComputerVisionClient(
    vision_endpoint, CognitiveServicesCredentials(vision_key)
)


def analyze_image(image_url, features):
    """Analyze an image using Azure AI Vision service"""
    print(f"\nAnalyzing image: {image_url}")

    # Get image analysis
    image_analysis = vision_client.analyze_image(image_url, visual_features=features)

    return image_analysis


def detect_objects(image_url):
    """Detect objects in an image"""
    print(f"\nDetecting objects in image: {image_url}")

    # Detect objects
    objects = vision_client.detect_objects(image_url)

    return objects


def recognize_text(image_url):
    """Extract text from images using OCR"""
    print(f"\nExtracting text from image: {image_url}")

    # Recognize text
    text_results = vision_client.recognize_printed_text(image_url)

    return text_results


def draw_bounding_boxes(image_url, objects):
    """Draw bounding boxes around detected objects"""
    # Download the image
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Draw rectangles around objects
    for obj in objects.objects:
        # Get object coordinates
        x = obj.rectangle.x
        y = obj.rectangle.y
        w = obj.rectangle.w
        h = obj.rectangle.h

        # Draw rectangle
        draw.rectangle([x, y, x + w, y + h], outline="red", width=3)

        # Add object name
        draw.text(
            [x, y - 20], f"{obj.object_property} ({obj.confidence:.2f})", fill="red"
        )

    # Save and return the modified image
    output_path = "objects_detected.jpg"
    img.save(output_path)
    print(f"Image with bounding boxes saved to {output_path}")
    return img


def demo_image_classification(image_url):
    """Demo image classification and tagging"""
    print("\n===== Image Classification Demo =====")

    # Select features to return
    features = [
        VisualFeatureTypes.categories,
        VisualFeatureTypes.description,
        VisualFeatureTypes.tags,
        VisualFeatureTypes.adult,
        VisualFeatureTypes.brands,
        VisualFeatureTypes.color,
    ]

    # Analyze the image
    analysis = analyze_image(image_url, features)

    # Display results
    print("\nImage Categories:")
    for category in analysis.categories:
        print(f"- {category.name} (confidence: {category.score:.2f})")

    print("\nImage Description:")
    for caption in analysis.description.captions:
        print(f"- {caption.text} (confidence: {caption.confidence:.2f})")

    print("\nTags:")
    for tag in analysis.tags:
        print(f"- {tag.name} (confidence: {tag.confidence:.2f})")

    print("\nContent Moderation:")
    print(f"- Adult content: {analysis.adult.is_adult_content}")
    print(f"- Racy content: {analysis.adult.is_racy_content}")

    # Detect dominiant colors
    print("\nDominant Colors:")
    if analysis.color.dominant_colors:
        for color in analysis.color.dominant_colors:
            print(f"- {color}")


def demo_object_detection(image_url):
    """Demo object detection"""
    print("\n===== Object Detection Demo =====")

    # Detect objects
    objects = detect_objects(image_url)

    # Display results
    print(f"\nObjects detected: {len(objects.objects)}")
    for obj in objects.objects:
        print(f"- {obj.object_property} (confidence: {obj.confidence:.2f})")
        print(
            f"  Position: x={obj.rectangle.x}, y={obj.rectangle.y}, w={obj.rectangle.w}, h={obj.rectangle.h}"
        )

    # Draw bounding boxes
    draw_bounding_boxes(image_url, objects)


def demo_ocr(image_url):
    """Demo OCR (Optical Character Recognition)"""
    print("\n===== OCR Demo =====")

    # Recognize text
    text_results = recognize_text(image_url)

    # Display results
    print("\nText extracted from image:")
    for region in text_results.regions:
        for line in region.lines:
            line_text = " ".join([word.text for word in line.words])
            print(f"- {line_text}")


def main():
    """Main function to run all demos"""
    # Sample images for different scenarios
    classification_image = "https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/street.jpg"
    object_detection_image = "https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/produce.jpg"
    ocr_image = "https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/letter.jpg"

    # Run demos
    demo_image_classification(classification_image)
    demo_object_detection(object_detection_image)
    demo_ocr(ocr_image)

    print("\nComputer vision demo completed!")


if __name__ == "__main__":
    main()
