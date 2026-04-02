import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Центр сообщений")
window.geometry("500x400")
window.configure(bg="light pink")

label = tk.Label(window, text="Добро пожаловать в Центр сообщений!", font=("Arial", 16), bg="lightblue")
label.pack(pady=10)


def clear_message():
    label.config(text="Сообщение очищено")


def exit_app():
    answer = messagebox.askyesno("Выход", "Хотите закрыть программу?")
    if answer:
        window.destroy()


menubar = tk.Menu(window)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Очистить сообщение", command=clear_message)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)

menubar.add_cascade(label="Файл", menu=file_menu)


def show_info():
    messagebox.showinfo("Информация", "Всё работает отлично!")
    label.config(text="Показано информационное сообщение")


def show_warning():
    messagebox.showwarning("Предупреждение", "Будьте осторожны и внимательны!")
    label.config(text="Будьте внимательны!")


def show_error():
    messagebox.showerror("Ошибка", "Произошла ошибка, но это просто демонстрация.")
    label.config(text="Произошла ошибка (на самом деле всё хорошо)")


msg_menu = tk.Menu(menubar, tearoff=0)
msg_menu.add_command(label="Информация", command=show_info)
msg_menu.add_command(label="Предупреждение", command=show_warning)
msg_menu.add_command(label="Ошибка", command=show_error)
menubar.add_cascade(label="Сообщения", menu=msg_menu)


def about_program():
    messagebox.showinfo("О программе", "Эта программа показывает работу меню и диалоговых окон.")


def about_author():
    messagebox.showinfo("Автор", "Имя: Иван Иванов, Класс: 10А, Школа: Школа №1")


help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="О программе", command=about_program)
help_menu.add_command(label="Автор", command=about_author)
menubar.add_cascade(label="Справка", menu=help_menu)
window.config(menu=menubar)
window.mainloop()
