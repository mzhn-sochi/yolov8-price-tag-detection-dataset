from PIL import Image
import hashlib
import os

source_path = 'input_images'
destination_path = 'prepared_images'

os.makedirs(destination_path, exist_ok=True)

supported_formats = [
    '.jpeg', 
    '.jpg',
    '.webp', 
    '.png'
]

def convert_image_to_jpeg(image_path, destination_path):
    with Image.open(image_path) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        img_byte_arr = img.tobytes()
        sha256_hash = hashlib.sha256(img_byte_arr).hexdigest()
        
        new_file_path = os.path.join(destination_path, f"{sha256_hash}.jpg")
        img.save(new_file_path, 'JPEG')

for root, dirs, files in os.walk(source_path):
    for file in files:
        if any(file.lower().endswith(ext) for ext in supported_formats):
            file_path = os.path.join(root, file)
            convert_image_to_jpeg(file_path, destination_path)