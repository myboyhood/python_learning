#!usr/bin/env python
from tkinter import *

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

LB1 = Listbox(frame1, setgrid=True)
LB1.pack()
for item in ["beijing", "shanghai", "guangzhou", "wuhan"]:
    LB1.insert(END, item)
Button(frame1, text="delete!", command=lambda x=LB1: x.delete(ACTIVE)).pack()

sb = Scrollbar(frame2)
sb.pack(side=RIGHT, fill=Y)
LB2 = Listbox(frame2, yscrollcommand=sb.set)
LB2.pack(side=LEFT, fill=BOTH)
for i in range(30):
    LB2.insert(END, str(i))
sb.config(command=LB2.yview)

mainloop()
