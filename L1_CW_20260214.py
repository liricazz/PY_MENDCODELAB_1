import tkinter as tk

window = tk.Tk()

window.title("Моя визитная карточка")
window.geometry("600x500")
window.configure(bg='#2c3e50')


label_name = tk.Label(
    window,
    text="Марта Кондратова",
    font=("Montserrat", 28, "bold"),
    fg="#f39c12",
    bg='#2c3e50'
)
label_name.pack(pady=(40, 10))

label_school = tk.Label(
    window,
    text="🎓 Выпускница IT-класса предпрофессиональной программы",
    font=("Montserrat", 11),
    fg="#ecf0f1",
    bg='#2c3e50'
)
label_school.pack(pady=2)

label_school_name = tk.Label(
    window,
    text="Школа №1420, г. Москва",
    font=("Montserrat", 11, "italic"),
    fg="#bdc3c7",
    bg='#2c3e50'
)
label_school_name.pack(pady=2)

label_hobby_title = tk.Label(
    window,
    text="💡 Любимые предметы и увлечения:",
    font=("Montserrat", 12, "bold"),
    fg="#e67e22",
    bg='#2c3e50'
)
label_hobby_title.pack(pady=(20, 5))

label_hobby = tk.Label(
    window,
    text="Информатика • Математика • Технология",
    font=("Montserrat", 11),
    fg="#ecf0f1",
    bg='#2c3e50',
    relief="solid",
    bd=1,
    padx=10,
    pady=5
)
label_hobby.pack(pady=2)

label_hobby2 = tk.Label(
    window,
    text="Программирование | Ораторское искусство | Бильярд",
    font=("Montserrat", 11),
    fg="#ecf0f1",
    bg='#2c3e50'
)
label_hobby2.pack(pady=2)

label_dream_title = tk.Label(
    window,
    text="✨ Мечта и цель:",
    font=("Montserrat", 12, "bold"),
    fg="#e67e22",
    bg='#2c3e50'
)
label_dream_title.pack(pady=(20, 5))

label_dream = tk.Label(
    window,
    text="Сиять, вопреки всему: даже когда одинок\nдаже когда ослаб\nдаже когда рядом нет кружки кофе :)",
    font=("Montserrat", 10),
    fg="#f39c12",
    bg='#2c3e50',
    justify="left",
    wraplength=500,
    relief="groove",
    bd=2,
    padx=20,
    pady=10
)
label_dream.pack(pady=5)

footer = tk.Label(
    window,
    text="————————————————————",
    font=("Montserrat", 10),
    fg="#7f8c8d",
    bg='#2c3e50'
)
footer.pack(pady=(20, 5))

window.mainloop()