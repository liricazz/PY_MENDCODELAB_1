import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DS_1.csv')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(df.index, df['Средний_балл'], marker='o', linestyle='-', color='b', linewidth=2, markersize=4)
ax1.set_title('Линейный график: Средний балл студентов', fontsize=14, fontweight='bold')
ax1.set_xlabel('Номер студента (индекс)', fontsize=12)
ax1.set_ylabel('Средний балл', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, len(df))

top_students = df.head(15)
x = range(len(top_students))
width = 0.35

bars1 = ax2.bar([i - width/2 for i in x], top_students['Возраст'], width, label='Возраст', color='orange', alpha=0.7)
bars2 = ax2.bar([i + width/2 for i in x], top_students['Средний_балл'], width, label='Средний балл', color='green', alpha=0.7)

ax2.set_title('Столбчатая диаграмма: Возраст и Средний балл (первые 15 студентов)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Студент', fontsize=12)
ax2.set_ylabel('Значение', fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(top_students['ФИО'], rotation=45, ha='right', fontsize=8)
ax2.legend()
ax2.grid(True, alpha=0.3, axis='y')

plt.suptitle('Анализ данных студентов', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()