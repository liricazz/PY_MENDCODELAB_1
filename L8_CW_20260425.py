import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class DataAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Анализ данных - Мини-проект")
        self.root.geometry("1200x750")
        self.root.configure(bg='#1a1a2e')

        self.font_family = "Montserrat"

        self.df = None
        self.numeric_columns = []
        self.selected_column = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self.root, bg='#16213e', height=90)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)

        title_label = tk.Label(
            title_frame,
            text="Анализ данных из CSV-файла",
            font=(self.font_family, 22, "bold"),
            bg='#16213e',
            fg='#e94560'
        )
        title_label.pack(pady=(15, 5))

        main_container = tk.Frame(self.root, bg='#1a1a2e')
        main_container.pack(fill='both', expand=True, padx=10, pady=10)

        left_panel = tk.Frame(main_container, bg='#1a1a2e', width=250)
        left_panel.pack(side='left', fill='y', padx=(0, 10))
        left_panel.pack_propagate(False)

        button_style = {
            'font': (self.font_family, 11),
            'width': 20,
            'pady': 8,
            'cursor': 'hand2',
            'relief': 'flat'
        }

        self.load_btn = tk.Button(
            left_panel,
            text="Загрузить файл",
            command=self.load_file,
            bg='#e94560',
            fg='white',
            activebackground='#c73e58',
            activeforeground='white',
            **button_style
        )
        self.load_btn.pack(pady=5)

        self.show_btn = tk.Button(
            left_panel,
            text="Показать таблицу",
            command=self.show_table,
            bg='#533483',
            fg='white',
            activebackground='#3d2668',
            activeforeground='white',
            state='disabled',
            **button_style
        )
        self.show_btn.pack(pady=5)

        tk.Label(
            left_panel,
            text="Выберите столбец:",
            font=(self.font_family, 10),
            bg='#1a1a2e',
            fg='#e94560'
        ).pack(pady=(10, 5))

        self.column_combo = ttk.Combobox(
            left_panel,
            textvariable=self.selected_column,
            state='readonly',
            width=18,
            font=(self.font_family, 10)
        )
        self.column_combo.pack(pady=(0, 10))

        self.analyze_btn = tk.Button(
            left_panel,
            text="Анализ данных",
            command=self.analyze_data,
            bg='#f5a623',
            fg='white',
            activebackground='#d48c12',
            activeforeground='white',
            state='disabled',
            **button_style
        )
        self.analyze_btn.pack(pady=5)

        self.plot_btn = tk.Button(
            left_panel,
            text="Построить график",
            command=self.plot_graph,
            bg='#20bf6b',
            fg='white',
            activebackground='#179754',
            activeforeground='white',
            state='disabled',
            **button_style
        )
        self.plot_btn.pack(pady=5)

        self.clear_btn = tk.Button(
            left_panel,
            text="Очистить",
            command=self.clear_output,
            bg='#4a5568',
            fg='white',
            activebackground='#2d3748',
            activeforeground='white',
            **button_style
        )
        self.clear_btn.pack(pady=5)

        self.info_label = tk.Label(
            left_panel,
            text="Файл не загружен",
            font=(self.font_family, 9),
            bg='#1a1a2e',
            fg='#718096',
            wraplength=200
        )
        self.info_label.pack(pady=(20, 5))

        right_panel = tk.Frame(main_container, bg='#1a1a2e')
        right_panel.pack(side='right', fill='both', expand=True)

        output_label = tk.Label(
            right_panel,
            text=" Результаты анализа:",
            font=(self.font_family, 12, 'bold'),
            bg='#1a1a2e',
            fg='#e94560'
        )
        output_label.pack(anchor='w')

        self.output_text = scrolledtext.ScrolledText(
            right_panel,
            height=10,
            font=('Courier New', 10),
            wrap=tk.WORD,
            bg='#0f0f1a',
            fg='#e0e0e0',
            insertbackground='white'
        )
        self.output_text.pack(fill='both', expand=True, pady=(5, 10))

        plot_label = tk.Label(
            right_panel,
            text="Область графика:",
            font=(self.font_family, 12, 'bold'),
            bg='#1a1a2e',
            fg='#e94560'
        )
        plot_label.pack(anchor='w')

        self.plot_frame = tk.Frame(right_panel, bg='#0f0f1a', height=350)
        self.plot_frame.pack(fill='both', expand=True, pady=(5, 0))
        self.plot_frame.pack_propagate(False)

        self.plot_info_label = tk.Label(
            self.plot_frame,
            text="График появится здесь\nпосле загрузки данных",
            font=(self.font_family, 12),
            bg='#0f0f1a',
            fg='#4a5568'
        )
        self.plot_info_label.pack(expand=True)

        footer_label = tk.Label(
            self.root,
            text="© Марта Ш-13 | Индустриальное программирование | РХТУ ПИШ ХИМ",
            font=(self.font_family, 9),
            bg='#1a1a2e',
            fg='#4a5568'
        )
        footer_label.pack(pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Выберите CSV файл",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if file_path:
            try:
                self.df = pd.read_csv(file_path)

                self.info_label.config(
                    text=f"Файл: {file_path.split('/')[-1]}\n{self.df.shape[0]} строк, {self.df.shape[1]} столбцов",
                    fg='#20bf6b'
                )

                self.numeric_columns = self.df.select_dtypes(include=[np.number]).columns.tolist()

                if not self.numeric_columns:
                    messagebox.showwarning("Предупреждение", "В таблице нет числовых столбцов для анализа!")
                    return

                self.column_combo['values'] = self.numeric_columns
                self.selected_column.set(self.numeric_columns[0])

                self.show_btn.config(state='normal')
                self.analyze_btn.config(state='normal')
                self.plot_btn.config(state='normal')

                info_text = f" Таблица успешно загружена!\n\n"
                info_text += f" Размер: {self.df.shape[0]} строк × {self.df.shape[1]} столбцов\n"
                info_text += f" Столбцы: {', '.join(self.df.columns)}\n"
                info_text += f" Числовые столбцы: {', '.join(self.numeric_columns)}\n\n"
                info_text += f" Первые 5 строк:\n\n"
                info_text += self.df.head().to_string()

                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(1.0, info_text)

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл:\n{str(e)}")
                self.info_label.config(text="❌ Ошибка загрузки файла", fg='#e94560')

    def show_table(self):
        if self.df is not None:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, self.df.to_string())
            messagebox.showinfo("Информация", "Таблица отображена в поле вывода")

    def analyze_data(self):
        if self.df is None:
            messagebox.showwarning("Предупреждение", "Сначала загрузите файл!")
            return

        if not self.selected_column.get():
            messagebox.showwarning("Предупреждение", "Выберите столбец для анализа!")
            return

        column = self.selected_column.get()

        if column not in self.df.columns:
            messagebox.showerror("Ошибка", "Выбранный столбец не найден!")
            return

        mean_val = self.df[column].mean()
        max_val = self.df[column].max()
        min_val = self.df[column].min()
        median_val = self.df[column].median()
        std_val = self.df[column].std()

        result = f" Анализ столбца: {column}\n"
        result += "=" * 50 + "\n"
        result += f"Среднее значение: {mean_val:.2f}\n"
        result += f"Минимальное значение: {min_val:.2f}\n"
        result += f"Максимальное значение: {max_val:.2f}\n"
        result += f"Медиана: {median_val:.2f}\n"
        result += f"Стандартное отклонение: {std_val:.2f}\n"
        result += "=" * 50 + "\n"
        result += f"Количество записей: {self.df[column].count()}\n"

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, result)

    def plot_graph(self):
        if self.df is None:
            messagebox.showwarning("Предупреждение", "Сначала загрузите файл!")
            return

        if not self.selected_column.get():
            messagebox.showwarning("Предупреждение", "Выберите столбец для построения графика!")
            return

        column = self.selected_column.get()

        if column not in self.df.columns:
            messagebox.showerror("Ошибка", "Выбранный столбец не найден!")
            return

        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
        fig.patch.set_facecolor('#0f0f1a')

        data_to_plot = self.df[column].head(20)
        ax1.plot(range(len(data_to_plot)), data_to_plot.values,
                 marker='o', linewidth=2, markersize=6, color='#e94560')
        ax1.set_title(f'Линейный график: {column}', fontsize=12, fontweight='bold', color='#e94560')
        ax1.set_xlabel('Индекс строки', fontsize=10, color='#e0e0e0')
        ax1.set_ylabel(column, fontsize=10, color='#e0e0e0')
        ax1.grid(True, alpha=0.3)
        ax1.set_facecolor('#1a1a2e')
        ax1.tick_params(colors='#e0e0e0')
        ax1.spines['bottom'].set_color('#4a5568')
        ax1.spines['top'].set_color('#4a5568')
        ax1.spines['left'].set_color('#4a5568')
        ax1.spines['right'].set_color('#4a5568')

        bars = ax2.bar(range(len(data_to_plot)), data_to_plot.values,
                       color='#20bf6b', alpha=0.8, edgecolor='#e94560', linewidth=1)
        ax2.set_title(f'Столбчатая диаграмма: {column}', fontsize=12, fontweight='bold', color='#e94560')
        ax2.set_xlabel('Индекс строки', fontsize=10, color='#e0e0e0')
        ax2.set_ylabel(column, fontsize=10, color='#e0e0e0')
        ax2.grid(True, alpha=0.3, axis='y')
        ax2.set_facecolor('#1a1a2e')
        ax2.tick_params(colors='#e0e0e0')
        ax2.spines['bottom'].set_color('#4a5568')
        ax2.spines['top'].set_color('#4a5568')
        ax2.spines['left'].set_color('#4a5568')
        ax2.spines['right'].set_color('#4a5568')

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

        info_text = f"Построены графики для столбца '{column}'\n"
        info_text += f"Линейный график и столбчатая диаграмма (первые 20 значений)\n"
        info_text += f"Всего значений в столбце: {self.df[column].count()}"
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, info_text)

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        self.plot_info_label = tk.Label(
            self.plot_frame,
            text="График появится здесь\nпосле загрузки данных",
            font=(self.font_family, 12),
            bg='#0f0f1a',
            fg='#4a5568'
        )
        self.plot_info_label.pack(expand=True)

        messagebox.showinfo("Очистка", "Вывод и график очищены")


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()
