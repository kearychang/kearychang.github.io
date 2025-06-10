import os
import concurrent.futures
from PIL import Image
import pillow_heif

def convert_image(file_path, format='JPEG'):
	hasConvert = False
	try:
		img = Image.open(file_path)
		jpg_path = os.path.splitext(file_path)[0] + ".jpeg"
		img.save(jpg_path, format=format)
		hasConvert = True
		print(f"Converted and saved: {jpg_path}")
	except Error:
		print(e)
		#print(f"Error processing {file_path}")

	return None if (hasConvert is False) else file_path

def process_folder(folder_path):
	pillow_heif.register_heif_opener()
	with concurrent.futures.ThreadPoolExecutor() as executor:
		for root, _, files in os.walk(folder_path):
			image_files = [file_name for file_name in files if file_name.lower().endswith(('.heic'))]

			results = [executor.submit(convert_image, os.path.join(root, file_name)) for file_name in image_files]
			for f in concurrent.futures.as_completed(results):
				if (f.result()): print(f.result())

if __name__ == "__main__":
	current_directory = os.getcwd()
	process_folder(current_directory)