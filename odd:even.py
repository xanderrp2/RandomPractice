from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)

def add():
    a = int(box.get())
    if a%2 == 0:
        messagebox.showinfo("the number is","EVEN")
        if messagebox.askretrycancel("retry or cancel","would you like to try again or cancel?"):
            box.delete(0,END)
        else:
            quit()
    else:
        messagebox.showinfo("the number is","ODD")
        if messagebox.askretrycancel("retry or cancel","would you like to try again or cancel?"):
            box.delete(0,END)
        else:
            quit()
lable = Label(root,text = "please enter a number")
lable.pack(side=LEFT)
box = Entry(root,text = "")
box.pack(side=RIGHT)
button = Button(root,text = "summet",command = add)
button.pack(side=BOTTOM)

root.mainloop()
