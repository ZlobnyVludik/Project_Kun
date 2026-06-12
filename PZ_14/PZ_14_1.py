from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sign Up")
root.geometry("600x700")
root.resizable(False, False)

title_label = Label(root, text="Sign Up", font=("Arial", 24, "bold"))
title_label.place(x=50, y=30)

first_name_label = Label(root, text="First Name", font=("Arial", 10))
first_name_label.place(x=50, y=100)
first_name_entry = Entry(root, width=30, font=("Arial", 12))
first_name_entry.place(x=50, y=125)

last_name_label = Label(root, text="Last Name", font=("Arial", 10))
last_name_label.place(x=320, y=100)
last_name_entry = Entry(root, width=30, font=("Arial", 12))
last_name_entry.place(x=320, y=125)

screen_name_label = Label(root, text="Screen Name", font=("Arial", 10))
screen_name_label.place(x=50, y=170)
screen_name_entry = Entry(root, width=30, font=("Arial", 12))
screen_name_entry.place(x=50, y=195)

dob_label = Label(root, text="Date of Birth", font=("Arial", 10))
dob_label.place(x=50, y=240)

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
month_var = StringVar(root)
month_var.set("May")
month_menu = OptionMenu(root, month_var, *months)
month_menu.config(width=8)
month_menu.place(x=50, y=265)

days = [str(i) for i in range(1, 32)]
day_var = StringVar(root)
day_var.set("5")
day_menu = OptionMenu(root, day_var, *days)
day_menu.config(width=4)
day_menu.place(x=150, y=265)

years = [str(i) for i in range(1980, 2026)]
year_var = StringVar(root)
year_var.set("1985")
year_menu = OptionMenu(root, year_var, *years)
year_menu.config(width=6)
year_menu.place(x=220, y=265)

gender_label = Label(root, text="Gender", font=("Arial", 10))
gender_label.place(x=50, y=310)
gender_var = StringVar(root)
gender_var.set("Male")
male_radio = Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.place(x=50, y=335)
female_radio = Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.place(x=130, y=335)

country_label = Label(root, text="Country", font=("Arial", 10))
country_label.place(x=50, y=370)
countries = ["USA", "Canada", "UK", "Australia", "Germany", "France", "Russia"]
country_var = StringVar(root)
country_var.set("USA")
country_menu = OptionMenu(root, country_var, *countries)
country_menu.config(width=20)
country_menu.place(x=50, y=395)

email_label = Label(root, text="E-mail", font=("Arial", 10))
email_label.place(x=320, y=240)
email_entry = Entry(root, width=30, font=("Arial", 12))
email_entry.place(x=320, y=265)

phone_label = Label(root, text="Phone", font=("Arial", 10))
phone_label.place(x=320, y=310)
phone_entry = Entry(root, width=30, font=("Arial", 12))
phone_entry.place(x=320, y=335)

password_label = Label(root, text="Password", font=("Arial", 10))
password_label.place(x=320, y=370)
password_entry = Entry(root, width=30, font=("Arial", 12), show="*")
password_entry.place(x=320, y=395)

confirm_label = Label(root, text="Confirm Password", font=("Arial", 10))
confirm_label.place(x=320, y=440)
confirm_entry = Entry(root, width=30, font=("Arial", 12), show="*")
confirm_entry.place(x=320, y=465)

agree_var = IntVar()
agree_check = Checkbutton(root, text="I agree to the Terms of Use", variable=agree_var)
agree_check.place(x=50, y=500)

def submit_action():
    pass

def cancel_action():
    root.destroy()

submit_button = Button(root, text="submit", bg="green", fg="white",
                       font=("Arial", 12), width=10, command=submit_action)
submit_button.place(x=50, y=560)

cancel_button = Button(root, text="Cancel", bg="red", fg="white",
                       font=("Arial", 12), width=10, command=cancel_action)
cancel_button.place(x=180, y=560)

root.mainloop()
