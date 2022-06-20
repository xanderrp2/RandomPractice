from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
h = DoubleVar()
def m():
    a = int(box1.get())
    b = a*(1/60)
    h.set(b)
    
def hS():
    a = int(box1.get())
    b = (a/60)/60
    h.set(b)
    
    
label = Label(root,text = "seconds")
label.pack()
box1 = Entry(root,text = "")
box1.pack()
button1 = Button(root,text = "minutes",command = m)
button1.pack()
button2 =Button(root,text = "hours",command = hS)
button2.pack()
label1 = Label(root, textvariable = h)
label1.pack()
root.mainloop()
