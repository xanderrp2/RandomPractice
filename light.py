from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
def LI(Colour):
    label = Label(root,text = "light",bg = Colour)
    label.place(x = 480,y = 0)

    
button1 = Button(root,text = "ON",command = lambda: LI("YELLOW"))
button1.pack(side = LEFT)
button2 = Button(root,text = "OFF",command = lambda: LI("white"))
button2.pack(side = RIGHT)






root.mainloop()
