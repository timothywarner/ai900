# Computer Vision Image Analysis Demo

## Overview

In this hands-on lab, you'll learn how to use the Azure Computer Vision service to analyze images and extract information. The Computer Vision service provides algorithms to process images and return information on their visual features.

## Learning Objectives

By the end of this lab, you will be able to:
- Create and configure a Computer Vision resource in Azure
- Use the Computer Vision API to analyze images
- Extract visual features, objects, and text from images
- Implement image analysis in a Python application

## Prerequisites

- An Azure subscription (free trial or paid)
- Basic knowledge of Python programming
- Visual Studio Code or another code editor
- Python 3.6 or later installed

## Step 1: Create a Computer Vision Resource

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Click **Create a resource**.
3. Search for **Computer Vision** and select it from the results.
4. Click **Create**.
5. Fill in the following details:
   - **Subscription**: Select your Azure subscription.
   - **Resource group**: Create a new resource group or select an existing one.
   - **Region**: Select a region close to you (e.g., East US, West Europe).
   - **Name**: Enter a unique name for your resource (e.g., `my-computer-vision`).
   - **Pricing tier**: Select **Free F0** (for testing) or **Standard S1**.
6. Click **Review + create**, then **Create**.
7. Once deployment is complete, click **Go to resource**.
8. In the left menu, click **Keys and Endpoint**.
9. Copy **Key 1** and the **Endpoint** URL. You'll need these values later.

## Step 2: Set Up Your Development Environment

1. Create a new folder for your project.
2. Open a terminal or command prompt and navigate to your project folder.
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
5. Install the required packages:
   ```bash
   pip install azure-cognitiveservices-vision-computervision pillow matplotlib
   ```
6. Create a new file named `analyze_image.py`.

## Step 3: Write the Image Analysis Code

Open `analyze_image.py` and add the following code:

```python
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image
import matplotlib.pyplot as plt
import requests
from io import BytesIO

# Add your Computer Vision subscription key and endpoint
subscription_key = "YOUR_COMPUTER_VISION_KEY"
endpoint = "YOUR_COMPUTER_VISION_ENDPOINT"

# Create a client
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# URL of the image to analyze
image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

# Function to display the image
def display_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# Display the image
print("Original image:")
display_image(image_url)

# Analyze the image
print("Analyzing image...")
features = [
    VisualFeatureTypes.categories,
    VisualFeatureTypes.description,
    VisualFeatureTypes.objects,
    VisualFeatureTypes.tags,
    VisualFeatureTypes.adult,
    VisualFeatureTypes.brands,
    VisualFeatureTypes.faces,
    VisualFeatureTypes.image_type,
    VisualFeatureTypes.color
]

results = computervision_client.analyze_image(image_url, visual_features=features)

# Print results
print("\nImage Description:")
if results.description.captions:
    for caption in results.description.captions:
        print(f"Description: {caption.text} (confidence: {caption.confidence:.2f})")

print("\nTags:")
for tag in results.tags:
    print(f"- {tag.name} (confidence: {tag.confidence:.2f})")

print("\nObjects:")
for object in results.objects:
    print(f"- {object.object_property} at location {object.rectangle.x}, {object.rectangle.y}, {object.rectangle.w}, {object.rectangle.h} (confidence: {object.confidence:.2f})")

print("\nCategories:")
for category in results.categories:
    print(f"- {category.name} (confidence: {category.score:.2f})")

print("\nColor Scheme:")
print(f"- Dominant foreground color: {results.color.dominant_color_foreground}")
print(f"- Dominant background color: {results.color.dominant_color_background}")
print(f"- Accent color: {results.color.accent_color}")
print(f"- Is black and white: {results.color.is_bw_img}")
```

## Step 4: Update the Code with Your Credentials

1. Replace `YOUR_COMPUTER_VISION_KEY` with the key you copied from the Azure portal.
2. Replace `YOUR_COMPUTER_VISION_ENDPOINT` with the endpoint URL you copied.

## Step 5: Run the Application

1. Save the file.
2. In your terminal or command prompt (with the virtual environment activated), run:
   ```bash
   python analyze_image.py
   ```
3. The application will:
   - Display the image
   - Analyze the image using the Computer Vision service
   - Print the analysis results, including description, tags, objects, categories, and color scheme

## Step 6: Experiment with Different Images

1. Try modifying the `image_url` variable to analyze different images.
2. You can use your own image URLs or try these sample images:
   - Landmark: `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg`
   - People: `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/people.jpg`
   - Objects: `https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg`

## Step 7: Analyze Local Images

To analyze local images instead of images from URLs, modify your code as follows:

```python
# Add this function to your code
def analyze_local_image(image_path):
    # Open local image file
    with open(image_path, "rb") as image_file:
        # Call API with local image
        results_local = computervision_client.analyze_image_in_stream(
            image_file, visual_features=features)
    
    # Display local image
    img = Image.open(image_path)
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
    return results_local

# Use the function with a local image file
# local_image_path = "path/to/your/image.jpg"
# results = analyze_local_image(local_image_path)
```

## Clean Up Resources

When you're done with the lab, you can delete the Azure resources to avoid incurring additional costs:

1. Go to the [Azure portal](https://portal.azure.com).
2. Navigate to your resource group.
3. Click **Delete resource group**.
4. Enter the resource group name to confirm deletion.
5. Click **Delete**.

## Next Steps

- Explore other Computer Vision features like OCR (Optical Character Recognition) and spatial analysis
- Try integrating Computer Vision with other Azure services
- Build a web application that uses the Computer Vision API
- Learn about Custom Vision for training your own image classification and object detection models

## Additional Resources

- [Computer Vision Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/)
- [Computer Vision API Reference](https://docs.microsoft.com/en-us/rest/api/computer-vision/)
- [Azure Cognitive Services Samples on GitHub](https://github.com/Azure-Samples/cognitive-services-python-sdk-samples)
- [Microsoft Learn: Analyze images with the Computer Vision service](https://docs.microsoft.com/en-us/learn/modules/analyze-images-computer-vision/) 