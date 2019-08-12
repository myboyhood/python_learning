#!usr/bin/env python
from tkinter import *


root = Tk()
v = StringVar()

def test(content, reason, name):
    if content == "whu":
        print("right")
        print(content, reason, name)
        return True
    else:
        print("fault")
        print(content, reason, name)
        return False


testCMD = root.register(test)
e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=(testCMD, '%P', '%v', '%W'))
e2 = Entry(root)
e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)

mainloop()