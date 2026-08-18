# imports all classes,functions, and variables
from tkinter import *
import tkinter as tk

# creates a widget using Tk(), automatically creates a window
# with title bar, mini, maximize and close buttons.
root = Tk()

Chris_web = Label(root, text="Hello, World!") # root window, set to "hello...."
# now we create a label widget, a child to the root window
Chris_web.pack()
# now we call pack() method on this widget.
root.mainloop()