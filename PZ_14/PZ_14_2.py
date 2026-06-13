from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Конвертер размера файла")
root.geometry("300x150")


def calculate():
    try:
        bytes_val = int(entry.get())
        kilobytes = bytes_val // 1024
        result_label.config(text=f"Килобайт: {kilobytes} КБ")
    except ValueError:
        result_label.config(text="Введите целое число!")


def close():
    root.destroy()
    root.quit()


Label(root, text="Введите размер файла (байт):").pack(pady=5)

entry = ttk.Entry(root, width=25)
entry.pack(pady=5)

ttk.Button(root, text="Вычислить", command=calculate).pack(pady=5)

result_label = Label(root, text="Килобайт: —")
result_label.pack(pady=5)

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
