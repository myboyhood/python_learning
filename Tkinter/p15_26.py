#!usr/bin/env python
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
text = Text(root, width=80, height=20)
text.pack()
text.insert(INSERT, "what IronMan says?", "tag1")

print(text.get("1.5 + 2 chars", "1.end"))
text.mark_set("here", "1.4")
text.insert("here", " fuck")
text.insert("here", " hhh")
text.mark_gravity("here", LEFT)  # insert in the left
text.insert("here", "ggg")

text.tag_add("tag1", "1.4", "1.5")
text.tag_config("tag1", background="yellow", foreground="blue")
photo = Image.open('/home/user/Tkinter/image/tony_stark.jpg')
img = ImageTk.PhotoImage(photo)


def show():
    text.image_create(END, image=img)  # the last "insert object" use keyword "END"


b1 = Button(text, text="acquire answer", command=show)
b1.pack(side=RIGHT)  # in Text. it is hard to place the location
text.window_create(INSERT, window=b1)

mainloop()