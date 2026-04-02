import tkinter as tk

window = tk.Tk()
window.title("Любимый цвет")
window.geometry("400x250")

radiobutton_frame = tk.LabelFrame(window, text="Любимый цвет", font=("Arial", 12, "bold"),
    relief="solid",bd = 2, bg = 'light green', fg = 'black')
radiobutton_frame.pack(padx=10, pady=10, fill="x")
color_var = tk.StringVar(value="Красный")

def show_color():
    result_label.config(text=f"Ваш любимый цвет: {color_var.get()}")
tk.Radiobutton(radiobutton_frame, text="Красный", variable=color_var, value="Красный",
    font=("Arial", 11), bg = 'light pink', command=show_color).pack(anchor="w", padx=20)
tk.Radiobutton(radiobutton_frame, text="Синий", variable=color_var, value="Синий",
    font=("Arial", 11), bg = 'light pink',  command=show_color).pack(anchor="w", padx=20)
tk.Radiobutton(radiobutton_frame, text="Зеленый", variable=color_var, value="Зеленый",
    font=("Arial", 11), bg = 'light pink', command=show_color).pack(anchor="w", padx=20)
tk.Radiobutton(radiobutton_frame, text="Желтый", variable=color_var, value="Желтый",
    font=("Arial", 11), bg = 'light pink',  command=show_color).pack(anchor="w", padx=20)
result_label = tk.Label(window, text="Выберите цвет", font=("Arial", 11))
result_label.pack(pady=10)

checkbutton_frame = tk.LabelFrame(window, text="Любимые занятия", font=("Arial", 12, "bold"),
    relief="solid", bd=2)
checkbutton_frame.pack(padx=10, pady=10, fill="x")

sport_var = tk.BooleanVar()
music_var = tk.BooleanVar()
read_var = tk.BooleanVar()
games_var = tk.BooleanVar()

label = tk.Label(checkbutton_frame, text="Выберите занятия", font=("Arial", 14))
label.pack(pady=10)

def show_hobbies():
    hobbies = []
    if sport_var.get():
        hobbies.append("спорт")
    if music_var.get():
        hobbies.append("музыка")
    if read_var.get():
        hobbies.append("чтение")
    if games_var.get():
        hobbies.append("игры")
    if hobbies:
        label.config(text="Любимые занятия: " + ", ".join(hobbies))
    else:
        label.config(text="Выберите занятия")

tk.Checkbutton(checkbutton_frame, text="Спорт", variable=sport_var, command=show_hobbies, font=("Arial", 12)).pack(anchor="w", padx=20)
tk.Checkbutton(checkbutton_frame, text="Музыка", variable=music_var, command=show_hobbies, font=("Arial", 12)).pack(anchor="w", padx=20)
tk.Checkbutton(checkbutton_frame, text="Чтение", variable=read_var, command=show_hobbies, font=("Arial", 12)).pack(anchor="w", padx=20)
tk.Checkbutton(checkbutton_frame, text="Игры", variable=games_var, command=show_hobbies, font=("Arial", 12)).pack(anchor="w", padx=20)
#
listbox_frame = tk.LabelFrame(window, text="3. Listbox - Список для выбора элементов", font=("Arial", 12, "bold"), relief="solid", bd=2)
listbox_frame.pack(padx=10, pady=10, fill="x")

films = ["Титаник", "Аватар", "Человек Паук", "Ужасающий", "Гарри Поттер", "Крик"]
film_listbox = tk.Listbox(listbox_frame, height=6, font=("Arial", 11))

for film in films:
    film_listbox.insert(tk.END, film)
film_listbox.pack(padx=20, pady=10)
end_frame = tk.LabelFrame(window, text="Мои предпочтения", font=("Arial", 12, "bold"), relief="solid",bd=2)
end_frame.pack(padx=10, pady=10, fill="x")

result_label1 = tk.Label(window, text="", font=("Arial", 12), justify="left")
result_label1.pack(pady=10)

def show_preferences():
    color = color_var.get()
    hobbies = ""
    if sport_var.get():
        hobbies += "Спорт, "
    if music_var.get():
        hobbies += "Музыка, "
    if read_var.get():
        hobbies += "Чтение, "
    if games_var.get():
        hobbies += "Игры, "
    if hobbies != "":
        hobbies = hobbies[:-2]  # убираем последнюю запятую и пробел
    else:
        hobbies = "Нет"

    if film_listbox.curselection():
        film = film_listbox.get(film_listbox.curselection())
    else:
        film = "Не выбран"
    result_label1.config(text="Любимый цвет: " + color +
                             "\nЛюбимые занятия: " + hobbies +
                             "\nЛюбимый фильм: " + film)

tk.Button(window, text="Показать мои предпочтения", command=show_preferences).pack(pady=20)

window.mainloop()