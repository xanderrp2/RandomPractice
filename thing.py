from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("400x100")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a = BooleanVar()
a.set(4)
def reverse():
    b = box1.get()
    if b[:] == b[::-1]:
        a.set(1)
        lable3["text"]=str(a.get())
    else:
        a.set(0)
        lable3["text"]=str(a.get())
def same():
    o = box1.get()
    p = box2.get()
    if len(o) == len(p):
        lable4["text"]="same"
    if len(o) != len(p):
        lable4["text"]="!same"
        
    

lable1 = Label(root,text = "the first word")
lable1.grid(row = 1,column = 1)
lable2 = Label(root,text = "the second word")
lable2.grid(row = 2,column = 1)
box1 = Entry(root,text = "")
box1.grid(row = 1, column = 2, columnspan = 4)
box2 = Entry(root,text = "")
box2.grid(row = 2, column = 2, columnspan = 4)
button = Button(root,text = "see",command = reverse)
button.grid(row = 3,column = 4)
button2 = Button(root,text = "same",command = same)
button2.grid(row = 3,column = 5)
lable3 = Label(root,text = "")
lable3.grid(row = 3, column = 3)
lable4 = Label(root,text = "")
lable4.grid(row = 3,column = 2)
root.mainloop()
