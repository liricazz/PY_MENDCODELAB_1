import tkinter as tk

window = tk.Tk()
window.title("Урок 5. Калькулятор")
window.geometry("500x450")
window.configure(bg="lavender")

title_label = tk.Label(
   window,
   text="Мой калькулятор",
   font=("Montserrat", 18, "bold"),
   bg="lavender",
   fg="darkblue"
)
title_label.pack(pady=15)


first_label = tk.Label(window, text="Введите первое число:", font=("Montserrat", 12), bg="lavender")
first_label.pack()

first_entry = tk.Entry(window, width=25, font=("Montserrat", 12))
first_entry.pack(pady=5)


second_label = tk.Label(window, text="Введите второе число:", font=("Montserrat", 12), bg="lavender")
second_label.pack()

second_entry = tk.Entry(window, width=25, font=("Montserrat", 12))
second_entry.pack(pady=10)


result_label = tk.Label(
   window,
   text="Результат: ...",
   font=("Montserrat", 16, "bold"),
   bg="white",
   fg="black",
   width=25,
   height=2,
   relief="solid",
   bd=2
)
result_label.pack(pady=10)

def add_numbers_1():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())
        res = num1 + num2
        result_label.config(text=f"Результат: {res}")
    except:
        result_label.config(text=f'Ошибка: введите числа заново.', fg="red")

add_button = tk.Button(
    window,
    text='Сложить',
    font=("Montserrat", 12, "bold"),
    bg='lightgreen',
    command=add_numbers_1)

add_button.pack()

def add_numbers_2():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())
        res = num1 - num2
        result_label.config(text=f'Результат: {res}')
    except:
        result_label.config(text=f'Ошибка: введите числа заново', fg="red")

add_button = tk.Button(
    window,
    text='Вычесть',
    font=("Montserrat", 12, "bold"),
    bg='lightgreen',
    command=add_numbers_2)

add_button.pack()

def add_numbers_3():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())
        if num2 != 0:
            res = num1 / num2
            result_label.config(text=f'Результат: {res}')
        else:
            result_label.config(text=f'На ноль делить нельзя!', fg="red")
    except:
        result_label.config(text=f'Ошибка: введите числа заново', fg="red")

add_button = tk.Button(
    window,
    text='Разделить',
    font=("Montserrat", 12, "bold"),
    bg='lightgreen',
    command=add_numbers_3)

add_button.pack()

def add_numbers_4():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())
        res = num1 * num2
        result_label.config(text=f'Результат: {res}')
    except:
        result_label.config(text=f'Ошибка: введите числа заново', fg="red")

add_button = tk.Button(
    window,
    text='Умножить',
    font=("Montserrat", 12, "bold"),
    bg='lightgreen',
    command=add_numbers_4)

add_button.pack()


window.mainloop()
