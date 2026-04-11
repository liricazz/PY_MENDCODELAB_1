import tkinter as tk

bgr = "#6D373F"
frg = "#DEDEDE"
fnt = "Helvetica"
sett = "bold"

window = tk.Tk()
window.title("Переводчик баллов РХТУ")
window.geometry("650x500")
window.configure(bg = bgr)


def entr_trigg():
    entryS = entry.get();
    if(len(entryS) == 0 or len(entryS.strip()) == 0):
        label2.config(text="Ошибка: введите число", font=(fnt, 18, sett), fg=frg, bg=bgr)
    elif (float(entryS) != float(int(float(entryS)))):
        label2.config(text="Ошибка: нужно целое число", font=(fnt, 18, sett), fg=frg, bg=bgr)
    elif (int(entryS) < 0 or int(entryS) > 100):
        label2.config(text="Ошибка: число должно быть от 0 до 100", font=(fnt, 18, sett), fg=frg, bg=bgr)
    else:
        if (int(entryS) <= 49):
            label2.config(text="Ваша оценка: 2. Незачет.", font=(fnt, 18, sett), bg="#FFB3B3", fg="#C66B5D")
        elif (int(entryS) >= 50 and int(entryS) <= 69):
            label2.config(text="Ваша оценка: 3. Нужно подтянуть.", font=(fnt, 18, sett), bg="#FFD9A1", fg="#C79100")
        elif (int(entryS) >= 70 and int(entryS) <= 84):
            label2.config(text="Ваша оценка: 4. Хорошо!", font=(fnt, 18, sett), bg="#D8E9D0", fg="#558B2F")
        elif (int(entryS) >= 85):
            label2.config(text="Ваша оценка: 5. Отлично!", font=(fnt, 18, sett), bg="#B2C2AD", fg="#4F6D45")

def clear_trigg():
    entry.delete(0, tk.END)
    label2.config(text="...", font=(fnt, 18, sett), fg=frg, bg=bgr)

label1 = tk.Label(window, text="Введите балл (0 - 100): ", font=(fnt, 18, sett), bg=bgr, fg=frg)
label1.pack(pady = 20)

entry = tk.Entry(window, width=10)
entry.pack(pady = 30)

button1 = tk.Button(window, text="Показать оценку", command=entr_trigg, font=(fnt, 16, sett), fg=frg, bg="#D86A33", relief="flat")
button1.pack(pady = 10)

button2 = tk.Button(window, text="Очистить", command=clear_trigg, font=(fnt, 16, sett), fg=frg, bg="#D86A33", relief="flat")
button2.pack(pady = 10)

label2 = tk.Label(window, text="...", font=(fnt, 18, sett), bg=bgr, fg=frg)
label2.pack(pady = 20)


window.mainloop()
