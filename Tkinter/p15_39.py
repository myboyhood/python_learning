from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
root = Tk()
# root.geometry('300x400')


def callback():
    print(" I was called")


def pop(event):
    print("pop")
    popmenu.post(event.x_root, event.y_root)


def create1():
    top1 = Toplevel()
    top1.title("Spinbox Demo")
    Message(top1, text="this is a new window").pack()
    w1 = Spinbox(top1, value=("shanghai", "beijing", "wuhan"))
    w1.pack(padx=10, pady=10)


def create2(event):
    top2 = Toplevel()
    top2.title("login in")
    Label(top2, text="username:").grid(row=0, sticky=W)
    Label(top2, text="password").grid(row=1, sticky=W)
    Entry(top2).grid(row=0, column=1)
    Entry(top2, show="*").grid(row=1, column=1)
    # print(event.char)


def create3():
    top3 = Toplevel()
    top3.title("Picture")
    top3.geometry('400x300')
    pic = Image.open('/home/user/Tkinter/image/tony_stark.jpg')
    photo = ImageTk.PhotoImage(pic)
    # Label(top3, image=photo).place(relx=0.5, rely=0.5, anchor=CENTER)
    piclabel = Label(top3, image=photo)
    piclabel.pack(side=LEFT)


def openfile():
    filename = filedialog.askopenfilename()
    print(filename)


def askyesorno():
    result = messagebox.askyesno("ask", "are you master ?")
    print(result)


menubar = Menu(root)
popmenu = Menu(root, tearoff=False)

file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label="open", command=callback)
file_menu.add_command(label="save", command=callback)
menubar.add_cascade(label="file", menu=file_menu)

edit_menu = Menu(menubar, tearoff=False)
edit_menu.add_command(label="copy", command=callback)
edit_menu.add_command(label="cut", command=callback)
menubar.add_cascade(label="edit", menu=edit_menu)

frame1 = Frame(root, width=100, height=100, bd=3, relief=SUNKEN)
frame1.pack(padx=10, pady=10)
frame1.bind("<Button-1>", pop)

root.config(menu=menubar)

m1 = Message(root, text="long long long long long long message", width=50)
m1.pack()

frame2 = Frame(root, width=100, height=100, bd=3, relief=SUNKEN, takefocus=True)
frame2.pack(fill=BOTH)
frame2.bind("<Control-KeyPress-o>", create2)
# frame2.bind("<Control-Key-o>", create2)
frame2.focus_set()

Button(root, text="create city", command=create1).pack()
Button(root, text="create picture", command=create3).pack()
Button(root, text="open file", command=openfile).pack()
Button(root, text="ask yes or no", command=askyesorno).pack()

mainloop()

