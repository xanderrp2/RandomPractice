from tkinter import *
import time
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a = StringVar()
b = False
c = 0
def start():

    global c
    c = 0
    global b
    b = True
    print("ok")
    while b == True:
        print("ok1")
        time.sleep(1)
        c = c + 1
        a.set(str(c))
        root.update()
      
def reset():
    
    global b
    global c
    c = 0
    b = False
    a.set(str(c - c))

Label1 = Label(root,textvariable = a)
Label1.pack()
class Buton():
    def __init__(self,text,command,pack):
        self.text = text
        self.command = command
        self.pack = pack
        self.button = Button(root,text = text,command = command)
        self.button.pack(side = pack)

B1 = Buton("start",start,LEFT)
B2 = Buton("restart",reset,RIGHT)




root.mainloop()
