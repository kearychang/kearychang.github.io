from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "darksouls2.png"
RANK = 100

"""
This program uses SVD to compress a PNG and print it.
The compression is customizable by changing RANK.
"""

def svd(image_path, rank):
	# Open the image using Pillow
	image = Image.open(image_path)

	# Convert the image to a NumPy array for processing
	img_array = np.array(image)
	
	 #Full SVD
	U, S, VT = np.linalg.svd(img_array, full_matrices=True)
	
	return modified_image

def show_image(image):
	# Display the image using matplotlib
	plt.imshow(image)
	plt.axis('off')  # Turn off axis labels
	plt.show()

if __name__ == "__main__":
	compressed_image = svd(IMAGE_PATH, rank = RANK)
	show_image(compressed_image)