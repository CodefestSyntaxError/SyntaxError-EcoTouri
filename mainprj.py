from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
from tkinter import messagebox
from llama_cpp import Llama

def review_page():
    def add_review():
        new_review = review_entry.get("1.0", "end-1c")
        reviews.append(new_review)
        update_reviews_text()
        save_reviews()

    def update_reviews_text():
        reviews_text.delete("1.0", "end")
        for review in reviews:
            reviews_text.insert("end", review + "\n")

    def save_reviews():
        global file_path
        if file_path:
            with open(file_path, "w") as file:
                for review in reviews:
                    file.write(review + "\n")

    global file_path
    reviews = []

    review = tk.Toplevel()
    review.title("Reviews")
    review.geometry("360x640")
    review.config(bg="#1D3C37")
        
    headingimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Loginhead.png")
    headinglabel = Label(review, image=headingimage, highlightthickness=0, borderwidth=0)
    headinglabel.grid(row=0, column=0, columnspan=4)

    review_image = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Reviewhead.png")
    review_label = tk.Label(review, image=review_image, highlightthickness=0, borderwidth=0)
    review_label.grid(row=0, column=0, columnspan=4)

    home_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Homebtn.png")
    home_btn = Button(review, image=home_img, highlightthickness=0, borderwidth=0)
    home_btn.grid(row=2, column=0)

    recom_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Recombtn.png")
    recom_btn = Button(review, image=recom_img, highlightthickness=0, borderwidth=0)
    recom_btn.grid(row=2, column=1)

    trip_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Tripbtn.png")
    trip_btn = Button(review, image=trip_img, highlightthickness=0, borderwidth=0)
    trip_btn.grid(row=2, column=2)

    review_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Reviewbtn.png")
    review_btn = Button(review, image=review_img, highlightthickness=0, borderwidth=0)
    review_btn.grid(row=2, column=3)

    review_entry = tk.Text(review, height=10, width=30, state=tk.NORMAL)
    review_entry.grid(row=4, column=0, columnspan=4)

    
    add_review_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Confirmbtn.png")
    add_review_btn = tk.Button(review, text="Add Review", command=add_review, image=add_review_img, highlightthickness=0, borderwidth=0)
    add_review_btn.grid(row=5, column=0, columnspan=4)

    reviews_label = tk.Label(review, text="Reviews:", fg="black")
    reviews_label.grid(row=6, column=0, columnspan=4)
    
    entreviewimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_EntReviewlbl.png")
    entreviews_label = tk.Label(review, image=entreviewimage, highlightthickness=0, borderwidth=0)
    entreviews_label.grid(row=3, column=0, columnspan=4)

    # Ask user for file path or use default
    file_path = "C:\\Users\\admin\\Desktop\\Codefest\\reviews.txt"
    if not file_path:
        file_path = "C:\\Users\\admin\\Desktop\\Codefest\\reviews.txt"

    reviews_text = tk.Text(review, height=10, width=30)
    reviews_text.grid(row=6, column=0, columnspan=4)

    # Load reviews from the selected or default file
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            reviews = file.read().splitlines()
    update_reviews_text()

    review.mainloop()

