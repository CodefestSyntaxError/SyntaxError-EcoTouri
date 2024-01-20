from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
from tkinter import messagebox

def home_page():
    global x
    home = tk.Tk()
    home.geometry("360x640")
    home.title("Welcome to Eco-Touri")
    home.configure(bg="#1D3C37")
    
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
    l.grid(row=3, column=0, columnspan=100, rowspan=100,pady=10) 

    home.mainloop()

if __name__ == "__main__":
    home_page()