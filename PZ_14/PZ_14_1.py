from tkinter import *

root = Tk()
root.title("Sign Up")
root.geometry("400x500")

Label(root, text="Sign Up", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

Label(root, text="First Name").grid(row=1, column=0, sticky="e")
Entry(root).grid(row=1, column=1, padx=5, pady=2)

Label(root, text="Last Name").grid(row=2, column=0, sticky="e")
Entry(root).grid(row=2, column=1, padx=5, pady=2)

Label(root, text="Screen Name").grid(row=3, column=0, sticky="e")
Entry(root).grid(row=3, column=1, padx=5, pady=2)

Label(root, text="Date of Birth").grid(row=4, column=0, sticky="e")
frame_dob = Frame(root)
frame_dob.grid(row=4, column=1, sticky="w")
month = StringVar(root)
month.set("May")
OptionMenu(frame_dob, month, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December").pack(side="left")
day = StringVar(root)
day.set("5")
OptionMenu(frame_dob, day, *[str(i) for i in range(1,32)]).pack(side="left")
year = StringVar(root)
year.set("1985")
OptionMenu(frame_dob, year, *[str(i) for i in range(1900,2026)]).pack(side="left")

Label(root, text="Gender").grid(row=5, column=0, sticky="e")
frame_gender = Frame(root)
frame_gender.grid(row=5, column=1, sticky="w")
gender_var = StringVar()
Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male").pack(side="left")
Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female").pack(side="left")

Label(root, text="Country").grid(row=6, column=0, sticky="e")
Entry(root).grid(row=6, column=1, padx=5, pady=2)
Label(root, text="USA").grid(row=6, column=2, sticky="w")

Label(root, text="E-mail").grid(row=7, column=0, sticky="e")
Entry(root).grid(row=7, column=1, padx=5, pady=2)

Label(root, text="Phone").grid(row=8, column=0, sticky="e")
Entry(root).grid(row=8, column=1, padx=5, pady=2)

Label(root, text="Password").grid(row=9, column=0, sticky="e")
Entry(root, show="*").grid(row=9, column=1, padx=5, pady=2)

Label(root, text="Confirm Password").grid(row=10, column=0, sticky="e")
Entry(root, show="*").grid(row=10, column=1, padx=5, pady=2)

agree_var = IntVar()
Checkbutton(root, text="I agree to the Terms of Use", variable=agree_var).grid(row=11, column=0, columnspan=2, pady=5)

frame_buttons = Frame(root)
frame_buttons.grid(row=12, column=0, columnspan=2, pady=10)
Button(frame_buttons, text="submit").pack(side="left", padx=5)
Button(frame_buttons, text="Cancel").pack(side="left", padx=5)

root.mainloop()
