import os
import concurrent.futures
from PIL import Image
import io

def reduce_image_file_size(image_path, target_size_kb=450, quality_step=5):
    original_size_kb = os.path.getsize(image_path) / 1024
    if original_size_kb <= target_size_kb:
        return  # Exit if the image size is already acceptable
    img = Image.open(image_path)
    print(image_path + " file size is " + str(original_size_kb) + " KB")

    # Convert image to RGB if it's in 'P' mode (palette mode)
    if img.mode == 'P':
        img = img.convert('RGB')

    quality = 95  # Start with high quality

    while True:
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='JPEG', quality=quality)
        size_kb = len(img_bytes.getvalue()) / 1024

        if size_kb <= target_size_kb or quality <= 10:
            break
        quality -= quality_step
    img.save(image_path, format='JPEG', quality=quality)
    print(f"Reduced size of {image_path} to {size_kb:.2f}KB with quality {quality}")

def process_folder(folder_path):
	with concurrent.futures.ThreadPoolExecutor() as executor:      
		for root, _, files in os.walk(folder_path):
			image_files = [file_name for file_name in files if file_name.lower().endswith(('.jpg', '.jpeg'))]
			results = [executor.submit(reduce_image_file_size, os.path.join(root, file_name)) for file_name in image_files]
			for f in concurrent.futures.as_completed(results):
				if (f.result()): print(f.result())

if __name__ == "__main__":
	current_directory = os.getcwd()
	process_folder(current_directory)