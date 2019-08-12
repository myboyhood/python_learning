#!usr/bin/env python
from tkinter import *
from PIL import Image, ImageTk


def callback():
    var.set("hhhhh")


root = Tk()
# root.geometry('400x300')
frame1 = Frame(root)
frame2 = Frame(root)


var = StringVar()
var.set("I have army!")
textLabel = Label(frame1, textvariable=var, justify=LEFT)
textLabel.pack(side=LEFT)

img = Image.open('/home/user/Tkinter/image/tony_stark.jpg')
photo = ImageTk.PhotoImage(img)
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="hhh  how can you compete with me?!", command=callback)

theButton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()