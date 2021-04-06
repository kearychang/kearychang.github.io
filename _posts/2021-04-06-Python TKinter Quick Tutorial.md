---
layout: post
title: Python TKinter Quick Tutorial
date: 2021-04-06
excerpt: A quick rundown to creating GUI for desktop app in Python3
tags: [Frontend]
comments: true
---
So you want a quick and easy GUI for a tool?\
Consider [TKinter](https://docs.python.org/3/library/tkinter.html).\ 
This module ships with Python3 so it doesn't have to be installed.\
This blog post's Markdown was created using a GUI application that handles the boilerplate of creating Github page posts. 
![Create Blog Post GUI](https://raw.githubusercontent.com/kearychang/kearychang.github.io/master/assets/post-project/createPostGUI.jpg)

The base code looks like this.
{% highlight python %}
import tkinter as tk
win = tk.Tk()  #create instance of TKinter application
win.title("Create blog post GUI") #application menu title
#OUR CODE
win.resizable(0, 0) #prevent resizing of application
win.mainloop()  #initialize application and its event loop
{% endhighlight %}

### Widgets ###
Of course, we need **widgets**.\
If you are familiar with this topic, the common elements and the method to create them are
* Label `ttk.Label(win, text="A Label")`
* Entry (text field) `ttk.Entry(win, width=12, textvariable=tk.StringVar())`
* Button `ttk.Button(win, text="Click Me!", command=callback)`
* Checkbutton `tk.Checkbutton(win, text="UnChecked", variable=tk.IntVar())`
* Radiobutton `tk.Radiobutton(win, text="1", variable=tk.IntVar(), value=1, command=callback)`
* LabelFrame (for nesting other widgets) `labelsFrame = ttk.LabelFrame(win, text='Labels')`

There are some more advanced widgets
* Combobox (dropdown list) `combo = ttk.Combobox(win, width=12, textvariable=tk.StringVar())`
* ScrolledText (textarea) `scr = tkinter.scrolledtext.ScrolledText(win, width=80, height=40)`
* Menu Bar (this is the UI dropdown menu when you hit *File>Open* or *File>Save*)

We need a bit extra code for these widgets
{% highlight python %}
#Combo Box
combo['values'] = (1,2,3) #arguments of our combobox in tuple form
comboChosen.current(0) #default index of selected dropdown option
#Menu Bar
menuBar = tkinter.Menu(win) #menu constructor
win.config(menu=menuBar) #assign menu to our GUI application
fileMenu = tkinter.Menu(menuBar, tearoff=0) #call for each menu (e.g. File, View, Edit, Help) of our menubar
fileMenu.add_command(label="New", command=_new) #_new is a callback func
fileMenu.add_separator() #horizontal line between menu bar commands
fileMenu.add_command(label="Exit", command=_exit) #_exit is a callback func
menuBar.add_cascade(label="File", menu=fileMenu) #element that creates our menubar when clicked
{% endhighlight %}

Be sure to return a variable reference to our widget.\
Now we can assign it a position on our grid by `widget.grid(row=x, column=y)`.\
If we want our element to span multiple columns, our argument will be `widget.grid(row=x, columnspan=y)`.

### Message Box ###
Sometimes, we want our GUI application to send out a **message box**.\
If you are familiar with JS, these are prompts which are new windows that users must confirm before returning to the application.\
These are used for feedback to let users know the state of the application such as success or failure.

{% highlight python %}
tkinter.messagebox.showinfo("Title", "Message")
tkinter.messagebox.showwarning("Title", "Message")
tkinter.messagebox.showerror("Title", "Message")
{% endhighlight %}

### Widget State and Application Logic ###
If you saw these data classes `tkinter.StringVar` or `tkinter.IntVar` and were confused, this section will explain them.\
Some widgets store state information which we need to retrieve for application logic such as whether a Checkbutton was checked or which Radiobutton was selected.\
When we interact with some widgets such as clicking on them, the values of these classes will change automatically.\
For **Entry**, `StringVar` will be the user input.\
For **ComboBox**, `StringVar` will store the string value of the selected option.\
For **Checkbutton**, `IntVar` will be 1 if checked and 0 if unchecked.\
For **Radiobutton**, `IntVar` will be the **n** referring to `tk.Radiobutton(win, text="A", variable=radVar, value=n, command=radCall)`.\
When we call `get()` on `StringVar` and `IntVar`, it returns a string and integer respectively. 