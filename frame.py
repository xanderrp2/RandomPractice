from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
frame = Frame(root,width = "1000",height = "500",highlightbackground = "pink")
frame.pack(side = TOP)
frame2 = Frame(root,width = "1000",height = "500",background = "red")
frame2.pack(side = BOTTOM)





root.mainloop()
