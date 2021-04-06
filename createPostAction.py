import os
from tkinter import messagebox
from datetime import date, datetime

def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)

def createPostAction(title, excerpt, content, tagsArr, isProject, folderName):
    if title == "" or excerpt == "" or content == "":
        alert(title="No content error", message = "You are missing either title, excerpt or content.", kind="error")
    today = date.today().strftime("%Y-%m-%d")
    fullTitle = today
    if isProject:
        fullTitle = fullTitle + "-!!!" + title + ".md"
    else:
        fullTitle = fullTitle + "-" + title + ".md"
    filePath = os.path.join(folderName, fullTitle)
    filePath.replace(" ", "-")

    #FILE CONTENT HEADER
    fileContent = []
    fileContent.append("---\n")
    fileContent.append("layout: post\n")
    fileContent.append("title: " + title + "\n")
    fileContent.append("date: " + today + "\n")
    fileContent.append("excerpt: " + excerpt + "\n")
    if isProject:
        fileContent.append("project: true\n")
        fileContent.append("tag:\n")
        for tag in tagsArr:
            fileContent.append("- " + tag + "\n")
    else:
        tagsStr = str(tagsArr).replace('\'', "")
        fileContent.append("tags: " + tagsStr + "\n")
    fileContent.append("comments: true\n")
    fileContent.append("---\n")

    #FILE CONTENT BODY
    fileContent.append(content)

    with open(filePath, 'wt') as f:
        for line in fileContent:
            f.writelines(line)

    alert(title="Created post file successfully", message = "File {0} was created".format(filePath))