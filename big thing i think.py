from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
asa = StringVar()
bsb = StringVar()
nsn = StringVar()
def CAT():
    print("working")
    frame2.pack_forget()
    frameDog.pack_forget()
    frameBIRD.forget()
    frameFISH.forget()
    frameCat.pack(side = RIGHT)
    def title():
        box2.delete(0,END)
        a = box1.get()
        b = a.title()
        
        box2.insert(0,b)
    def uper():
        box2.delete(0,END)
        a = box1.get()
        b = a.upper()
        
        box2.insert(0,b)
    def lower():
        box2.delete(0,END)
        a = box1.get()
        b = a.lower()
        
        box2.insert(0,b)
    def cap():
        box2.delete(0,END)
        a = box1.get()
        b = a.capitalize()
        
        box2.insert(0,b)

    box1 = Entry(frameCat,text = "")
    box1.place(x = 275,y = 300)
    box2 = Entry(frameCat,text = "")
    box2.place(x = 275,y = 400)
    button11 = Button(frameCat,text = "Title",command = title,width = 20, height = 2)
    button11.place(x = 200,y = 600)
    button12 = Button(frameCat,text = "UperCase",command = uper,width = 20, height = 2)
    button12.place(x = 375,y = 600)
    button13 = Button(frameCat,text = "LowerCase",command = lower,width = 20, height = 2)
    button13.place(x = 200,y = 700)
    button14 = Button(frameCat,text = "Capital",command = cap,width = 20, height = 2)
    button14.place(x = 375,y = 700)
    
def DOG():
    print("work")
    frame2.pack_forget()
    frameCat.pack_forget()
    frameBIRD.forget()
    frameFISH.forget()
    frameDog.pack(side = RIGHT)
    def pal():
        if box1.get() == box1.get()[::-1]:
            asa.set("yes")
        elif box1.get() != box1.get()[::-1]:
            asa.set("no")
    def le():
        kh = str(len(box1.get()))
        asa.set(str(kh))

    box1 = Entry(frameDog,text = "")
    box1.place(x = 275,y = 300)
    label = Label(frameDog,textvariable = asa)
    label.place(x = 275,y = 400)
    button1  = Button(frameDog,text = "palendrome",command = pal,width = 20, height = 2)
    button1.place(x = 275,y = 600)
    button2 = Button(frameDog,text = "length",command = le,width = 20, height = 2)
    button2.place(x = 275, y = 700)
def BIRD():
    frame2.pack_forget()
    frameCat.pack_forget()
    frameDog.forget()
    frameFISH.forget()
    frameBIRD.pack(side = RIGHT)
    def od():
        if int(box.get()) %2 == 0:
            bsb.set("even")
        if int(box.get()) %2 == 1:
            bsb.set("odd")
    def mul():
        M = []
        for i in range(1,int(box.get()),1):
            
            if int(box.get())%i == 0:
                
                M.append(i)
            bsb.set(M)
                
    button1 = Button(frameBIRD,text = "odd/even",command = od,width = 20, height = 2)
    button1.place(x = 200,y = 600)
    button12 = Button(frameBIRD,text = "factors",command = mul,width = 20, height = 2)
    button12.place(x = 375,y = 600)
    box = Entry(frameBIRD,text = "")
    box.place(x = 275,y = 300)
    label = Label(frameBIRD,textvariable = bsb)
    label.place(x = 275,y = 400)
##    
def FISH():
    frame2.pack_forget()
    frameCat.pack_forget()
    frameDog.forget()
    frameBIRD.forget()
    frameFISH.pack(side = RIGHT)

    def prime():
        M = []
        for i in range(1,(int(box.get())+ 1),1):
            if  int(box.get())%i == 0:
                M.append(i)
                print(M)
            if len(M)==2 and M[0] == 1 and M[1] == int(box.get()):
                nsn.set("yes")
            else:nsn.set("no")
                    
                

            
                
    def pal():
        if box.get() == box.get()[::-1]:
            nsn.set("yes")
        elif box.get() != box.get()[::-1]:
            nsn.set("no")        

    box = Entry(frameFISH,text = "")
    box.place(x = 275,y = 300)
    label = Label(frameFISH,textvariable = nsn)
    label.place(x = 275,y = 400)
    button1 = Button(frameFISH,text = "Prime number?",command = prime, width = 20, height = 2)
    button1.place(x = 200,y = 600)
    button2 = Button(frameFISH,text = "palandrom",command = pal,width = 20,height = 2)
    button2.place(x = 375,y = 600)





frame1 = Frame(root,width = "300",height = "1000",background = "blue")
frame1.pack(side = LEFT)
button1 = Button(frame1,text = "Strings",command = CAT,width = 20, height = 2)
button1.place(x = 25,y = 150)
button2 = Button(frame1,text = "Advanced Strings",command = DOG,width = 20, height = 2)
button2.place(x = 25,y = 450)
button3 = Button(frame1,text = "numbers",command = BIRD,width = 20, height = 2)
button3.place(x = 25,y = 650)
button4 = Button(frame1,text = "Advanced numbers",command = FISH,width = 20, height = 2)
button4.place(x = 25,y = 950)
frame2 = Frame(root,width = "700",height = "1000",background = "green")
frame2.pack(side = RIGHT)
frameCat = Frame(root,width = "700",height = "1000",background = "red")
frameDog = Frame(root,width = "700",height = "1000",background = "pink")
frameBIRD = Frame(root,width = "700",height = "1000",background = "black")
frameFISH = Frame(root,width = "700",height = "1000",background = "purple")
root.mainloop()
