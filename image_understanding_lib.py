import os
import base64
from openai import OpenAI
from io import BytesIO

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Get a BytesIO object from file bytes
def get_bytesio_from_bytes(image_bytes):
    image_io = BytesIO(image_bytes)
    return image_io

# Load the bytes from a file on disk
def get_bytes_from_file(file_path):
    with open(file_path, "rb") as image_file:
        file_bytes = image_file.read()
    return file_bytes

# Generate a response using OpenAI API
def get_response_from_model(prompt_content, image_bytes, mask_prompt=None):
    # Encode image bytes to base64
    base64_image = base64.b64encode(image_bytes).decode('ascii')
    
    image_message = {
        "role": "user",
        "content": [
            {"type": "text", "text": "Image 1:"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            },
            {"type": "text", "text": prompt_content}
        ],
    }
    
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[image_message],
        max_tokens=2000,
        temperature=0
    )
    
    output = response.choices[0].message.content
    
    return output