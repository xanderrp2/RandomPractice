from tkinter import *
from tkinter import messagebox
import sqlite3
connection = sqlite3.connect("Passwords.db")
cursor = connection.cursor()
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="red")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)


def sign_up():
    a = box1.get()
    b = box2.get()
    cursor.execute("SELECT * FROM passwords")
    data = cursor.fetchall()

    for i in data:
        if a in i[0]:
            b.set(i[1])
            print("you are already signed up")
        else:
            print("INSERT INTO words values("+'"'+ str(a) +'"'+","+'"'+ str(b) +'"'+");")
            cursor.execute("INSERT INTO words values("+'"'+ str(a) +'"'+","+'"'+ str(b) +'"'+");")
        
        


def login():
    print("working")


label1 = Label(root,text = "Email")
label1.grid(row = 2,column = 2, padx = 2,pady = 2)
label2 = Label(root,text = "Password")
label2.grid(row = 3,column = 2, padx = 2,pady = 2)
box1 = Entry(root)
box1.grid(row = 2,column = 3,padx = 2,pady = 2)
box2 = Entry(root)
box2.grid(row = 3,column = 3,padx = 2,pady = 2)
button1 = Button(root,text = "Sign Up?",command = sign_up)
button1.grid(columnspan = 2, row = 4, column = 2, padx = 2, pady = 2)
button2 = Button(root,text = "Login?",command = login)
button2.grid(columnspan = 2, row = 5, column = 2, padx = 2, pady = 2)

root.mainloop()
