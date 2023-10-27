from tkinter import *

root = Tk()

def onclick():
    label = Label(root,text="You clicked")
    label.pack()

button = Button(root, text="Click this button",command=onclick,fg="white",bg="black")
button.pack()


root.mainloop()