import os
from pathlib import Path
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

def unnest_files_in_cwd():
    cwd = os.getcwd()

    # Iterate through all items in the cwd
    for subfolder in os.listdir(cwd):
        subfolder_path = os.path.join(cwd, subfolder)

        if os.path.isdir(subfolder_path):
            # Iterate through files in the subfolder, sorted by natural sort
            for file_name in natural_sort(os.listdir(subfolder_path)):
                file_path = os.path.join(subfolder_path, file_name)
                if os.path.isfile(file_path): #and (file_name.endswith('.srt') or file_name.endswith('.mp4')):
                    # Construct new file name: folder_name + "_" + original file_name
                    new_file_name = f"{subfolder}_{file_name}"
                    new_file_path = os.path.join(cwd, new_file_name)

                    # Rename and move the file to the cwd
                    os.rename(file_path, new_file_path)

            # Remove the now empty subfolder if there are no more files
            if not os.listdir(subfolder_path):
                os.rmdir(subfolder_path)

if __name__ == "__main__":
    unnest_files_in_cwd()

