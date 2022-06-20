from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)

def click(a):
    label1 = Label(root,text = a)
    label1.pack(side = RIGHT)

button1 = Button(root,text = "dogs",command = lambda: click("AAAHHHH"))
button1.pack()
button2 = Button(root,text = "Cats",command = lambda: click("things"))
button2.pack()


root.mainloop()
