from tkinter import *

root = Tk()
label =Label(root, text="Blank window")
label1 = Label(root, text="Hello world")
label.grid(row=0, column=0)
label1.grid(row=1, column=1)


root.mainloop()