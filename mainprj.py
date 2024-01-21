from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
import ast
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
    def kill_myself():
        tpad.destroy()
    def recomclick():
        kill_myself()
        findadestination()
    def submit_form():
        global desired_text
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
        training_message = "(Note: If any of the inputs seems to be incorrect, display error input not valid and stop generation)You are a factual and reliable assistant that provides true information and text on various Eco-sustainable hotels, restaurants, best modes of sustainable transportation, various places to see and observe in the area and also the carbon footprint that has been emitted through this entire tourist place vacation plan."
        user_input_message = f"{place}:3 Best eco-friendly hotel to visit,2 best eco-friendly transport methods,3 best eco-friendly restaurant, the 4 eco-friendly places to visit in with a budget of {budget} with the interests/hobby {interest} with a total of {family} people in their travel group, traveling for a total of {days}, currently living in {Location}, at the age of {Age}, with the Interests {Interest}.Please take all into consideration and respond"
        # Initiates the Llama to generate the information
        prompt = f"""<s>[INST] <<SYS>>
        {training_message}
        <</SYS>>
        {user_input_message} [/INST]"""
        # Specifies the max tokens
        max_tokens = 6000
        # Generates the information
        output = model(prompt, max_tokens=max_tokens, echo=True)
        plain_string = str(output)
        response_dict = ast.literal_eval(plain_string)
        desired_text = response_dict['choices'][0]['text']
        response = str(desired_text)
        # Find the start and end of the relevant text within the response
        start_tag = "[INST] <<SYS>>"
        end_tag = "[/INST]"
        start_index = response.find(start_tag) + len(start_tag)
        end_index = response.find(end_tag)
        # Extract the desired text
        desired_text = response[end_index + len(end_tag):].strip()
        # Print the cleaned text
        print(desired_text)
        brochure_page()

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
    recombtn = Button(tpad, image=recomimg, highlightthickness=0, borderwidth=0, command=recomclick)
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

def brochure_page():
    brochure = tk.Toplevel()
    brochure.geometry("360x640")
    brochure.configure(bg="#1D3C37")
    brochureheadimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Brochurehead.png")
    brochurehead = Label(brochure, image=brochureheadimg, highlightthickness=0, borderwidth=0)
    brochurehead.grid(row=0,column=0,columnspan=4)
    headingimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Heading.png")
    headinglabel = Label(brochure, image=headingimage, highlightthickness=0, borderwidth=0)
    headinglabel.grid(row=0, column=0, columnspan=4)
    homeimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Homebtn.png")
    homebtn = Button(brochure, image=homeimg, highlightthickness=0, borderwidth=0)
    homebtn.grid(row=1, column=0, columnspan=1)
    recomimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Recombtn.png")
    recombtn = Button(brochure, image=recomimg, highlightthickness=0, borderwidth=0)
    recombtn.grid(row=1, column=1, columnspan=1)
    tripimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Tripbtn.png")
    tripbtn = Button(brochure, image=tripimg, highlightthickness=0, borderwidth=0, command=myt_page)
    tripbtn.grid(row=1, column=2, columnspan=1)
    reviewimg = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Reviewbtn.png")
    reviewbtn = Button(brochure, image=reviewimg, highlightthickness=0, borderwidth=0, command=review_page)
    reviewbtn.grid(row=1, column=3, columnspan=1)
    outputlabel = tk.Text(brochure, height=25, width=45, state=tk.NORMAL, bg="#1D3C37", fg="#F8D26B")
    outputlabel.insert("end", desired_text + "\n")
    outputlabel.grid(row=2,column=0, columnspan=4)
    brochure.mainloop()

