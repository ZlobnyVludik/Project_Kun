from tkinter import *

root = Tk()
root.title("Sign Up")
root.geometry("400x500")
root.configure(bg="navy")

root.columnconfigure(0, minsize=130)  # фиксируем ширину колонки с лейблами
root.columnconfigure(1, minsize=220)  # фиксируем ширину колонки с полями

Label(text="Sign Up", font=("Arial", 16), bg="navy", fg="yellow").grid(row=0, column=0, columnspan=2, pady=10)

Label(text="First Name", bg="navy", fg="yellow").grid(row=1, column=0, sticky="e", padx=(0,5))
Entry(root).grid(row=1, column=1, sticky="w", pady=2)

Label(text="Last Name", bg="navy", fg="yellow").grid(row=2, column=0, sticky="e", padx=(0,5))
Entry(root).grid(row=2, column=1, sticky="w", pady=2)

Label(text="Screen Name", bg="navy", fg="yellow").grid(row=3, column=0, sticky="e", padx=(0,5))
Entry(root).grid(row=3, column=1, sticky="w", pady=2)

Label(text="Date of Birth", bg="navy", fg="yellow").grid(row=4, column=0, sticky="e", padx=(0,5))
frame_date = Frame(root, bg="navy")
frame_date.grid(row=4, column=1, sticky="w", pady=2)
month = StringVar(value="May")
OptionMenu(frame_date, month, "January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December").pack(side="left")
day = StringVar(value="5")
OptionMenu(frame_date, day, *[str(i) for i in range(1, 32)]).pack(side="left")
year = StringVar(value="1985")
OptionMenu(frame_date, year, *[str(i) for i in range(1900, 2026)]).pack(side="left")

Label(text="Gender", bg="navy", fg="yellow").grid(row=5, column=0, sticky="e", padx=(0,5))
frame_gender = Frame(root, bg="navy")
frame_gender.grid(row=5, column=1, sticky="w", pady=2)
gender_var = StringVar()
Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male",
            bg="navy", fg="yellow", selectcolor="navy").pack(side="left")
Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female",
            bg="navy", fg="yellow", selectcolor="navy").pack(side="left")

Label(text="Country", bg="navy", fg="yellow").grid(row=6, column=0, sticky="e", padx=(0,5))
country_var = StringVar(value="USA")
countries = ["USA", "Canada", "UK", "Germany", "France", "Russia", "China", "Japan", "India", "Brazil", "Australia"]
OptionMenu(root, country_var, *countries).grid(row=6, column=1, sticky="w", pady=2)

Label(text="E-mail", bg="navy", fg="yellow").grid(row=7, column=0, sticky="e", padx=(0,5))
Entry(root).grid(row=7, column=1, sticky="w", pady=2)

Label(text="Phone", bg="navy", fg="yellow").grid(row=8, column=0, sticky="e", padx=(0,5))
Entry(root).grid(row=8, column=1, sticky="w", pady=2)

Label(text="Password", bg="navy", fg="yellow").grid(row=9, column=0, sticky="e", padx=(0,5))
Entry(root, show="*").grid(row=9, column=1, sticky="w", pady=2)

Label(text="Confirm Password", bg="navy", fg="yellow").grid(row=10, column=0, sticky="e", padx=(0,5))
Entry(root, show="*").grid(row=10, column=1, sticky="w", pady=2)

agree_var = IntVar()
Checkbutton(root, text="I agree to the Terms of Use", variable=agree_var,
            bg="navy", fg="yellow", selectcolor="navy").grid(row=11, column=1, sticky="w", pady=5)

frame_buttons = Frame(root, bg="navy")
frame_buttons.grid(row=12, column=0, columnspan=2, pady=10)
Button(frame_buttons, text="Submit", bg="green").pack(side="left", padx=5)
Button(frame_buttons, text="Cancel", bg="red").pack(side="left", padx=5)

root.mainloop()
