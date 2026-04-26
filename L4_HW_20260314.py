import tkinter as tk
from tkinter import messagebox

COLORS = {
    'bg_primary': '#1a1a2e',
    'bg_secondary': '#16213e',
    'accent_1': '#e94560',
    'accent_2': '#0f3460',
    'text_light': '#e0e0e0',
    'text_accent': '#f5a623',
    'highlight': '#20bf6b'
}

def clear_message():
    label.config(text="", font=("Montserrat", 18))

def exit_programm():
    answer = messagebox.askyesno("Выход", "Хотите закрыть программу?")
    if answer:
        window.destroy()

def info():
    messagebox.showinfo("Информация", "Информация показана на экране")
    label.config(text="Показано информационное сообщение", font=("Montserrat", 18), fg=COLORS['highlight'])

def warning():
    messagebox.showwarning("Предупреждение", "Предупреждение показано на экране")
    label.config(text="Будьте внимательны", font=("Montserrat", 18), fg=COLORS['text_accent'])

def error():
    messagebox.showerror("Ошибка", "Ошибка показана на экране")
    label.config(text="Произошла ошибка (на самом деле всё хорошо)", font=("Montserrat", 14), fg=COLORS['accent_1'])

def about():
    messagebox.showinfo("О программе", "Данная программа выводит сообщения в зависимости от выбранной опции в меню.")

def author():
    messagebox.showinfo("Об авторе", "✧ Марта, Ш-13 ПИШ ХИМ РХТУ ✧")

window = tk.Tk()
window.title("Центр сообщений")
window.configure(bg=COLORS['bg_primary'])
window.geometry("550x450")

window.option_add('*tearOff', False)
window.option_add('*Menu.font', ('Montserrat', 10))
window.option_add('*Menu.background', COLORS['bg_secondary'])
window.option_add('*Menu.foreground', COLORS['text_light'])
window.option_add('*Menu.activeBackground', COLORS['accent_2'])
window.option_add('*Menu.activeForeground', COLORS['accent_1'])

label = tk.Label(
    window,
    text="Добро пожаловать в центр сообщений!",
    font=("Montserrat", 16, "bold"),
    fg=COLORS['text_light'],
    bg=COLORS['bg_primary'],
    wraplength=500
)
label.pack(pady=30, padx=20)

decoration = tk.Frame(window, bg=COLORS['accent_1'], height=2)
decoration.pack(fill='x', padx=50, pady=10)

main_menu = tk.Menu(window, bg=COLORS['bg_secondary'], fg=COLORS['text_light'], font=("Montserrat", 10))
window.config(menu=main_menu)

file_menu = tk.Menu(main_menu, tearoff=0, bg=COLORS['bg_secondary'], fg=COLORS['text_light'], font=("Montserrat", 10))
main_menu.add_cascade(label="📁 Файл", menu=file_menu)

file_menu.add_command(label="Очистить сообщение", command=clear_message)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_programm)

messages_menu = tk.Menu(main_menu, tearoff=0, bg=COLORS['bg_secondary'], fg=COLORS['text_light'], font=("Montserrat", 10))
main_menu.add_cascade(label="Сообщения", menu=messages_menu)

messages_menu.add_command(label="ℹИнформация", command=info)
messages_menu.add_command(label="⚠Предупреждение", command=warning)
messages_menu.add_command(label="Ошибка", command=error)

reference_menu = tk.Menu(main_menu, tearoff=0, bg=COLORS['bg_secondary'], fg=COLORS['text_light'], font=("Montserrat", 10))
main_menu.add_cascade(label="Справка", menu=reference_menu)

reference_menu.add_command(label="О программе", command=about)
reference_menu.add_command(label="Автор: Марта К. Ш-13 ПИШ ХИМ РХТУ", command=author)

window.mainloop()