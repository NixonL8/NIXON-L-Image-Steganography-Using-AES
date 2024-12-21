from PIL import Image
import pytesseract
import os

# Function to generate a basic description of an image
def generate_image_description(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Get the image size
    width, height = image.size
    
    # Extract text from the image (if any)
    try:
        extracted_text = pytesseract.image_to_string(image).strip()
    except Exception as e:
        extracted_text = ""
    
    # Form a basic description
    description = f"The image has a resolution of {width}x{height} pixels. "
    if extracted_text:
        description += f"It contains the following text: '{extracted_text}'."
    else:
        description += "No text was detected in the image."
    
    return description

# Path to your image
image_path = "C:\\Users\\nixon\\Downloads\\flower.jpeg"

# Generate and display description
if os.path.exists(image_path):
    description = generate_image_description(image_path)
    print(f"Generated Description: {description}")
else:
    print(f"Image not found at {image_path}. Please check the path.")
