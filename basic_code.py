from tkinter import *
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
lable = Label(root,text="talk")
lable.pack()

box = Entry(root)
box.pack()
lable1 = Label(root,text="")
lable1.pack()
def run():
    
    lable1["text"] = box.get()
    
    print(box.get())
bouton = Button(root,text="press",command = run,fg = "pink")
bouton.pack()








root.mainloop()
