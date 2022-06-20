from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a1 = PhotoImage(file = "canada.png")
##class NOTE():
##
##    def __init__(self.info1,info2):
##        self.info1 = info1
##        self.info2 = info2
##        x = ttk.Notebook(root,width = 200,height = 200)
##    def build():
##        
        
x = ttk.Notebook(root,width = 20, height = 100)

x.pack()
a = ttk.Frame(x)
label1 = Label(a,image = a1)
label1.place(0,0)
b = ttk.Frame(x)

c = ttk.Frame(x)
x.add(a,text = "food")
x.add(b,text = "animals")
x.add(c,text = "size")
root.mainloop()
