from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a= IntVar()
b= IntVar()
c= IntVar()

def CO():
    M = []
    if a.get():
        M.append("bread")
    if b.get():
        M.append("milk")
    if c.get():
        M.append("banana")
    print(M)
def clear():
    a.set(0)
    b.set(0)
    c.set(0)
button1 = Checkbutton(root,text = "bread",variable = a)
button1.pack(side = TOP)
button2 = Checkbutton(root,text = "milk",variable = b)
button2.pack(side = TOP)
button3 = Checkbutton(root,text = "banana",variable = c)
button3.pack(side = TOP)
button4 = Button(root,text = "clear",command = clear)
button4.pack(side = TOP)
button5 = Button(root,text = "check out",command = CO)
button5.pack(side = TOP)

root.mainloop()
