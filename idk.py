from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a = StringVar()
b = StringVar()
c = IntVar()
d = DoubleVar()
def randome():
    box1.delete(0,END)
    box2.delete(0,END)
    c.set(random.randint(0,99999))
    box1.insert(0,c.get())
    ##a.set(c)
    d.set(random.uniform(0,99999))
    box2.insert(0,d.get())
    ##b.set(d)
    
    
    
    
button = Button(root,text = "generate",command = randome)
button.pack(side = BOTTOM)
label1 = Label(root,text = "intager")
label1.pack(side = LEFT)
label2 = Label(root,text = "desamol")
label2.pack(side = LEFT)
box1 = Entry(root,textvariable = a)
box1.pack(side = RIGHT)
box2 = Entry(root,textvariable = b)
box2.pack(side = RIGHT)
root.mainloop()

