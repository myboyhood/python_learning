#!usr/bin/env python
from tkinter import *

root = Tk()
e = Entry(root)
e.pack(padx=10, pady=10)
e.delete(0, END)
e.insert(0, "default")

mainloop()