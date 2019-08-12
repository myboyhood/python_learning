#!usr/bin/env python
from tkinter import *

root = Tk()

group = LabelFrame(root, text="best scripts language is ?", padx=5, pady=5)
group.pack(padx=20, pady=20)

LANGS = [("Python", 1), ("Perl", 2), ("Ruby", 3), ("Lua", 4)]
v = IntVar()
v.set(1)
for lang, num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num, indicatoron=False)  # change to rectangle frame
    b.pack(fill=X)

mainloop()