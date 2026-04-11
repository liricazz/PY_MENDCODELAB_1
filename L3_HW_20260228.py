import tkinter as tk

bgr = "#6E635A"
frg = "#DEDEDE"
fnt = "Helvetica"
sett = "bold"

window = tk.Tk()
window.title("Создание героя для приключения")
window.geometry("650x1000")
window.configure(bg=bgr)

label1 = tk.Label(window, text="Введите имя героя:", font=(fnt, 18, sett), bg=bgr, fg=frg)
label1.pack(pady=20)

entry = tk.Entry(window, width=30)
entry.pack(pady=20)

radiobutton_frame = tk.LabelFrame(window, text="Класс героя", font=(fnt, 16, "bold"), relief="solid", bd=2, bg=bgr)
radio_var = tk.StringVar()
tk.Radiobutton(radiobutton_frame, text="Маг", variable=radio_var, value="Маг", font=(fnt, 16, "bold"), bg=bgr,
               fg=frg).pack(anchor="w", padx=20)
tk.Radiobutton(radiobutton_frame, text="Войн", variable=radio_var, value="Войн", font=(fnt, 16, "bold"), bg=bgr,
               fg=frg).pack(anchor="w", padx=20)
tk.Radiobutton(radiobutton_frame, text="Лучник", variable=radio_var, value="Лучник", font=(fnt, 16, "bold"), bg=bgr,
               fg=frg).pack(anchor="w", padx=20)
tk.Radiobutton(radiobutton_frame, text="Разбойник", variable=radio_var, value="Разбойник", font=(fnt, 16, "bold"),
               bg=bgr, fg=frg).pack(anchor="w", padx=20)
radiobutton_frame.pack(padx=20, pady=20, fill="both", expand=True)

checkbutton_frame = tk.LabelFrame(window, text="Способности героя", font=(fnt, 16, "bold"), relief="solid", bd=2,
                                  bg=bgr)
str_var = tk.IntVar()
int_var = tk.IntVar()
speed_var = tk.IntVar()
prot_var = tk.IntVar()

strength = tk.Checkbutton(checkbutton_frame, text="Сила", variable=str_var, font=(fnt, 16, "bold"), bg=bgr, fg=frg)
strength.pack(anchor="w", padx=20)
intellect = tk.Checkbutton(checkbutton_frame, text="Интеллект", variable=int_var, font=(fnt, 16, "bold"), bg=bgr,
                           fg=frg)
intellect.pack(anchor="w", padx=20)
speed = tk.Checkbutton(checkbutton_frame, text="Скорость", variable=speed_var, font=(fnt, 16, "bold"), bg=bgr, fg=frg)
speed.pack(anchor="w", padx=20)
protection = tk.Checkbutton(checkbutton_frame, text="Защита", variable=prot_var, font=(fnt, 16, "bold"), bg=bgr, fg=frg)
protection.pack(anchor="w", padx=20)
checkbutton_frame.pack(padx=20, pady=20, fill="both", expand=True)

weapons = ["Меч", "Посох", "Лук", "Кинжал", "Топор"]
weaponbox_frame = tk.LabelFrame(window, text="Оружие героя", font=(fnt, 16, "bold"), relief="solid", bd=2, bg=bgr)
weapons_listbox = tk.Listbox(weaponbox_frame, font=(fnt, 16, "bold"), bg=bgr, fg=frg, height=5)

for weapon in weapons:
    weapons_listbox.insert(tk.END, weapon)

weapons_listbox.pack(padx=20, pady=20, fill="both", expand=True)
weaponbox_frame.pack(padx=20, pady=20, fill="both", expand=True)

label = tk.Label(window, text="...", font=(fnt, 18, sett), bg=bgr, fg=frg)
label.pack(pady=20)


def clear_trigg():
    entry.delete(0, tk.END)
    label.config(text="...", font=(fnt, 18, sett), fg=frg, bg=bgr)

    radio_var.set("")
    str_var.set(0)
    speed_var.set(0)
    int_var.set(0)
    prot_var.set(0)

    weapons_listbox.selection_clear(0, "end")


def show_person():
    entryS = entry.get();
    if (len(entryS) == 0 or len(entryS.strip()) == 0):
        label.config(text="Ошибка: Введите имя героя", font=(fnt, 18, sett), bg="#FFB3B3", fg="#C66B5D")
        return 0

    if radio_var.get():
        klass = radio_var.get()
    else:
        label.config(text="Ошибка: Выберите класс героя", font=(fnt, 18, sett), bg="#FFB3B3", fg="#C66B5D")
        return 0

    abilities = []
    if str_var.get(): abilities.append("Сила")
    if int_var.get(): abilities.append("Интеллект")
    if speed_var.get(): abilities.append("Скорость")
    if prot_var.get(): abilities.append("Защита")
    if abilities:
        abilities_str = ", ".join(abilities)
    else:
        label.config(text="Ошибка: Выберите хотя бы одну способность", font=(fnt, 18, sett), bg="#FFB3B3", fg="#C66B5D")
        return 0

    selected_indices = weapons_listbox.curselection()
    selected_weapons = [weapons_listbox.get(i) for i in selected_indices]
    if selected_weapons:
        weapons_str = ", ".join(selected_weapons)
    else:
        label.config(text="Ошибка: Выберите оружие", font=(fnt, 18, sett), bg="#FFB3B3", fg="#C66B5D")
        return 0

    final_text = f"Герой создан!\nИмя: {entryS}\n"
    final_text += f"Класс: {klass}\n"
    final_text += f"Способности: {abilities_str}\n"
    final_text += f"Оружие: {weapons_str}"

    label.config(text=final_text, bg="#D8E9D0", fg="#558B2F")


btn_show = tk.Button(window, text="Создать героя",
                     font=(fnt, 14, "bold"), bg=frg, fg="white",
                     command=show_person)
btn_show.pack(pady=5)

btn_clear = tk.Button(window, text="Очистить героя",
                      font=(fnt, 14, "bold"), bg=frg, fg="white",
                      command=clear_trigg)
btn_clear.pack(pady=5)

window.mainloop()
