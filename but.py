from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)

class Buton():
    
    
    def __init__(self,x,y,number):
        
        self.x = x
        self.y = y
        self.number = number
        self.button = Button(root,text = number,command = self.pressed)
    def pllace(self):
        self.button.place(x = self.x,y = self.y)
    def pressed(self):
        print(self.number)

for i in range(0,3,1):
    a = Buton(i*100+100,300,str(i))
    a.pllace()
for k in range(0,3,1):
    a = Buton(k*100+100,600,str(k))
    a.pllace()
for b in range(0,3,1):
    a = Buton(b*100+100,900,str(b))
    a.pllace()
        
root.mainloop()
