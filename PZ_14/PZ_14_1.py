from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sign Up")
root.geometry("560x620")
root.configure(bg="#1e2233")
root.resizable(False, False)

title_frame = Frame(root, bg="#e6a817", height=40)
title_frame.pack(fill=X)
title_frame.pack_propagate(False)

Label(title_frame, text="Sign Up", bg="#e6a817", fg="white", font="Arial 13 bold").pack(side=LEFT, padx=10, pady=8)

main_frame = Frame(root, bg="#1e2233")
main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

label_cfg = {"bg": "#1e2233", "fg": "#e6a817", "font": "Arial 10", "anchor": "e", "width": 15}
entry_cfg = {"font": "Arial 10", "bd": 1, "relief": SOLID}

def add_row(parent, row, label_text, widget):
    Label(parent, text=label_text, **label_cfg).grid(row=row, column=0, padx=(0, 10), pady=6, sticky=E)
    widget.grid(row=row, column=1, pady=6, sticky=EW)

main_frame.columnconfigure(1, weight=1)

entry_first = Entry(main_frame, **entry_cfg)
entry_first.insert(0, "Enter First Name...")
add_row(main_frame, 0, "First Name", entry_first)

entry_last = Entry(main_frame, **entry_cfg)
entry_last.insert(0, "Enter Last Name...")
add_row(main_frame, 1, "Last Name", entry_last)

entry_screen = Entry(main_frame, **entry_cfg)
entry_screen.insert(0, "Enter Screen Name...")
add_row(main_frame, 2, "Screen Name", entry_screen)

Label(main_frame, text="Date of Birth", **label_cfg).grid(row=3, column=0, padx=(0, 10), pady=6, sticky=E)

dob_frame = Frame(main_frame, bg="#1e2233")
dob_frame.grid(row=3, column=1, pady=6, sticky=W)

months = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]
month_var = StringVar(value="May")
month_cb = ttk.Combobox(dob_frame, textvariable=month_var, values=months, width=10, state="readonly")
month_cb.pack(side=LEFT, padx=(0, 4))

days = [str(i) for i in range(1, 32)]
day_var = StringVar(value="5")
day_cb = ttk.Combobox(dob_frame, textvariable=day_var, values=days, width=4, state="readonly")
day_cb.pack(side=LEFT, padx=(0, 4))

years = [str(i) for i in range(1950, 2010)]
year_var = StringVar(value="1985")
year_cb = ttk.Combobox(dob_frame, textvariable=year_var, values=years, width=6, state="readonly")
year_cb.pack(side=LEFT)

Label(main_frame, text="Gender", **label_cfg).grid(row=4, column=0, padx=(0, 10), pady=6, sticky=E)

gender_frame = Frame(main_frame, bg="#1e2233")
gender_frame.grid(row=4, column=1, pady=6, sticky=W)

gender_var = StringVar(value="Male")
Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#1e2233", fg="white", selectcolor="#1e2233", font="Arial 10").pack(side=LEFT)
Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#1e2233", fg="white", selectcolor="#1e2233", font="Arial 10").pack(side=LEFT)

Label(main_frame, text="Country", **label_cfg).grid(row=5, column=0, padx=(0, 10), pady=6, sticky=E)

countries = ["USA", "UK", "Canada", "Germany", "France", "Australia", "Other"]
country_var = StringVar(value="USA")
country_cb = ttk.Combobox(main_frame, textvariable=country_var, values=countries, state="readonly", font="Arial 10")
country_cb.grid(row=5, column=1, pady=6, sticky=EW)

entry_email = Entry(main_frame, **entry_cfg)
entry_email.insert(0, "Enter E-mail......")
add_row(main_frame, 6, "E-mail", entry_email)

entry_phone = Entry(main_frame, **entry_cfg)
entry_phone.insert(0, "Enter Phone......")
add_row(main_frame, 7, "Phone", entry_phone)

entry_pass = Entry(main_frame, show="*", **entry_cfg)
add_row(main_frame, 8, "Password", entry_pass)

entry_confirm = Entry(main_frame, show="*", **entry_cfg)
add_row(main_frame, 9, "Confirm Password", entry_confirm)

agree_frame = Frame(main_frame, bg="#1e2233")
agree_frame.grid(row=10, column=0, columnspan=2, pady=6)

agree_var = IntVar()
Checkbutton(agree_frame, text="I agree to the Terms of Use", variable=agree_var, bg="#1e2233", fg="white", selectcolor="#1e2233", font="Arial 10").pack()

bottom_frame = Frame(root, bg="#e6a817", height=50)
bottom_frame.pack(fill=X, side=BOTTOM)
bottom_frame.pack_propagate(False)

Button(bottom_frame, text="submit", bg="#4cae4c", fg="white", font="Arial 10 bold", bd=0, padx=10).pack(side=RIGHT, padx=(0, 5), pady=10)
Button(bottom_frame, text="Cancel", bg="#d9534f", fg="white", font="Arial 10 bold", bd=0, padx=10).pack(side=RIGHT, padx=5, pady=10)

root.mainloop()
