#!usr/bin/env python
from tkinter import *

root = Tk()
v = IntVar()
Radiobutton(root, text="one", variable=v, value=1).pack(anchor=N)
Radiobutton(root, text="two", variable=v, value=2).pack(anchor=N)
Radiobutton(root, text="three", variable=v, value=3).pack(anchor=N)

mainloop()