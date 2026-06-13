from tkinter import *

root = Tk()
root.title("Sign Up")
root.geometry("400x500")
root.configure(bg="navy")

Label(text="Sign Up", font=("Arial", 16), bg="navy", fg="yellow").grid(row=0, column=0, columnspan=2, pady=10)

Label(text="First Name", bg="navy", fg="yellow").grid(row=1, column=0, sticky="e")
Entry().grid(row=1, column=1, padx=5, pady=2)

Label(text="Last Name", bg="navy", fg="yellow").grid(row=2, column=0, sticky="e")
Entry().grid(row=2, column=1, padx=5, pady=2)

Label(text="Screen Name", bg="navy", fg="yellow").grid(row=3, column=0, sticky="e")
Entry().grid(row=3, column=1, padx=5, pady=2)

Label(text="Date of Birth", bg="navy", fg="yellow").grid(row=4, column=0, sticky="e")
frame_dob = Frame(bg="navy")
frame_dob.grid(row=4, column=1, sticky="w")
month = StringVar()
month.set("May")
OptionMenu(frame_dob, month, "January", "February", "March", "April", "May", "June", "July", "August",
           "September", "October", "November", "December").pack(side="left")
day = StringVar()
day.set("5")
OptionMenu(frame_dob, day, *[str(i) for i in range(1, 32)]).pack(side="left")
year = StringVar()
year.set("1985")
OptionMenu(frame_dob, year, *[str(i) for i in range(1900, 2026)]).pack(side="left")

Label(text="Gender", bg="navy", fg="yellow").grid(row=5, column=0, sticky="e")
frame_gender = Frame(bg="navy")
frame_gender.grid(row=5, column=1, sticky="w")
gender_var = StringVar()
Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male", bg="navy", fg="yellow",
            selectcolor="navy").pack(side="left")
Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female", bg="navy",
            fg="yellow", selectcolor="navy").pack(side="left")

Label(text="Country", bg="navy", fg="yellow").grid(row=6, column=0, sticky="e")
country_var = StringVar()
country_var.set("USA")
countries = ["USA", "Canada", "UK", "Germany", "France", "Russia", "China", "Japan", "India", "Brazil", "Australia"]
OptionMenu(root, country_var, *countries).grid(row=6, column=1, sticky="w", padx=5, pady=2)

Label(text="E-mail", bg="navy", fg="yellow").grid(row=7, column=0, sticky="e")
Entry().grid(row=7, column=1, padx=5, pady=2)

Label(text="Phone", bg="navy", fg="yellow").grid(row=8, column=0, sticky="e")
Entry().grid(row=8, column=1, padx=5, pady=2)

Label(text="Password", bg="navy", fg="yellow").grid(row=9, column=0, sticky="e")
Entry(show="*").grid(row=9, column=1, padx=5, pady=2)

Label(text="Confirm Password", bg="navy", fg="yellow").grid(row=10, column=0, sticky="e")
Entry(show="*").grid(row=10, column=1, padx=5, pady=2)

agree_var = IntVar()
Checkbutton(text="I agree to the Terms of Use", variable=agree_var, bg="navy",
            fg="yellow", selectcolor="navy").grid(row=11, column=0, columnspan=2, pady=5)

frame_buttons = Frame(bg="navy")
frame_buttons.grid(row=12, column=0, columnspan=2, pady=10)
Button(frame_buttons, text="Submit", bg="green").pack(side="left", padx=5)
Button(frame_buttons, text="Cancel", bg="red").pack(side="left", padx=5)

root.mainloop()
