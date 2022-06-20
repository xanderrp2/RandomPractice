from tkinter import *
import webcolors, random, time
from tkinter import messagebox
from tkinter import filedialog as fd
root = Tk()
root.title("CATS")
root.geometry("400x200")
root.resizable(width=True,height=True)
root.configure(bg="snow")

GH = ["thing1","thing2","thing3"]
cat,this,thing = StringVar()

dropDown = OptionMenu(root, var, *GH).grid(row = 1 ,column = 1)

day = [i for i in range(1,32,1) if i%2 == 0]
print(day)
a= int(input("what is this?"))
    



root.mainloop()
