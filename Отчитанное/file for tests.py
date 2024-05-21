import os
import re

# Функция для поиска времени в формате hh:mm или hh:mm:ss
def find_time(text):
    return re.findall(r'\b(?:[01]\d|2[0-3]):(?:[0-5]\d)(?::[0-5]\d)?\b', text)

# Функция для поиска email-адресов
def find_emails(text):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Функция для поиска url-адресов
def find_urls(text):
    return re.findall(r'\b(?:http|https)://\S+\b', text)

# Функция для поиска корректных имен переменных в Питоне
def find_python_variables(text):
    return re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', text)

# Функция для поиска дат в различных форматах
def find_dates(text):
    return re.findall(r'\b(?:\d{1,2}[.-]\d{1,2}[.-]\d{2,4}|\d{2,4}[.-]\d{1,2}[.-]\d{1,2})\b', text)

# Функция для поиска вещественных чисел
def find_floats(text):
    return re.findall(r'\b\d+\.\d+\b', text)

# Функция для поиска номерных знаков российских транспортных средств
def find_russian_vehicle_numbers(text):
    return re.findall(r'\b[АВЕКМНОРСТУХABEKMHOPCTYX]{1}\d{3}[АВЕКМНОРСТУХABEKMHOPCTYX]{2}\d{2,3}\b', text)

# Заданная буква для поиска файлов
starting_letter = 'a'

# Путь к папке с файлами
folder_path = '/Users/arseniy/PycharmProjects/AoDS&PS/task2'

# Получаем список файлов в папке
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Фильтруем файлы по заданным критериям
filtered_files = [f for f in files if f.lower().startswith(starting_letter.lower()) and f[-2].isdigit() and len(os.path.splitext(f)[0]) >= 7 and f.lower().endswith('.txt')]

# Поиск данных в каждом из найденных файлах
for filename in filtered_files:
    with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
        file_content = file.read()
        times = find_time(file_content)
        emails = find_emails(file_content)
        urls = find_urls(file_content)
        python_variables = find_python_variables(file_content)
        dates = find_dates(file_content)
        floats = find_floats(file_content)
        vehicle_numbers = find_russian_vehicle_numbers(file_content)
        
        print(f"File: {filename}")
        print("Times:", times)
        print("Emails:", emails)
        print("URLs:", urls)
        print("Python Variables:", python_variables)
        print("Dates:", dates)
        print("Floats:", floats)
        print("Russian Vehicle Numbers:", vehicle_numbers)
        print()
