import requests
import matplotlib.pyplot as plt
import pandas as pd

#Пример №1 - requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')

# Проверяем, успешный ли был запрос
if response.status_code == 200:
    # Если запрос успешен, выводим данные
    print(response.json())
else:
    # Если произошла ошибка, выводим код статуса
    print(f'Ошибка: {response.status_code}')



#Пример №2 - matplotlib.pyplot

# Пример данных
labels = ['Категория A', 'Категория B', 'Категория C', 'Категория D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']
explode = (0.1, 0, 0, 0)  # выделение первой категории

# Круговая диаграмма
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)


# чтобы круговая диаграмма была кругом
plt.axis('equal')
plt.title('Круговая диаграмма примера')
plt.show()





#Пример 3 - pandas

# Создаем DataFrame с данными
data = {
    'Название книги': ['1984', 'Моби Дик', 'Убить пересмешника', 'Гордость и предубеждение'],
    'Автор': ['Джордж Оруэлл', 'Герман Мелвилл', 'Харпер Ли', 'Джейн Остин'],
    'Год публикации': [1949, 1851, 1960, 1813],
    'Жанр': ['Достоевщина', 'Приключения', 'Драма', 'Роман'],
    'Количество страниц': [328, 635, 281, 432],
}

df = pd.DataFrame(data)

# Устанавливаем параметры для отображения всех столбцов
pd.set_option('display.max_columns', None)

# Выводим первые несколько строк данных
print("Анализ книг:")
print(df.head())

# Анализ: вычисляем среднее количество страниц
average_pages = df['Количество страниц'].mean()
print(f"\nСреднее количество страниц: {average_pages:.2f}")

# Группируем по жанрам и считаем количество книг
genre_counts = df['Жанр'].value_counts()
print("\nКоличество книг по жанрам:")
print(genre_counts)