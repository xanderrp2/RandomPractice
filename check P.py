from tkinter import *
root = Tk()
from tkinter import messagebox
root.title("CATS")
root.geometry("300x100")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 5)
root.grid_rowconfigure(1,minsize = 5)
a = 0
def check():
    global a
    if str(box1.get()) != "mr.Fishy":
        messagebox.askretrycancel("warning","the passward you enterd is incorect")
        box2.delete(0,END)
        box1.delete(0,END)
        a = a + 1
    elif str(box2.get()) != "dogs are good":
        messagebox.askretrycancel("warning","the username you enterd is incorect")
        box2.delete(0,END)
        box1.delete(0,END)
        a = a + 1
    elif str(box2.get()) != "mr.Fishy" and str(box1.get()) != "dogs are good":
        messagebox.askretrycancel("warning","the username and passward you enterd is incorect")
        box2.delete(0,END)
        box1.delete(0,END)
        a = a + 1
    if str(box1.get()) == "mr.Fishy" and str(box2.get()) == "dogs are good":
        messagebox.showwarning("access granted","welcome 'mr.Fishy'")
        box2.delete(0,END)
        box1.delete(0,END)
    if a == 5:
        messagebox.showwarning("stop","you have been banned")
        box2.delete(0,END)
        box1.delete(0,END)
        
        
        

box1 = Entry(root,show = "*")
box1.grid(row = 6,column = 4)
box2 = Entry(root)
box2.grid(row = 7,column = 4)
label1 = Label(root,text = "username")
label1.grid(row = 6,column = 3)
label2 = Label(root,font = ("Arial","20","italic"),text = "passward")
label2.grid(row = 7,column = 3)
button1 = Button(root,text = "GO",command = check)
button1.grid(row = 8,column = 4)



root.mainloop()
