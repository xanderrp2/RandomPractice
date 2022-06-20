from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)


def forget():
    frame1.pack_forget()
    frame2.pack()
frame1 = Frame(root,width = "1000",height = "1000",bg = "red")
frame1.pack()
button = Button(frame1,text = "button",command = forget)
button.place(x = 100,y = 100)
frame2 = Frame(root,width = "1000",height = "1000",bg = "blue")




root.mainloop()
