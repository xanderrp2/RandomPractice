from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)

    
class thing():
    def pressed(self):
        for i in range(self.y ,1000,50):
                a = thing(i,self.y,"texting")
                a.pllace()
        for i in range(self.x ,1000,50):
                a = thing(self.x,i,"texting")
                a.pllace()
        


    def __init__(self,x,y,text):
        self.x = x
        self.y = y
        self.text = text
        self.button = Button(root,text = self.text, command = self.pressed) 
    def pllace(self):
        self.button.place(x = self.x, y = self.y)




for i in range(0,1000,50):
    a = thing(i,i,"texting")
    a.pllace()




root.mainloop()
