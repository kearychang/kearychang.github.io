import os
from pathlib import Path
import re

#Iterate through Authors, then iterate through Chapter
#Assuming pages inside are not folders, renames them to
#Author + Chapter + pageNo.

#To work properly, pages should just be a number

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l, key=alphanum_key)

def unnestDoubleNested(path):
    for author in os.listdir(path):
        if (os.path.isdir(author)):
            for chapter in os.listdir(author):
                if (os.path.isdir(author + "\\" + chapter)):
                    os.chdir(path + "\\" + author)
                    for page in natural_sort(os.listdir(chapter)):
                        file = chapter + "\\" + page
                        os.rename(file, str(page))
                    os.rmdir(chapter)
                    os.chdir(path)
unnestDoubleNested(os.getcwd())