def myt_page():
    def submit_form():
        place = country_entry.get()
        budget = budget_entry.get()
        interest = interests_entry.get()
        days = days_entry.get()
        family = family_entry.get()

        # Specifying the model path (Mistral.gguf)
        model_path = "C:\\Users\\admin\\Desktop\\Codefest\\mistral-7b-instruct-v0.2.Q6_K.gguf"

        # Model variable
        model = Llama(model_path=model_path)

        # Training message and user input message for generating information
        training_message = "You are a factual and reliable assistant that provides true information and text on various Eco-sustainable hotels, restaurants, best modes of sustainable transportation, various places to see and observe in the area and also the carbon footprint that has been emitted through this entire tourist place vacation plan."
        user_input_message = f"{place}:The Best eco-friendly hotel to visit,the best eco-friendly transport methods,the best eco-friendly restaurant, the best eco-friendly places to visit in with a budget of {budget} with the interests {interest} with a total of {family} people in their travel group, traveling for a total of {days}."
        # Initiates the Llama to generate the information
        prompt = f"""<s>[INST] <<SYS>>
        {training_message}
        <</SYS>>
        {user_input_message} [/INST]"""
        # Specifies the max tokens
        max_tokens = 10
        # Generates the information
        output = model(prompt, max_tokens=max_tokens, echo=True)
        # Printing the output
        print(output)

     #Create main window
    tpad = tk.Tk()
    tpad.title("Trip plan advisor")
    tpad.geometry("360x640")
    tpad.configure(bg="#1D3C37")
    
    headingimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_TripTitle.png")
    headinglabel = Label(tpad, image=headingimage, highlightthickness=0, borderwidth=0)
    headinglabel.grid(row=0, column=0, columnspan=4)
    
    headingimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Heading.png")
    headinglabel = Label(tpad, image=headingimage, highlightthickness=0, borderwidth=0)
    headinglabel.grid(row=0, column=0, columnspan=4)
    homeimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Homebtn.png")
    homebtn = Button(tpad, image=homeimg, highlightthickness=0, borderwidth=0)
    homebtn.grid(row=1, column=0, columnspan=1)
    recomimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Recombtn.png")
    recombtn = Button(tpad, image=recomimg, highlightthickness=0, borderwidth=0)
    recombtn.grid(row=1, column=1, columnspan=1)
    tripimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Tripbtn.png")
    tripbtn = Button(tpad, image=tripimg, highlightthickness=0, borderwidth=0, command=myt_page)
    tripbtn.grid(row=1, column=2, columnspan=1)
    reviewimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Reviewbtn.png")
    reviewbtn = Button(tpad, image=reviewimg, highlightthickness=0, borderwidth=0, command=review_page)
    reviewbtn.grid(row=1, column=3, columnspan=1)

    # Create and place input widgets
    countryimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_CountryInput.png")
    county_label = Label(tpad, text="Country:",image=countryimg, highlightthickness=0, borderwidth=0)
    county_label.grid(row=2, column=0, pady=5,columnspan=8, sticky=W)
    country_entry = tk.Entry(tpad)
    country_entry.grid(row=2, column=2, pady=5,padx=10,columnspan=2, sticky=W)

    memberimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_MemberInput.png")
    member_label = Label(tpad, text="Country:",image=memberimg, highlightthickness=0, borderwidth=0)
    member_label.grid(row=3, column=0, pady=5,columnspan=8, sticky=W)
    family_entry = tk.Entry(tpad)
    family_entry.grid(row=3, column=2, pady=5,padx=10,columnspan=2, sticky=W)

    daysimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_DaysInput.png")
    days_label = Label(tpad, text="Country:",image=daysimg, highlightthickness=0, borderwidth=0)
    days_label.grid(row=4, column=0, pady=5,columnspan=8, sticky=W)
    days_entry = tk.Entry(tpad)
    days_entry.grid(row=4, column=2, pady=5,padx=10,columnspan=2, sticky=W)

    interestsimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_InterestsInput.png")
    interests_label = Label(tpad, text="Country:",image=interestsimg, highlightthickness=0, borderwidth=0)
    interests_label.grid(row=5, column=0, pady=5,columnspan=8, sticky=W)
    interests_entry = tk.Entry(tpad)
    interests_entry.grid(row=5, column=2, pady=5,padx=10,columnspan=2, sticky=W)

    budgetimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_BudgetInput.png")
    budget_label = Label(tpad, text="Country:",image=budgetimg, highlightthickness=0, borderwidth=0)
    budget_label.grid(row=6, column=0, pady=5,columnspan=8, sticky=W)
    budget_entry = tk.Entry(tpad)
    budget_entry.grid(row=6, column=2, pady=5,padx=10,columnspan=2, sticky=W)

    # Create and place submit button
    submitimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Confirmbtn.png")
    submit_button = tk.Button(tpad, text="Submit", command=submit_form, image=submitimg, highlightthickness=0, borderwidth=0)
    submit_button.grid(row=7, column=0, columnspan=4, pady=10)

    # Start the Tkinter event loop
    tpad.mainloop()


def login_page():
    login = tk.Tk()
    login.geometry("360x640")
    login.title("Welcome to Eco-Touri")
    login.configure(bg="#1D3C37")
    
    def kill_login():
        login.destroy()
    
    def confirm_btn():
        kill_login()
        myt_page()

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
            confirm_btn()
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
    tripbtn = Button(home, image=tripimg, highlightthickness=0, borderwidth=0, command=myt_page)
    tripbtn.grid(row=1, column=2, columnspan=1)
    reviewimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Reviewbtn.png")
    reviewbtn = Button(home, image=reviewimg, highlightthickness=0, borderwidth=0, command=review_page)
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
