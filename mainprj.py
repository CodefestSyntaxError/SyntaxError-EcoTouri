from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
from tkinter import messagebox

def home_page():
    home = tk.Tk()
    home.geometry("360x640")
    home.title("Welcome to Eco-Touri")
    home.configure(bg="#1D3C37")
    
    headingimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Heading.png")
    headinglabel = Label(home, image=headingimage, highlightthickness=0, borderwidth=0)
    headinglabel.grid(row=0, column=0, columnspan=4)

    homeimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Homebtn.png")
    homebtn = Button(home, image=homeimg, highlightthickness=0, borderwidth=0)
    homebtn.grid(row=0, column=1, columnspan=1)

    home.mainloop()

if __name__ == "__main__":
    home_page()