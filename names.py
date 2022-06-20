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
a = StringVar()
def name():
    names = ["a","b","c","s","d","e","f"]
    b = random.choice(names)
    a.set(b)
    print(a.get())
    
    
lable = Label(root,textvariable = a)
lable.pack()
button = Button(root,text = "name", command = name)
button.pack()

root.mainloop()
