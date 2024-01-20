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
    home.mainloop()

if __name__ == "__main__":
    home_page()