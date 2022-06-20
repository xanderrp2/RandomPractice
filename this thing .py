from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
c = StringVar()
a = IntVar(0)
def check():
    d = a.get() 
    if d == 1:
        c.set("CORRECT")
    elif d == 2:
        c.set("INCORRECT")
        
radio1 = Radiobutton(root,text = "dogs",value = 1,variable = a)
radio1.grid(row = 2,column = 1,columnspan = 2,padx=2,pady=1)
radio2 = Radiobutton(root,text = "cats",value = 2,variable = a)
radio2.grid(row = 3,column = 1,columnspan = 2,padx=2,pady=1)
button = Button(root,text = "submit",command = check)
button.grid(row = 4,column = 2,padx=2,pady=1)

label1 = Label(root,text = "Which is better?")
label1.grid(row = 1,column = 1,padx=2,pady=1)
label2 = Label(root,textvariable = c)
label2.grid(row = 4,column = 3,padx=2,pady=1)

root.mainloop()
