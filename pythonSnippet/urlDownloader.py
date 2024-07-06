import requests
import os

def download_images(base_url, start, end, save_dir):
    """
    Downloads images from a specified URL pattern and saves them to a directory.

    :param base_url: The base URL pattern (e.g., "https://www.xyz.com/")
    :param start: The starting index for the image URLs
    :param end: The ending index for the image URLs
    :param save_dir: The directory where images will be saved
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i in range(start, end + 1):
        image_url = f"{base_url}{i}.jpg"
        response = requests.get(image_url)
        if response.status_code == 200:
            file_path = os.path.join(save_dir, f"{i}.jpg")
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {image_url}")
        else:
            print(f"Failed to download: {image_url}")

if __name__ == "__main__":
    base_url = "https://google.com#0"
    start_index = 1
    end_index = 54
    save_directory = "C:/Users/keary/Downloads"

    download_images(base_url, start_index, end_index, save_directory)
