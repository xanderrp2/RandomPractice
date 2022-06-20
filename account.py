from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
q = StringVar()
def withdraw():
    a = int(box3.get())
    b = int(box4.get())
    c = a - b
    q.set(c)

def add():
    a = int(box3.get())
    b = int(box4.get())
    c = a + b
    q.set(c)
    
    
    
label1 = Label(root,text = "name")
label1.grid(row = 1, column = 1)
label2 = Label(root,text = "account balance")
label2.grid(row = 2, column = 1)
label3 = Label(root,text = "accound total")
label3.grid(row = 3, column = 1)
label4 = Label(root,text = "amount")
label4.grid(row = 4, column = 1)
box1 = Entry(root,text = "")
box1.grid(row = 1,column = 2,columnspan = 3)
box2 = Entry(root,text = "")
box2.grid(row = 2,column = 2,columnspan = 3)
box3 = Entry(root,text = "")
box3.grid(row = 3,column = 2,columnspan = 3)
box4 = Entry(root,text = "")
box4.grid(row = 4,column = 2,columnspan = 3)
button1 = Button(root,text = "withdraw", command = withdraw)
button1.grid(row = 5,column = 3)
button2 = Button(root,text = "add",command = add)
button2.grid(row = 5,column = 4)
m = Message(root,textvariable = q)
m.grid(row = 1,column = 6)
root.mainloop()
