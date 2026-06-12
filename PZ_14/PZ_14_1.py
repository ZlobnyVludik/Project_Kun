from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sign Up")
root.geometry("560x640")
root.configure(bg="#2b2d42")
root.resizable(False, False)

header = Frame(root, bg="#f0a500", height=45)
header.pack(fill=X)
header.pack_propagate(False)

header_label = Label(header, text="Sign Up", bg="#f0a500", fg="yellow",
                     font=("Arial", 14, "bold"))
header_label.pack(side=LEFT, padx=10, pady=8)

form_frame = Frame(root, bg="#2b2d42")
form_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

label_opts = {"bg": "#2b2d42", "fg": "yellow", "font": ("Arial", 10), "anchor": "e", "width": 16}
entry_opts = {"font": ("Arial", 10), "bd": 0, "relief": "flat", "bg": "white"}

Label(form_frame, text="First Name", **label_opts).grid(row=0, column=0, padx=10, pady=8, sticky=E)
first_name_entry = Entry(form_frame, width=35, **entry_opts)
first_name_entry.insert(0, "Enter First Name...")
first_name_entry.grid(row=0, column=1, columnspan=4, padx=5, pady=8, sticky=W)

Label(form_frame, text="Last Name", **label_opts).grid(row=1, column=0, padx=10, pady=8, sticky=E)
last_name_entry = Entry(form_frame, width=35, **entry_opts)
last_name_entry.insert(0, "Enter Last Name...")
last_name_entry.grid(row=1, column=1, columnspan=4, padx=5, pady=8, sticky=W)

Label(form_frame, text="Screen Name", **label_opts).grid(row=2, column=0, padx=10, pady=8, sticky=E)
screen_name_entry = Entry(form_frame, width=35, **entry_opts)
screen_name_entry.insert(0, "Enter Screen Name...")
screen_name_entry.grid(row=2, column=1, columnspan=4, padx=5, pady=8, sticky=W)

Label(form_frame, text="Date of Birth", **label_opts).grid(row=3, column=0, padx=10, pady=8, sticky=E)

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
month_var = StringVar(value="May")
month_cb = ttk.Combobox(form_frame, textvariable=month_var, values=months, width=10, state="readonly")
month_cb.grid(row=3, column=1, padx=5, pady=8, sticky=W)

days = [str(i) for i in range(1, 32)]
day_var = StringVar(value="5")
day_cb = ttk.Combobox(form_frame, textvariable=day_var, values=days, width=4, state="readonly")
day_cb.grid(row=3, column=2, padx=5, pady=8, sticky=W)

years = [str(i) for i in range(1950, 2025)]
year_var = StringVar(value="1985")
year_cb = ttk.Combobox(form_frame, textvariable=year_var, values=years, width=6, state="readonly")
year_cb.grid(row=3, column=3, padx=5, pady=8, sticky=W)

Label(form_frame, text="Gender", **label_opts).grid(row=4, column=0, padx=10, pady=8, sticky=E)
gender_frame = Frame(form_frame, bg="#2b2d42")
gender_frame.grid(row=4, column=1, columnspan=4, padx=5, pady=8, sticky=W)
gender_var = IntVar(value=1)
Radiobutton(gender_frame, text="Male", variable=gender_var, value=1,
            bg="#2b2d42", fg="white", selectcolor="#2b2d42", font=("Arial", 10)).pack(side=LEFT)
Radiobutton(gender_frame, text="Female", variable=gender_var, value=2,
            bg="#2b2d42", fg="white", selectcolor="#2b2d42", font=("Arial", 10)).pack(side=LEFT, padx=5)

Label(form_frame, text="Country", **label_opts).grid(row=5, column=0, padx=10, pady=8, sticky=E)
countries = ["USA", "Canada", "UK", "Germany", "France", "Australia", "Japan", "Other"]
country_var = StringVar(value="USA")
country_cb = ttk.Combobox(form_frame, textvariable=country_var, values=countries, width=33, state="readonly")
country_cb.grid(row=5, column=1, columnspan=4, padx=5, pady=8, sticky=W)

Label(form_frame, text="E-mail", **label_opts).grid(row=6, column=0, padx=10, pady=8, sticky=E)
email_entry = Entry(form_frame, width=35, **entry_opts)
email_entry.insert(0, "Enter E-mail......")
email_entry.grid(row=6, column=1, columnspan=4, padx=5, pady=8, sticky=W)

Label(form_frame, text="Phone", **label_opts).grid(row=7, column=0, padx=10, pady=8, sticky=E)
phone_entry = Entry(form_frame, width=35, **entry_opts)
phone_entry.insert(0, "Enter Phone......")
phone_entry.grid(row=7, column=1, columnspan=4, padx=5, pady=8, sticky=W)

Label(form_frame, text="Password", **label_opts).grid(row=8, column=0, padx=10, pady=8, sticky=E)
password_entry = Entry(form_frame, width=35, show="", **entry_opts)
password_entry.grid(row=8, column=1, columnspan=4, padx=5, pady=8, sticky=W)

Label(form_frame, text="Confirm Password", **label_opts).grid(row=9, column=0, padx=10, pady=8, sticky=E)
confirm_entry = Entry(form_frame, width=35, show="", **entry_opts)
confirm_entry.grid(row=9, column=1, columnspan=4, padx=5, pady=8, sticky=W)

agree_frame = Frame(form_frame, bg="#2b2d42")
agree_frame.grid(row=10, column=0, columnspan=5, pady=8, padx=10, sticky=E)
agree_var = IntVar()
Checkbutton(agree_frame, text="I agree to the Terms of Use", variable=agree_var,
            bg="#2b2d42", fg="white", selectcolor="#2b2d42",
            font=("Arial", 10)).pack(side=LEFT)

footer = Frame(root, bg="#f0a500", height=50)
footer.pack(fill=X, side=BOTTOM)
footer.pack_propagate(False)

btn_frame = Frame(footer, bg="#f0a500")
btn_frame.pack(side=RIGHT, padx=10, pady=8)

submit_btn = Button(btn_frame, text="submit", bg="#4caf50", fg="white",
                    font=("Arial", 10, "bold"), bd=0, padx=10, pady=4)
submit_btn.pack(side=LEFT, padx=5)

cancel_btn = Button(btn_frame, text="Cancel", bg="#e74c3c", fg="white",
                    font=("Arial", 10, "bold"), bd=0, padx=10, pady=4)
cancel_btn.pack(side=LEFT, padx=5)

root.mainloop()