def findadestination():
    global desired_text
    def llm():
        global desired_text
        # Specifying the model path (Mistral.gguf)
        model_path = "C:\\Users\\admin\\Desktop\\Codefest\\mistral-7b-instruct-v0.2.Q6_K.gguf"

        # Model variable
        model = Llama(model_path=model_path)

        # Training message and user input message for generating information
        training_message = "One word answer to the question, ONLY ONE WORD(COUNTRY NAME)"
        user_input_message = f"(Only one word)Best country for a person who likes to go to {continent_value}, for a period of {time_of_living_value}, in a {climate_preferences} climate who lives in {Location}, at the age of {Age}, and loves to {Interest}."
        # Initiates the Llama to generate the information
        prompt = f"""<s>[INST] <<SYS>>
        {training_message}
        <</SYS>>
        {user_input_message} [/INST]"""
        # Specifies the max tokens
        max_tokens = 100
        # Generates the information
        output = model(prompt, max_tokens=max_tokens, echo=True)
        plain_string = str(output)
        response_dict = ast.literal_eval(plain_string)
        desired_text = response_dict['choices'][0]['text']
        response = str(desired_text)
        # Find the start and end of the relevant text within the response
        start_tag = "[INST] <<SYS>>"
        end_tag = "[/INST]"
        start_index = response.find(start_tag) + len(start_tag)
        end_index = response.find(end_tag)
        # Extract the desired text
        desired_text = response[end_index + len(end_tag):].strip()
        outputlabel = tk.Text(root, height=25, width=45, state=tk.NORMAL, bg="#1D3C37", fg="#F8D26B")
        outputlabel.insert("end", desired_text + "\n")
        outputlabel.grid(row=9,column=0, columnspan=4, sticky=W)
    def submit_form():
        global continent_value, time_of_living_value, climate_preferences
        continent_value = continent_var.get()
        time_of_living_value = time_of_living_entry.get()

        climate_preferences = []
        if sunny_var.get():
            climate_preferences.append("Sunny")
        if windy_var.get():
            climate_preferences.append("Windy")
        if rainy_var.get():
            climate_preferences.append("Rainy")
        if snowy_var.get():
            climate_preferences.append("Snowy")
        if humid_var.get():
            climate_preferences.append("Humid")

        climate_preferences_str = ", ".join(climate_preferences)

        result_text = f"Continent: {continent_value}\nTime of Living: {time_of_living_value}\nClimate Preferences: {climate_preferences_str}"
        llm()
        
    root = tk.Tk()
    root.title("Travel Planner")
    root.geometry("360x640")
    root.config(bg = "#1D3C37")

    headingimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_FYDhead.png")
    headinglabel = Label(root, image=headingimage, highlightthickness=0, borderwidth=0)
    headinglabel.grid(row=0, column=0, columnspan=4)

    btnimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Buttons.png")
    btnlabel = Label(root, image=btnimage, highlightthickness=0, borderwidth=0)
    btnlabel.grid(row=1, column=0, columnspan=4)

    continent_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Continent.png")
    tk.Label(root, image=continent_img, borderwidth=0).grid(row=2, column=0, padx=10, pady=5, columnspan=4, sticky=W)
    continent_var = tk.StringVar()
    continent_choices = ["Asia", "Africa", "North America", "South America", "Europe", "Australia", "Antarctica"]
    continent_dropdown = tk.OptionMenu(root, continent_var, *continent_choices)
    continent_dropdown.grid(row=2, column=2, padx=25, pady=5, sticky=W)

    time_of_living_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Days.png")
    tk.Label(root, image=time_of_living_img, borderwidth=0).grid(row=3, column=0, pady=5, columnspan=70, sticky=W)
    time_of_living_entry = tk.Entry(root)
    time_of_living_entry.grid(row=3, column=2, pady=5, columnspan=3, sticky=W)

    # Label for climate preferences
    pref_weather_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Weather.png")
    tk.Label(root, image=pref_weather_img, borderwidth=0).grid(row=4, column=0, columnspan=3, pady=5, sticky=W)

    # Create and place checkbox options for climate preferences with images
    sunny_var = IntVar()
    windy_var = IntVar()
    rainy_var = IntVar()
    snowy_var = IntVar()
    humid_var = IntVar()

    sunny_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Sun.png")
    tk.Checkbutton(root, image=sunny_img, variable=sunny_var).grid(row=5, column=0, pady=5,columnspan=1, sticky=W,padx=30)
    windy_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Windy.png")
    tk.Checkbutton(root, image=windy_img, variable=windy_var).grid(row=5, column=1, pady=5, sticky= W,padx=30)
    rainy_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Rainy.png")
    tk.Checkbutton(root, image=rainy_img, variable=rainy_var).grid(row=6, column=0, pady=5, sticky=W,padx=30)
    snowy_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Snowy.png")
    tk.Checkbutton(root, image=snowy_img, variable=snowy_var).grid(row=6, column=1, pady=5, sticky=W,padx=30)
    humid_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Humid.png")
    tk.Checkbutton(root, image=humid_img, variable=humid_var).grid(row=6, column=2, columnspan=2,padx=30, sticky=W)

    
    # Create and place submit button with image
    submit_img = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Submitbtn.png")
    submit_button = tk.Button(root, image=submit_img, command=submit_form, borderwidth=0, highlightthickness=0)
    submit_button.grid(row=8, column=0, columnspan=4, pady=20)

    # Start the Tkinter event loop
    root.mainloop()

