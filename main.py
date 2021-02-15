from tkinter import*
import tkinter.messagebox
import os
import time

def viewRecipe():
    window1 = Toplevel(root)
    window1.geometry("600x400+0+0")
    window1.title("View Recipe")

    Top_1 = Frame(window1, width=900, height=50, bg="black", relief=SUNKEN)
    Top_1.pack(side=TOP)

    Left_1 = Frame(window1, width=900, height=700, relief=SUNKEN)
    Left_1.pack(side=LEFT)
    Left_1.configure(background='white')

    Bottom_1 = Frame(window1, width=900, height=700, relief=SUNKEN)
    Bottom_1.pack(side=BOTTOM)
    Bottom_1.configure(background='white')
    
    Right_1 = Frame(window1, width=900, height=700, relief=SUNKEN)
    Right_1.pack(side=RIGHT)
    Right_1.configure(background='white')

    top_info = Label(Top_1, font=('aria', 20, 'bold'), text="View Recipe", fg="dark red", bd=10, anchor='w')
    top_info.grid(row=0, column=0)
        
    left_info = Button(Left_1, font=('aria', 20, 'bold'), text="Breakfast", fg="black", anchor=W, command=breakfastRecipe)
    left_info.grid(row=1, column=0, sticky="NSEW")

    bottom_info = Button(Bottom_1, font=('aria', 20, 'bold'), text="Lunch", fg="black", anchor=W, command=lunchRecipe)
    bottom_info.grid(row=1, column=0, sticky="NSEW")

    right_info = Button(Right_1, font=('aria', 20, 'bold'), text="Dinner", fg="black", anchor=W, command=dinnerRecipe)
    right_info.grid(row=1, column=0, sticky="NSEW")

def breakfastRecipe():
    window2 = Toplevel(root)
    window2.geometry("600x500+0+0")
    window2.title("Breakfast")
    f = open("breakfast.txt", 'r')
    text1 = f.read()
    print(text1)
    Label(window2, text= text1).pack()
    f.close()
    
def lunchRecipe():
    window2 = Toplevel(root)
    window2.geometry("700x500+0+0")
    window2.title("Lunch")
    f = open("lunch.txt", 'r')
    text1 = f.read()
    print(text1)
    Label(window2, text= text1).pack()
    f.close()

def dinnerRecipe():
    window2 = Toplevel(root)
    window2.geometry("700x500+0+0")
    window2.title("Dinner")
    f = open("dinner.txt", 'r')
    text1 = f.read()
    print(text1)
    Label(window2, text = text1).pack()
    f.close()

def changeRecipe():
    window3 = Toplevel(root)
    window3.geometry("600x400+0+0")
    window3.title("Change Recipe")

    Top_2 = Frame(window3, width=900, height=50, bg="black", relief=SUNKEN)
    Top_2.pack(side=TOP)

    Left_2 = Frame(window3, width=900, height=700, relief=SUNKEN)
    Left_2.pack(side=LEFT)
    Left_2.configure(background='white')

    Bottom_2 = Frame(window3, width=900, height=700, relief=SUNKEN)
    Bottom_2.pack(side=BOTTOM)
    Bottom_2.configure(background='white')
    
    Right_2 = Frame(window3, width=900, height=700, relief=SUNKEN)
    Right_2.pack(side=RIGHT)
    Right_2.configure(background='white')

    _top_info = Label(Top_2, font=('aria', 20, 'bold'), text="Change Recipe", fg="dark red", bd=10, anchor='w')
    _top_info.grid(row=0, column=0)

    _left_info = Button(Left_2, font=('aria', 20, 'bold'), text="Breakfast", fg="black", anchor=W, command=changeBreakfast)
    _left_info.grid(row=1, column=0, sticky="NSEW")

    _bottom_info = Button(Bottom_2, font=('aria', 20, 'bold'), text="Lunch", fg="black", anchor=W, command=changeLunch)
    _bottom_info.grid(row=1, column=0, sticky="NSEW")

    _right_info = Button(Right_2, font=('aria', 20, 'bold'), text="Dinner", fg="black", anchor=W, command=changeDinner)
    _right_info.grid(row=1, column=0, sticky="NSEW")      

