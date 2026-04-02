import tkinter as tk

window = tk.Tk()

window.title("Напиши предложение")
window.geometry("400x300")

title_label = tk.Label(window, text = "Напиши предложение", font = ("arial", 18), bg = "light blue")
title_label.pack(pady=10)

name_label = tk.Label(window, text="Ваше предложение:")
name_label.pack()

name_entry = tk.Entry(window, width=30, )
name_entry.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 12), fg="violet")
result_label.pack(pady=10)

def show_info():
    word = name_entry.get()
    result_label.config(text=f"Ваше предложение: {word}.")

button = tk.Button(window, text="Показать результат", command=show_info, font=("Arial", 18), bg="light green", fg="black")
button.pack(pady=10)
clear_label = tk.Label(window, text="очистить", font=("Arial", 18), bg = "light blue")

def clear_text():
    word = name_entry.get()
    word = ""
    result_label.config(text="")
    name_entry.delete(0, tk.END)

button = tk.Button(window, text="очистить", command = clear_text, font=("Arial", 18), bg="light green", fg="black", relief="raised")
button.pack(pady=10)

window.mainloop()