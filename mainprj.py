from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
from tkinter import messagebox

def login_page():
    login = tk.Tk()
    login.geometry("360x640")
    login.title("Welcome to Eco-Touri")
    login.configure(bg="#1D3C37")
    
    headingimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Loginhead.png")
    headinglabel = Label(login, image=headingimage, highlightthickness=0, borderwidth=0)
    headinglabel.grid(row=0, column=0, columnspan=4)
    
    usernameimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Username.png")
    username_label = tk.Label(login, image=usernameimage, highlightthickness=0, borderwidth=0)
    username_label.grid(row=1,column=0,columnspan=4,pady=20)

    username_entry = tk.Entry(login)
    username_entry.grid(row=2,column=0,columnspan=4,pady=20)

    passwordimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Password.png")
    password_label = tk.Label(login, image=passwordimage, highlightthickness=0, borderwidth=0)
    password_label.grid(row=3,column=0,columnspan=4, pady=20)

    password_entry = tk.Entry(login, show="*") 
    password_entry.grid(row=4,column=0,columnspan=4,pady=20)
    
    def validate_login():
        userid = username_entry.get()
        password = password_entry.get()

        if userid == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    confirmimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Confirmbtn.png")
    confirm_button = tk.Button(login, image=confirmimage, command=validate_login, highlightthickness=0, borderwidth=0)
    confirm_button.grid(row=5,column=0,columnspan=4,pady=20)
    
    login.mainloop()

def home_page():
    global x
    home = tk.Tk()
    home.geometry("360x640")
    home.title("Welcome to Eco-Touri")
    home.configure(bg="#1D3C37")
    
    def close_window():
        home.destroy()
        
    def login_btn():
        close_window()
        login_page()

    headingimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Heading.png")
    headinglabel = Label(home, image=headingimage, highlightthickness=0, borderwidth=0)
    headinglabel.grid(row=0, column=0, columnspan=4)

    homeimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Homebtn.png")
    homebtn = Button(home, image=homeimg, highlightthickness=0, borderwidth=0)
    homebtn.grid(row=1, column=0, columnspan=1)

    recomimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Recombtn.png")
    recombtn = Button(home, image=recomimg, highlightthickness=0, borderwidth=0)
    recombtn.grid(row=1, column=1, columnspan=1)

    tripimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Tripbtn.png")
    tripbtn = Button(home, image=tripimg, highlightthickness=0, borderwidth=0)
    tripbtn.grid(row=1, column=2, columnspan=1)

    reviewimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Reviewbtn.png")
    reviewbtn = Button(home, image=reviewimg, highlightthickness=0, borderwidth=0)
    reviewbtn.grid(row=1, column=3, columnspan=1)

    car1 = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Car1.jpg")
    car2 = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Car2.jpg")
    car3 = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Car3.jpg")
    car4 = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Car4.jpg")
    car5 = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Car5.jpg")

    l = Label(borderwidth=0, highlightthickness=0)
    x = 1
    def carousel():
        global x
        if x == 6: 
            x = 1
        if x == 1: 
            l.config(image=car1) 
        elif x == 2: 
            l.config(image=car2) 
        elif x == 3: 
            l.config(image=car3)
        elif x == 4: 
            l.config(image=car4) 
        elif x == 5: 
            l.config(image=car5) 
        x = x+1
        l.after(3000, carousel)
    carousel()
    l.grid(row=3, column=0, columnspan=4, pady=10) 
    
    descriptionimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Description.png")
    descriptionlabel = Label(home, image=descriptionimage, highlightthickness=0, borderwidth=0)
    descriptionlabel.grid(row=4, column=0, columnspan=4) 
    
    loginbtnimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Loginbtn.png")
    loginbtn = Button(home, image=loginbtnimg, highlightthickness=0, borderwidth=0, command = login_btn)
    loginbtn.grid(row=5, column=0, columnspan=4, pady=10)

    home.mainloop()

if __name__ == "__main__":
    home_page()