from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a = IntVar()
a.set(9999)
labeltezt = Label(root,text="c",textvariable = a)
labeltezt.pack(side = TOP)
##frame1 = Frame(root,width = "1000",height = "250",bg = "red")
##frame1.pack(side = TOP)
##label = Label(frame1,text = "What is better?")
##label.place(x = 125,y = 125)
##button1 = Radiobutton(frame1,text = "dog",value = 0, variable = a)
##button1.place(x = 350,y = 150)
##button2 = Radiobutton(frame1,text = "cat",value = 1, variable = a)
##button2.place(x= 350,y = 175)
##frame2 = Frame(root,width = "1000",height = "250",bg = "blue")
##frame2.pack(side = TOP)
##label = Label(frame2,text = "What is better?")
##label.place(x = 125,y = 125)
##button1 = Radiobutton(frame2,text = "food",value = 0, variable = a)
##button1.place(x = 350,y = 150)
##button2 = Radiobutton(frame2,text = "pizza",value = 1, variable = a)
##button2.place(x= 350,y = 175)
##frame3 = Frame(root,width = "1000",height = "250",bg = "green")
##frame3.pack(side = TOP)
##label = Label(frame3,text = "What is better?")
##label.place(x = 125,y = 125)
##button1 = Radiobutton(frame3,text = "apples",value = 0, variable = a)
##button1.place(x = 350,y = 150)
##button2 = Radiobutton(frame3,text = "caramle",value = 1, variable = a)
##button2.place(x= 350,y = 175)
##frame4 = Frame(root,width = "1000",height = "250",bg = "purple")
##frame4.pack(side = TOP)
##label = Label(frame4,text = "What is better?")
##label.place(x = 125,y = 125)
##button1 = Radiobutton(frame4,text = "candy",value = 0, variable = a)
##button1.place(x = 350,y = 150)
##button2 = Radiobutton(frame4,text = "sun",value = 1, variable = a)
##button2.place(x= 350,y = 175)
##
##

root.mainloop()
