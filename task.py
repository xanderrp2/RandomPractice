from tkinter import *
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
def prit():
    print(box1.get())
    print(box2.get())
    lable1["text"] = box1.get()
    lable2["text"] = box2.get()
def rem():
    box1.delete(0,END)
    box2.delete(0,END)
box1 = Entry(root)
box1.pack(side=LEFT)
box2 = Entry(root)
box2.pack(side=LEFT)
button1 = Button(root,text = "Clear",width = 200)
button1.pack(side=LEFT)
button2 = Button(root,text = "print",command = prit)
button2.pack(side=BOTTOM)
button3 = Button(root,text = "quit",command = exit)
button3.pack(side=LEFT)
lable1 = Label(root,text="")
lable1.pack()
lable2 = Label(root,text="")
lable2.pack()







root.mainloop()
