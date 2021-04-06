import tkinter as tk
import os
from createPostAction import createPostAction
from tkinter import ttk, scrolledtext
from pathlib import Path

win = tk.Tk()
win.title("Create blog post GUI")

#CREATE POST BUTTON ACTION
def createPost():
    createPostAction(title=postTitle.get(), excerpt=excerptTitle.get(), content=scr.get("1.0", "end-1c"), tagsArr = chVar, isProject = (radVar.get() == 2), folderName = folderComboBox.get())
    return

#BLOG POST TITLE
ttk.Label(win, text="Post Title").grid(column=0, row=0, padx=20)
postTitle = tk.StringVar()
postTitleTextField = ttk.Entry(win, width=100, textvariable=postTitle)
postTitleTextField.grid(columnspan=2, row=1)

#BLOG POST EXCERPT
ttk.Label(win, text="Post Excerpt").grid(column=0, row=2, padx=20)
excerptTitle = tk.StringVar()
excerptTitleTextField = ttk.Entry(win, width=100, textvariable=excerptTitle)
excerptTitleTextField.grid(columnspan=2, row=3)

#BLOG CONTENT
ttk.Label(win, text="Post Content").grid(column=0, row=4, padx=20)
scr = scrolledtext.ScrolledText(win, width=80, height=40, wrap=tk.WORD)
scr.grid(columnspan=2, row=5)

#TAGS
tagList = ["CS", "Network", "Algorithm", "DB", "AI", "NLP", "Frontend", "Backend", "Books", "Thought"]
chVar = [None]*len(tagList)
check = [None]*len(tagList)
checkFrame = ttk.LabelFrame(win)
checkFrame.grid(column=0, row=6, padx=20)
for index, tag in enumerate(tagList):
    chVar[index] = tk.IntVar()
    check[index] = tk.Checkbutton(checkFrame, text=tag, variable=chVar[index])
    check[index].grid(column=index, row=0)
    check[index].deselect()

#PROJECT
radFrame = ttk.LabelFrame(win)
radFrame.grid(column=0, row=7)
radVar = tk.IntVar()
rad1 = tk.Radiobutton(radFrame, text="POST", variable=radVar, value=1)
rad1.grid(column=0, row=0, sticky=tk.W)
rad2 = tk.Radiobutton(radFrame, text="PROJECT", variable=radVar, value=2)
rad2.grid(column=1, row=0, sticky=tk.W)

#FOLDER SELECTION
folderName = tk.StringVar()
folderComboBox = ttk.Combobox(radFrame, width=36, textvariable=folderName)
folderList = list(filter(lambda f: not f.startswith('.'), filter(os.path.isdir, os.listdir(os.getcwd()))))
folderList.insert(0, "")
folderComboBox['values'] = tuple(folderList)
folderComboBox.grid(column=2, row=0)
folderComboBox.current(0)

#CREATE POST BUTTON
createPostButton = ttk.Button(radFrame, text="Create Post", command=createPost)
createPostButton.grid(column=3, row=0)

#DEFAULT
postTitleTextField.focus()
rad1.select()

win.resizable(0, 0) # 6 Disable resizing the GUI
win.mainloop()