#!usr/bin/env python
from tkinter import *


def show():
    print("username1 %s " % e1.get())
    print("password: %s " % e2.get())
    print("username2 %s " % v1.get())
    print("password: %s " % v2.get())
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def test():
    if e2.get() == "2":
        print("True!")
        validateresult.set("correct")
        return True
    else:
        validateresult.set("not correct")
        e2.delete(0, END)
        return False


root = Tk()

validateresult = StringVar()
validateresult.set("please input")

Label(root, text="username1").grid(row=0)
Label(root, text="password").grid(row=1)
Label(root, text="username2").grid(row=3)
Label(root, text="password").grid(row=4)
Label(root, textvariable=validateresult).grid(row=2, column=1)

e1 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2 = Entry(root, show="*", validate="focusout", validatecommand=test)
e2.grid(row=1, column=1, padx=10, pady=5)

v1 = StringVar()
v2 = StringVar()
e3 = Entry(root, textvariable=v1)
e4 = Entry(root, textvariable=v2, show="#")
e3.grid(row=3, column=1, padx=10, pady=5)
e4.grid(row=4, column=1, padx=10, pady=5)





Button(root, text="get information", width=10, command=show)\
    .grid(row=5, column=0, sticky=W, padx=10, pady=5)
Button(root, text="quit", width=10, command=root.quit())\
    .grid(row=5, column=1, sticky=E, padx=10, pady=5)

mainloop()