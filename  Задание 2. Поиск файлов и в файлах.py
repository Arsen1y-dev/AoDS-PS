import fnmatch
import os
import re
import chardet

files = []  # создаем пустой список для хранения имен файлов
letter = input('Задайте букву: ')  # запрашиваем у пользователя букву
for file in os.listdir('task2'):  # перебираем все файлы в директории 'task2'
    if fnmatch.fnmatch(file, '*.txt'):  # проверяем, является ли файл текстовым (*.txt)
        filename = file[:-4]  # извлекаем имя файла без расширения
        if filename[0] == letter:  # проверяем, начинается ли имя файла с заданной буквы
            if len(filename) >= 7:  # проверяем, что длина имени файла не менее 7 символов
                if filename[-2] in '1234567890':  # проверяем, что предпоследний символ имени файла - цифра
                    files.append(file)  # добавляем файл в список files

def detect_encoding(file_path):
    """
    Определяет кодировку файла, используя библиотеку chardet.
    """
    with open(file_path, 'rb') as f:  # открываем файл в бинарном режиме для чтения
        result = chardet.detect(f.read())  # определяем кодировку с помощью chardet
    return result['encoding']  # возвращаем кодировку

def find_time_in_files(file):
    """
    Ищет время в формате hh:mm или hh:mm:ss в файле.
    """
    encoding = detect_encoding(file)  # определяем кодировку файла
    time_pattern = re.compile(r'\b(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?\b')  # регулярное выражение для поиска времени
    with open(file, 'r', encoding=encoding) as f:  # открываем файл в текстовом режиме с определенной кодировкой
        content = f.read()  # считываем содержимое файла
    matches = re.findall(time_pattern, content)  # ищем совпадения с помощью регулярного выражения
    return matches  # возвращаем найденные совпадения

# email-адреса;
def find_emails_in_files(file):
    encoding = detect_encoding(file)
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    with open(file, 'r', encoding=encoding) as f:
        content = f.read()
    matches = re.findall(email_pattern, content)
    return matches

# url-адреса;
def find_urls_in_files(file):
    encoding = detect_encoding(file)
    url_pattern = re.compile(r'\b(?:https?|ftp):\/\/[^\s/$.?#].[^\s]*\b')
    with open(file, 'r', encoding=encoding) as f:
        content = f.read()
    matches = re.findall(url_pattern, content)
    return matches

# корректные имена переменных в Питоне;
def find_valid_python_variable_names(file):
    encoding = detect_encoding(file)
    variable_name_pattern = re.compile(r'\b[a-zA-Z_]\w*\b')
    with open(file, 'r', encoding=encoding) as f:
        content = f.read()
    matches = re.findall(variable_name_pattern, content)
    return matches

# даты в различных форматах;
def find_dates_in_files(file):
    encoding = detect_encoding(file)
    date_pattern = re.compile(r"\b\d{1,2}[-/.]\d{1,2}[-/.]\d{4}\b|\b\d{4}[-/.]\d{1,2}[-/.]\d{1,2}\b")
    #date_pattern = re.compile(r'\b\d{1,4}[-/.]\d{1,2}[-/.]\d{1,4}\b|\b\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}\b|\b\d{1,2}[-/.]\w{1,2}[-/.]\d{2,4}\b')
    with open(file, 'r', encoding=encoding) as file:
        content = file.read()
    matches = re.findall(date_pattern, content)
    return matches

# вещественные числа;
def find_float_numbers(file):
    encoding = detect_encoding(file)
    float_pattern = re.compile(r'\b\d+\.\d+\b|\b\d+\.\d+e[+-]?\d+\b|\b\d+e[+-]?\d+\b')
    with open(file, 'r', encoding=encoding) as file:
        content = file.read()
    matches = re.findall(float_pattern, content)
    return matches

# номерные знаки российских транспортных средств.
def find_russian_vehicle_numbers(file):
    encoding = detect_encoding(file)
    pattern = re.compile(r'[A-ЯA-Z]{1}[0-9]{3}[A-ЯA-Z]{2}|[A-ЯA-Z]{1}[0-9]{3}[A-ЯA-Z]{2}[0-9]{2,3}|[0-9]{4}[A-ЯA-Z]{2}')
    with open(file, 'r', encoding=encoding) as file:
        content = file.read()
    matches = re.findall(pattern, content)
    return matches


for file in files:
    file_path = os.path.join('task2', file) # формируем полный путь к файлу
    print(f"В файле {file}:")
    if find_time_in_files(file_path):
        time = find_time_in_files(file_path)
        print(f"Время: {time}")
    if find_emails_in_files(file_path):
        email = find_emails_in_files(file_path)
        print(f"Email-адреса: {email}")
    if find_urls_in_files(file_path):
        url = find_urls_in_files(file_path)
        print(f"URL-адреса: {url}")
    if find_valid_python_variable_names(file_path):
        name = find_valid_python_variable_names(file_path)
        print(f"Имена переменных в Python: {name}")
    if find_dates_in_files(file_path):
        date = find_dates_in_files(file_path)
        print(f'Дата: {date}')
    if find_float_numbers(file_path):
        float_number = find_float_numbers(file_path)
        print(f'Вещественные числа: {float_number}')
    if find_russian_vehicle_numbers(file_path):
        vehicle_numbers = find_russian_vehicle_numbers(file_path)
        print(f'Номерные знаки российских транспортных средств: {vehicle_numbers}')
    print()
