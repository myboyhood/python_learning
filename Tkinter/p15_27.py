#!usr/bin/env python
from tkinter import *
import webbrowser


root = Tk()
text = Text(root, width=20, height=10, font=20)
text.pack()
text.insert(INSERT, "I love px4")
text.tag_add("link", "1.7", "1.10")
text.tag_config("link", background="yellow", underline=True)


def show_hand_cursor(event):
    text.config(cursor="arrow")


def show_arrow_cursor(event):
    text.config(cursor="xterm")


def link_to_web(event):
    webbrowser.open("http://www.px4.io")


text.tag_bind("link", "<Enter>", show_hand_cursor)
text.tag_bind("link", "<Leave>", show_arrow_cursor)
text.tag_bind("link", "<Button-1>", link_to_web)

mainloop()
