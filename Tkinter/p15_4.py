#!usr/bin/env python
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
img = Image.open('/home/user/Tkinter/image/tony_stark.jpg')
photo = ImageTk.PhotoImage(img)
theLabel = Label(root,
                 text="stark industry",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=("Times NewRoman", 20),
                 fg="white")
theLabel.pack()
mainloop()
