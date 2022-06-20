from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("200x40")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a = IntVar()
b = 0
def plus():
    global b
    b = b + 1
    a.set(b)

def minus():
    global b
    b = b - 1
    a.set(b)
    
lable = Label(root, textvariable = a,width = 5)
lable.grid(row = 1,column = 2,padx = 3,pady = 4)
button = Button(root,text = "+", command = plus)
button.grid(row = 1, column = 1)
button1 = Button(root,text = "-", command = minus)
button1.grid(row = 1,column = 3)

root.mainloop()
