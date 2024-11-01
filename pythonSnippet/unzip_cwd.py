import os
import zipfile

def unzip_and_delete(zip_path):
    # Unzip the contents in the same folder as the .zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        extract_path = os.path.dirname(zip_path)
        zip_ref.extractall(extract_path)
    
    # Delete the .zip file after extraction
    os.remove(zip_path)

def process_folders_in_cwd():
    cwd = os.getcwd()

    # Walk through all folders and subfolders in the cwd
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                unzip_and_delete(zip_path)

if __name__ == "__main__":
    process_folders_in_cwd()
