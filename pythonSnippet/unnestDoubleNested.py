import os
from pathlib import Path
import re
import sys

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

def process_folder(path):
    for subfolder in os.listdir(path):
        subfolder_path = os.path.join(path, subfolder)
        
        if os.path.isdir(subfolder_path):
            # Iterate through files, sorted by natural sort
            for file_name in natural_sort(os.listdir(subfolder_path)):
                file_path = os.path.join(subfolder_path, file_name)
                
                if os.path.isfile(file_path):
                    # Construct new file name
                    parent_folder_name = os.path.basename(subfolder_path)
                    new_file_name = f"{parent_folder_name}_{file_name}"
                    new_file_path = os.path.join(path, new_file_name)
                    
                    # Move and rename the file
                    os.rename(file_path, new_file_path)
            # Remove the now empty subfolder
            os.rmdir(subfolder_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        process_folder(folder_path)