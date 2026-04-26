import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

window = tk.Tk()
window.title("Графики по таблице")
window.geometry("800x900")
window.configure(bg=COLORS['bg_primary'])

df = None
canvas = None

def load_file():
    global df
    try:
        df = pd.read_csv("students.csv")
        info_label.config(text=f"Файл загружен. Строк: {len(df)}", fg=COLORS['accent_4'])
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл students.csv не найден")
        info_label.config(text="Ошибка: файл не найден", fg=COLORS['accent_1'])

def show_table():
    if df is None:
        result_label.config(text="Сначала загрузите файл!")
        messagebox.showwarning("Ошибка", "Сначала загрузите файл!")
        return
    result_label.config(text="Первые 10 студентов:\n\n" + str(df.head(10)))

def clear_old_canvas():
    global canvas
    if canvas is not None:
        canvas.get_tk_widget().destroy()
        canvas = None

def plot_line():
    if df is None:
        result_label.config(text="Сначала загрузите файл!")
        messagebox.showwarning("Ошибка", "Сначала загрузите файл!")
        return

    clear_old_canvas()

    fig = plt.figure(figsize=(6, 4), facecolor=COLORS['bg_secondary'])
    plt.plot(df["Имя"], df["Средний_балл"], color=COLORS['accent_1'], marker='o', linewidth=2)

    plt.title("Средний балл", color=COLORS['text_light'], fontsize=12)
    plt.xlabel("Студенты", color=COLORS['text_light'])
    plt.ylabel("Значение", color=COLORS['text_light'])
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45, color=COLORS['text_light'])
    plt.yticks(color=COLORS['text_light'])
    plt.gca().set_facecolor(COLORS['text_dark'])
    plt.tight_layout()

    global canvas
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def plot_bar():
    if df is None:
        result_label.config(text="Сначала загрузите файл!")
        messagebox.showwarning("Ошибка", "Сначала загрузите файл!")
        return

    clear_old_canvas()

    fig = plt.figure(figsize=(6, 4), facecolor=COLORS['bg_secondary'])
    plt.bar(df["Имя"], df["Часы_подготовки"], color=COLORS['accent_4'], alpha=0.8, edgecolor=COLORS['accent_1'])

    plt.title("Часы подготовки", color=COLORS['text_light'], fontsize=12)
    plt.xlabel("Студенты", color=COLORS['text_light'])
    plt.ylabel("Часы подготовки", color=COLORS['text_light'])
    plt.grid(True, alpha=0.3, axis='y')
    plt.xticks(rotation=45, color=COLORS['text_light'])
    plt.yticks(color=COLORS['text_light'])
    plt.gca().set_facecolor(COLORS['text_dark'])
    plt.tight_layout()

    global canvas
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def clear_all():
    global df
    df = None
    info_label.config(text="Нажмите Загрузить файл", fg=COLORS['text_light'])
    result_label.config(text="")
    clear_old_canvas()

header = tk.Label(window, text="Графики по таблице", font=("Montserrat", 18, "bold"), fg=COLORS['text_light'], bg=COLORS['bg_primary'])
header.pack(pady=15)

line = tk.Frame(window, bg=COLORS['accent_1'], height=2)
line.pack(fill='x', padx=50, pady=(0, 15))

button_style = {
    'font': ('Montserrat', 10),
    'width': 25,
    'pady': 8,
    'relief': 'flat',
    'cursor': 'hand2'
}

tk.Button(window, text="Загрузить файл", bg=COLORS['accent_2'], fg=COLORS['text_dark'], activebackground=COLORS['accent_1'], command=load_file, **button_style).pack(pady=6)
tk.Button(window, text="Показать таблицу", bg=COLORS['accent_2'], fg=COLORS['text_dark'], activebackground=COLORS['accent_1'], command=show_table, **button_style).pack(pady=6)
tk.Button(window, text="Линейный график", bg=COLORS['accent_3'], fg=COLORS['text_dark'], activebackground=COLORS['accent_1'], command=plot_line, **button_style).pack(pady=6)
tk.Button(window, text="Столбчатая диаграмма", bg=COLORS['accent_4'], fg=COLORS['text_dark'], activebackground=COLORS['accent_1'], command=plot_bar, **button_style).pack(pady=6)
tk.Button(window, text="Очистить всё", bg=COLORS['accent_1'], fg=COLORS['text_dark'], activebackground=COLORS['accent_2'], command=clear_all, **button_style).pack(pady=12)

info_label = tk.Label(window, text="Нажмите Загрузить файл", font=("Montserrat", 10), fg=COLORS['text_light'], bg=COLORS['bg_primary'])
info_label.pack(pady=8)

result_label = tk.Label(window, text="", font=("Courier New", 9), fg=COLORS['text_light'], bg=COLORS['text_dark'], relief="solid", bd=2, justify="left", height=13, anchor="nw")
result_label.pack(pady=10, padx=30, fill="x")

graph_frame = tk.LabelFrame(window, text="График", font=("Montserrat", 10), fg=COLORS['accent_1'], bg=COLORS['bg_primary'], padx=10, pady=10)
graph_frame.pack(pady=10, padx=30, fill="both", expand=True)

author_label = tk.Label(window, text="Марта Ш-13 | ПИШ ХИМ РХТУ", font=("Montserrat", 9), fg=COLORS['accent_2'], bg=COLORS['bg_primary'])
author_label.pack(pady=(0, 10))

window.mainloop()