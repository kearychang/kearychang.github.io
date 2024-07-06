import tkinter as tk
from tkinter import ttk # ttk module has some advanced widgets that make our GUI look great

# Modified Button Click Function
def clickMe():
    action.configure(text='Hello ' + name.get())

win = tk.Tk() # create an instance of the Tk class by calling its constructor (the parentheses appended to Tk turn the class into an instance).
win.title("Python GUI") # use the instance variable of the class ( win ) to give our window a title via the title property

aLabel = ttk.Label(win, text="Enter a name:")
aLabel.grid(column=0, row=0)

action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=1)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

win.resizable(0, 0) # Disable resizing the GUI
nameEntered.focus() # Place cursor into name Entry
win.mainloop() # we start the window's event loop by calling the mainloop method on the class instance win