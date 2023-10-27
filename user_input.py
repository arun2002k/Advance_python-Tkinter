from tkinter import *

root = Tk()

input = Entry(root,width=100)
input.pack()

def onclick():
    label = Label(root,text=input.get())
    label.pack()

button = Button(root, text="Click this button",command=onclick,fg="white",bg="black")
button.pack()


root.mainloop()