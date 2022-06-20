from tkinter import *
import webcolors
from tkinter import messagebox
from tkinter import filedialog as fd



root = Tk()
root.title("CATS")
root.geometry("400x200")
root.resizable(width=True,height=True)
root.configure(bg="snow")

file_name = None

def New():
    global file_name
    Test.delete("1.0",END)
def Save():
    global file_name
    if file_name == None:
        file_name = fd.asksaveasfilename()
        a = open(file_name,"w")
        a.write(Test.get("1.0",END))
        a.close()
    else:
        a = open(file_name,"w")
        a.write(Test.get("1.0",END))
        a.close()
    
def Open():
    Test.delete("1.0",END)
    global file_name
    file_name = fd.askopenfilename()
    a = open(file_name,"r")
    I = a.read()
    Test.insert(END,I)
    a.close()
def about():
    print("about")
def EXIT():
    exit()
    
#does not appear on the window, look up
Menubar = Menu(root)
filemen = Menu(Menubar,tearoff = 100)
filemen1 = Menu(Menubar,tearoff = 100)
filemen.add_command(label = "New",command = New)
filemen.add_command(label = "Open",command = Open)
filemen.add_command(label = "Save",command = Save)
filemen.add_command(label = "EXIT",command = EXIT)
Menubar.add_cascade(label = "file", menu = filemen)
Menubar.add_cascade(label = "Help", menu = filemen1)
filemen1.add_command(label = "About",command = about)

Test = Text(root, height = 100, width = 100)
Test.grid(row = 1, column = 0)


root.config(menu= Menubar)
root.mainloop()
