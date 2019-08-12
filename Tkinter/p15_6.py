#!usr/bin/env python
from tkinter import *


root = Tk()
root.geometry('400x300')
CARS = ["BMW", "AUTO", "Benze", "Ford"]
v = []
for car in CARS:
    v.append(IntVar())
    c = Checkbutton(root, text=car, variable=v)
    c.pack(anchor=W)
    l = Label(root, textvariable=v)
    l.pack(side=LEFT)

mainloop()
