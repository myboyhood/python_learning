#!usr/bin/env python
from tkinter import *

root = Tk()
# v1 = StringVar()
# v1.set(0)


s1 = Scale(root, from_=0, to=40, tickinterval=5, length=200, \
      resolution=5, orient=VERTICAL)

s1.pack()
Scale(root, from_=0, to=200, tickinterval=10, length=600, \
      resolution=10, orient=HORIZONTAL).pack()


# Label(root, textvariable=v1).pack()

mainloop()