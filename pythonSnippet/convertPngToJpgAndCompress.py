import os
import concurrent.futures
from PIL import Image

def resize_and_convert_image(file_path):
	filename, ext = os.path.splitext(file_path)
	if ext in (".png", ".jpg", ".jpeg"):
		try:
			img = Image.open(file_path)
			action = ""

			#rotate if landscape
			if img.width > img.height:
				img = img.rotate(-90, expand=True)
				img.save(file_path)
				action += "rotated "

			#resize if too big
			if img.width > 1800 or img.height > 2400:
				img = img.resize((img.width // 2, img.height // 2), Image.LANCZOS)
				img.save(file_path)  # Overwrite the original image
				action += "compressed "
			
			#convert if png
			if file_path.lower().endswith('.png'):
				jpg_path = os.path.splitext(file_path)[0] + ".jpg"
				img = Image.open(file_path)
				if img.mode != "RGB":  #OSError: cannot write mode P as JPEG
					img = img.convert("RGB")
				img.save(jpg_path, "JPEG", quality=70)
				os.remove(file_path)  # Delete the original PNG image
				action += "converted "
		except:
			print(f"Error processing {file_path}")

	return None if len(action)==0 else action + file_path

def process_folder(folder_path):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		for root, _, files in os.walk(folder_path):
			image_files = [file_name for file_name in files if file_name.lower().endswith(('.png', '.jpg', '.jpeg'))]

			results = [executor.submit(resize_and_convert_image, os.path.join(root, file_name)) for file_name in image_files]
			for f in concurrent.futures.as_completed(results):
				if (f.result()): print(f.result())

if __name__ == "__main__":
	current_directory = os.getcwd()
	process_folder(current_directory)