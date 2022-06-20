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

x = ttk.Notebook(root,width = 20, height = 100)
x.pack()




FOOD = ttk.Frame(x)


CLIMAT = ttk.Frame(x)

ANIMALS = ttk.Frame(x)












root.mainloop()