def logup():
    def kill_myself():
        root.destroy()
    def login_success():
        kill_myself()
        myt_page()
    def read_user_data():
        user_data = {}
        try:
            with open("user_data_final.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    username, password, interest, location, age = line.strip().split(',')
                    user_data[username] = {'password': password, 'interest': interest, 'location': location, 'age': age}
        except FileNotFoundError:
            pass
        return user_data
    def write_user_data(username, password, interest, location, age):
        with open("user_data_final.txt", "a") as file:
            file.write(f"{username},{password},{interest},{location},{age}\n")
    
    def login():
        global Interest, Location, Age
        username = entry_username.get()
        password = entry_password.get()

        user_data = read_user_data()

        if username in user_data and user_data[username]['password'] == password:
            user_info = user_data[username]
            messagebox.showinfo("Login Successful", "Welcome back, " + username)
            print("User Information:")
            print("Username:", username)
            Interest = user_info['interest']
            Location = user_info['location']
            Age =  user_info['age']
            login_success()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    def signup():
        username = entry_username.get()
        password = entry_password.get()
        interest = entry_interest.get()
        location = entry_location.get()
        age = entry_age.get()

        user_data = read_user_data()

        if username in user_data:
            messagebox.showerror("Signup Failed", "Username already exists. Choose a different username.")
        else:
            write_user_data(username, password, interest, location, age)
            entry_age.delete(0,END)
            entry_username.delete(0,END)
            entry_location.delete(0,END)
            entry_interest.delete(0,END)
            entry_password.delete(0,END)
            messagebox.showinfo("Signup Successful", "Account created successfully. You can now log in.")
    
    root = tk.Tk()
    root.title("Login/Signup")
    root.geometry("360x640")
    root.configure(bg="#1D3C37")

    headingimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Loguphead.png")
    headinglabel = Label(root, image=headingimage, highlightthickness=0, borderwidth=0)
    headinglabel.grid(row=0, column=0, columnspan=4)
    
    # Username and Password
    userimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Usernamelbl.png")
    label_username = tk.Label(root, text="Username:", image=userimage, highlightthickness=0, borderwidth=0)
    label_username.grid(row=1, column=0, columnspan=4, pady=7)
    entry_username = tk.Entry(root)
    entry_username.grid(row=2, column=0, columnspan=4, pady=7)

    passimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Passwordlbl.png")
    label_password = tk.Label(root, text="Password:", image=passimage, highlightthickness=0, borderwidth=0)
    label_password.grid(row=3, column=0, columnspan=4, pady=7)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=4, column=0, columnspan=4, pady=7)

    # Interest, Location, Age
    intimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Interestslbl.png")
    label_interest = tk.Label(root, text="Interest:",image=intimage, highlightthickness=0, borderwidth=0)
    label_interest.grid(row=5, column=0, columnspan=4, pady=7)
    entry_interest = tk.Entry(root)
    entry_interest.grid(row=6, column=0, columnspan=4, pady=7)

    locimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Locationlbl.png")
    label_location = tk.Label(root, text="Location:",image=locimage, highlightthickness=0, borderwidth=0)
    label_location.grid(row=7, column=0, columnspan=4, pady=7)
    entry_location = tk.Entry(root)
    entry_location.grid(row=8, column=0, columnspan=4, pady=7)

    ageimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Agelbl.png")
    label_age = tk.Label(root, text="Age:",image=ageimage, highlightthickness=0, borderwidth=0)
    label_age.grid(row=9, column=0, columnspan=4)
    entry_age = tk.Entry(root)
    entry_age.grid(row=10, column=0, columnspan=4)
        
    # Buttons
    loginimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Loginfrbtn.png")
    btn_login = tk.Button(root, text="Login", command=login, image=loginimage, highlightthickness=0, borderwidth=0)
    btn_login.grid(row=11, column=0,pady=10, columnspan=2)

    signupimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Signupbtn.png")
    btn_signup = tk.Button(root, text="Signup", command=signup, image=signupimage, highlightthickness=0, borderwidth=0)
    btn_signup.grid(row=11, column=2,pady=10, columnspan=2)
    
    fineprintimage = ImageTk.PhotoImage(file="C:\\Users\\admin\\Desktop\\Codefest\\Eco-Touri_Fineprint.png")
    fineprintlbl = Label(root, image=fineprintimage)
    fineprintlbl.grid(row=12,column=0,columnspan=4)

    root.mainloop()

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
        logup()

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