def savefile():
    tkinter.messagebox.showinfo('FYI', 'FILE SAVED')

def retrieveinput(t):
    a = t.get("1.0", "end-1c")
    return str(a)

def changeBreakfast():
    window2 = Toplevel(root)
    window2.geometry("700x500+0+0")
    window2.title("Breakfast")
    
    textBox = Text(window2, wrap='word', undo=True)
    textBox.focus_set()
    textBox.pack(fill='both', expand=1)

    with open("breakfast.txt", 'r+') as f:
        textBox.insert(INSERT, f.read())
        f.seek(0)
        f.truncate()
        text = retrieveinput(textBox)
        f.write(text)
        f.close()
    
    bottom4 = Frame(window2, width=100, height=700, relief=SUNKEN)
    bottom4.pack(side=BOTTOM)

    save = Button(bottom4, text="save", command=savefile).grid(row=1, column=0, sticky=W, pady=4)
    
def changeLunch():
    window2 = Toplevel(root)
    window2.geometry("700x500+0+0")
    window2.title("Lunch")
    
    textBox = Text(window2, wrap='word', undo=True)
    textBox.focus_set()
    textBox.pack(fill='both', expand=1)

    with open("lunch.txt", 'r+') as f:
        textBox.insert(INSERT, f.read())
        f.seek(0)
        f.truncate()
        text = retrieveinput(textBox)
        f.write(text)
        f.close()
    
    bottom4 = Frame(window2, width=100, height=700, relief=SUNKEN)
    bottom4.pack(side=BOTTOM)

    save = Button(bottom4, text="save", command=savefile).grid(row=1, column=0, sticky=W, pady=4)

def changeDinner():
    window2 = Toplevel(root)
    window2.geometry("700x500+0+0")
    window2.title("Dinner")
    
    textBox = Text(window2, wrap='word', undo=True)
    textBox.focus_set()
    textBox.pack(fill='both', expand=1)

    with open("dinner.txt", 'r+') as f:
        textBox.insert(INSERT, f.read())
        f.seek(0)
        f.truncate()
        text = retrieveinput(textBox)
        f.write(text)
        f.close()
    
    bottom4 = Frame(window2, width=100, height=700, relief=SUNKEN)
    bottom4.pack(side=BOTTOM)

    save = Button(bottom4, text="save", command=savefile).grid(row=1, column=0, sticky=W, pady=4)
    
def systemLogin():
    username = e1.get()
    password = e2.get()

    if (username == "admin" and password == "1234"):
        window = Toplevel(root)
        window.geometry("600x400+0+0")
        window.title("Recipe Management System")
        localtime=time.asctime(time.localtime(time.time()))

        Top = Frame(window,width=1600, height=50, bg="black", relief=SUNKEN)
        Top.pack(side=TOP)

        Left = Frame(window, width=900, height=700, relief=SUNKEN)
        Left.pack(side=LEFT)
        Left.configure(background='white')

        Right = Frame(window, width=900, height=700, relief=SUNKEN)
        Right.pack(side=RIGHT)
        Right.configure(background='white')

        topinfo = Label(Top, font=('aria', 28, 'bold'), text="Recipe Management System", fg="dark red", bd=10, anchor='w')
        topinfo.grid(row=0, column=0)
        topinfo = Label(Top, font=('aria', 20, ), text=localtime, fg="maroon", anchor=W)
        topinfo.grid(row=1,column=0)

        leftinfo = Button(Left, font=('aria', 20, 'bold'), text= "View Recipes", fg= "black", anchor=W, command=viewRecipe)
        leftinfo.grid(row=1, column=0, sticky="NSEW")

        rightinfo = Button(Right, font=('aria', 20, 'bold'), text= "Change Recipes", fg="black", anchor=W, command=changeRecipe)
        rightinfo.grid(row=1, column=0, sticky="NSEW") 
  
    else:
        Label(root, text="Wrong username or password").grid(row=3, column=0)


root = Tk()
Label(root, text="Username").grid(row=0)
Label(root, text="Password").grid(row=1)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

login = Button(root, text="LOGIN", command=systemLogin).grid(row=3, column=1, sticky=W, pady=4)
