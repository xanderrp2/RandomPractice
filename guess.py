from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
n = 0
def pro():
    n = random.randint(0,100)
    print(n)
def check():
    if int(box1.get()) == n:
        messagebox.showinfo("texting cats","correct")
        #lable.insert(0,"correct")
    if int(box1.get()) > n:
        messagebox.showinfo("texting cats","thats a little high")
       # "just a little heigh")
    if int(box1.get()) < n:
        messagebox.showinfo("texting cats","thats a little low")
        #lable.insert(0,"just a little low")
        
            
root.grid_columnconfigure(0,minsize = 420)
root.grid_rowconfigure(1,minsize = 50)
                        

box1 = Entry(root)
box1.grid(row = 0,column = 1)
button1 = Button(root,text = "start",height = 5, width = 10,command = pro)
button1.grid(row = 2, column = 1)

button2 = Button(root,text = "guess",height = 5, width = 10,command = check)
button2.grid(row = 3, column = 1)
lable = Label(root,text = "")
lable.grid(row = 4,column = 1)







root.mainloop()
