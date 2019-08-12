#!usr/bin/env python
import tkinter as tk

class App:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()
        self.hi_there = tk.Button(frame, text="say hello", fg="blue", bg="yellow", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT, padx=10, pady=10)

    def say_hi(self):
        print("I am first windows program!")


root = tk.Tk()
app = App(root)
root.mainloop()