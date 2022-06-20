from tkinter import *
import time
root = Tk()
root.title("CATS")
root.geometry("100x100")
root.resizable(width=True,height=True)
root.configure(bg="snow")
case = IntVar()
cats = StringVar()
dogs = False
def stop():
    global dogs
    dogs = False
    root.update()
def does():
    global dogs
    case=0
    dogs = True
    while True:
        cats.set(case)
        root.update()
        time.sleep(1)
        case = case + 1

buttonStart = Button(root,text = "start",command = does)
buttonStart.pack(side=BOTTOM)
buttonStart = Button(root,text = "stop",command = stop)
buttonStart.pack(side=BOTTOM)
screen = Label(root,textvariable = cats,relief = RIDGE)
screen.pack()





root.mainloop()
