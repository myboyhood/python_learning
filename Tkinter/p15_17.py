#!usr/bin/env python
from tkinter import *


root = Tk()
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def testCMD(content):
    if content.isdigit():
        return True
    else:
        return False


Entry(root, textvariable=v1, width=10, validate="key", validatecommand=(testCMD, "%P")).grid(padx=5, pady=10, row=0, column=0)
Label(root, text="+").grid(row=0, column=1)
Entry(root, textvariable=v2, width=10, validate="key", validatecommand=(testCMD, "%P")).grid(padx=5, pady=10, row=0, column=2)
Label(root, text="=").grid(row=0, column=3)
Entry(root, textvariable=v3, width=10, validate="key", validatecommand=(testCMD, "%P")).grid(padx=5, pady=10, row=0, column=4)


def sum():
    result = int(v1.get()) + int(v2.get())
    v3.set(result)


Button(root, text="calculate", width=10, command=sum).grid(row=1, column=2)


mainloop()