import os
import re
import sys
from pathlib import Path

def sanitize_path(path):
    """
    Escape the path for use in command line by wrapping it in double quotes.
    This is typically needed for paths with spaces, brackets, and other special characters.
    """
    return f'"{path}"'

# Sorts items in a natural/human order
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l, key=alphanum_key)

def renameNestedFiles(path, move):
    shouldMove = (move != None)
    print(path)
    for chapter in os.listdir(path):
        chapter_path = os.path.join(path, chapter) # Correctly handle paths
        if os.path.isdir(chapter_path):
            counter = 0
            print(chapter)
            pageList = natural_sort(os.listdir(chapter_path))
            # No need to change directories; handle paths directly
            l = len(pageList)
            for page in pageList:
                _, ext = os.path.splitext(page)
                if move:
                    page_path = os.path.join(chapter_path, page)
                    # Adjust for number of digits
                    number_format = "_{:03d}" if l >= 100 else "_{:02d}"
                    new_name = chapter + number_format.format(counter) + ext
                    new_path = os.path.join(path, new_name)
                    os.rename(page_path, new_path)
                else:
                    if l >= 100:
                        if counter <= 9:
                            os.rename(page, chapter + "_00" + str(counter) + ext)
                        elif counter <= 99:
                            os.rename(page, chapter + "_0" + str(counter) + ext)
                        else:
                            os.rename(page, chapter + "_" + str(counter) + ext)
                    else:
                        if counter <= 9:
                            os.rename(page, chapter + "_0" + str(counter) + ext)
                        else:
                            os.rename(page, chapter + "_" + str(counter) + ext)
                counter += 1
            # After processing all files in the directory, remove it if empty
            os.rmdir(chapter_path) # This only works if the directory is empty

if __name__ == "__main__":
    move = True if len(sys.argv) >= 2 else None
    cwd = os.getcwd()
    # for folder in cwd:
        # print(os.path.)
    folder = sys.argv[2]
    renameNestedFiles(os.path.join(cwd,folder), move)