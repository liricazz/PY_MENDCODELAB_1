import tkinter as tk
import pandas as pd

COLORS = {
    'bg_primary': '#1a1a2e',
    'bg_secondary': '#16213e',
    'accent_1': '#e94560',
    'accent_2': '#0f3460',
    'accent_3': '#f5a623',
    'accent_4': '#20bf6b',
    'text_light': '#e0e0e0',
    'text_dark': '#0f0f1a',
    'button_hover': '#c73e58'
}

table = None

def load_csv():
    global table
    try:
        table = pd.read_csv("students.csv")
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Таблица успешно загружена!\n")
        result.insert(tk.END, f"Размер: {table.shape[0]} строк, {table.shape[1]} столбцов\n")
        result.insert(tk.END, f"Столбцы: {', '.join(table.columns)}")
    except FileNotFoundError:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Ошибка: файл 'students.csv' не найден!\n")
        result.insert(tk.END, "Убедитесь, что файл находится в той же папке, что и программа.")
    except Exception as e:
        result.delete("1.0", tk.END)
        result.insert(tk.END, f"Ошибка при загрузке: {str(e)}")

def show_table():
    if table is not None:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Полная таблица:\n\n")
        result.insert(tk.END, table.to_string())
    else:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Сначала загрузите таблицу (кнопка 'Загрузить таблицу')")

def show_head():
    if table is not None:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Первые 5 строк:\n\n")
        result.insert(tk.END, table.head().to_string())
    else:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Сначала загрузите таблицу (кнопка 'Загрузить таблицу')")

def show_mean():
    if table is not None:
        if "Возраст" in table.columns:
            value = table["Возраст"].mean()
            result.delete("1.0", tk.END)
            result.insert(tk.END, f"Средний возраст студентов:\n\n{value:.2f} лет")
        else:
            result.delete("1.0", tk.END)
            result.insert(tk.END, "Столбец 'Возраст' не найден в таблице!")
    else:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Сначала загрузите таблицу (кнопка 'Загрузить таблицу')")

def show_max():
    if table is not None:
        if "Возраст" in table.columns:
            value = table["Возраст"].max()
            result.delete("1.0", tk.END)
            result.insert(tk.END, f"Максимальный возраст студентов:\n\n{value:.0f} лет")
        else:
            result.delete("1.0", tk.END)
            result.insert(tk.END, "Столбец 'Возраст' не найден в таблице!")
    else:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Сначала загрузите таблицу (кнопка 'Загрузить таблицу')")

def show_min():
    if table is not None:
        if "Возраст" in table.columns:
            value = table["Возраст"].min()
            result.delete("1.0", tk.END)
            result.insert(tk.END, f"Минимальный возраст студентов:\n\n{value:.0f} лет")
        else:
            result.delete("1.0", tk.END)
            result.insert(tk.END, "Столбец 'Возраст' не найден в таблице!")
    else:
        result.delete("1.0", tk.END)
        result.insert(tk.END, "Сначала загрузите таблицу (кнопка 'Загрузить таблицу')")

window = tk.Tk()
window.title("Анализ таблицы pandas")
window.geometry("800x600")
window.configure(bg=COLORS['bg_primary'])

title = tk.Label(
    window,
    text="Анализ данных студентов",
    font=("Montserrat", 20, "bold"),
    fg=COLORS['text_light'],
    bg=COLORS['bg_primary']
)
title.pack(pady=15)

line = tk.Frame(window, bg=COLORS['accent_1'], height=2)
line.pack(fill='x', padx=50, pady=(0, 15))

frame = tk.Frame(window, bg=COLORS['bg_primary'])
frame.pack(pady=10)

button_style = {
    'font': ('Montserrat', 10),
    'fg': COLORS['text_light'],
    'activeforeground': 'white',
    'relief': 'flat',
    'padx': 15,
    'pady': 8,
    'cursor': 'hand2'
}

# Ряд 1
btn_load = tk.Button(frame, text="Загрузить таблицу", command=load_csv,
                     bg=COLORS['accent_2'], activebackground=COLORS['accent_1'], **button_style)
btn_load.grid(row=0, column=0, padx=5, pady=5)

btn_show = tk.Button(frame, text="Показать таблицу", command=show_table,
                     bg=COLORS['accent_2'], activebackground=COLORS['accent_1'], **button_style)
btn_show.grid(row=0, column=1, padx=5, pady=5)

btn_head = tk.Button(frame, text="Первые 5 строк", command=show_head,
                     bg=COLORS['accent_2'], activebackground=COLORS['accent_1'], **button_style)
btn_head.grid(row=0, column=2, padx=5, pady=5)

btn_mean = tk.Button(frame, text="Среднее (возраст)", command=show_mean,
                     bg=COLORS['accent_3'], activebackground=COLORS['accent_1'], **button_style)
btn_mean.grid(row=1, column=0, padx=5, pady=5)

btn_max = tk.Button(frame, text="Максимум (возраст)", command=show_max,
                    bg=COLORS['accent_1'], activebackground=COLORS['accent_2'], **button_style)
btn_max.grid(row=1, column=1, padx=5, pady=5)

btn_min = tk.Button(frame, text="Минимум (возраст)", command=show_min,
                    bg=COLORS['accent_4'], activebackground=COLORS['accent_1'], **button_style)
btn_min.grid(row=1, column=2, padx=5, pady=5)

result_frame = tk.Frame(window, bg=COLORS['bg_secondary'])
result_frame.pack(fill='both', expand=True, padx=20, pady=15)

result_label = tk.Label(
    result_frame,
    text="Результат:",
    font=("Montserrat", 11, "bold"),
    fg=COLORS['text_light'],
    bg=COLORS['bg_secondary']
)
result_label.pack(anchor='w', pady=(5, 0))

result = tk.Text(
    result_frame,
    width=80,
    height=20,
    font=("Courier New", 10),
    bg=COLORS['text_dark'],
    fg=COLORS['text_light'],
    insertbackground=COLORS['text_light'],
    relief='flat',
    wrap=tk.WORD
)
result.pack(fill='both', expand=True, pady=(5, 10))

author_label = tk.Label(
    window,
    text="Марта Ш-13 | ПИШ ХИМ РХТУ",
    font=("Montserrat", 9),
    fg=COLORS['accent_2'],
    bg=COLORS['bg_primary']
)
author_label.pack(pady=(0, 10))

window.mainloop()