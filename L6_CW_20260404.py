import pandas as pd

df = pd.read_csv('DS_1.csv')

print("Размер таблицы:", df.shape)
print()

print("Названия столбцов:", list(df.columns))
print()

print("Первые 5 строк:")
print(df.head())
print()

print("Столбец Возраст:")
print(df['Возраст'])
print()

print("Столбцы ФИО, Группа, Средний_балл:")
print(df[['ФИО', 'Группа', 'Средний_балл']])
print()

print("Средний возраст студентов:", df['Возраст'].mean())
print()

print("Максимальный балл по математике:", df['Математика'].max())
print()

print("Минимальный балл по физике:", df['Физика'].min())
print()

print("Студенты старше 21 года:")
print(df[df['Возраст'] > 21])
print()

print("Студенты с посещаемостью выше 85:")
print(df[df['Посещаемость'] > 85])
print()

print("Таблица, отсортированная по Средний_балл (по убыванию):")
print(df.sort_values('Средний_балл', ascending=False))
