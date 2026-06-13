from tkinter import *
from tkinter import ttk

root = Tk()
root.title("К ПЗ 2")
root.geometry("300x150")


def calculate():
    byt = int(entry.get())
    kilobytes = byt // 1024
    result_label.config(text=f"Килобайт: {kilobytes} КБ")


Label(text="Введите размер файла (байт):").pack(pady=5)

entry = ttk.Entry(width=25)
entry.pack()

ttk.Button(root, text="Вычислить", command=calculate).pack(pady=5)

result_label = Label(text="Килобайт: —")
result_label.pack(pady=5)

root.mainloop()
