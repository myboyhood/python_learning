#!usr/bin/env python
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
textLabel = Label(root, text="Tony Stark")
textLabel.pack(side=LEFT)

img = Image.open('/home/user/Tkinter/image/tony_stark.jpg')
photo = ImageTk.PhotoImage(img)
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)

mainloop()