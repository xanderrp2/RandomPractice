from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a = 0
b = 0
button = Button(root,text = "")
while True():
    button.place(x = a,y = b)
    a = a +10
    b = b +10
root.mainloop()
