import csv

def read_csv_file(file_name):
    students = []
    with open(file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

def task1(students):
    count = 0
    for student in students:
        if student['district'] == 'Ц' and student['favorite_subject'] == 'английский':
            count += 1
    print(f"Количество учеников в Центральном округе, выбравших английский язык: {count}")

def task2(students):
    scores = []
    for student in students:
        if student['district'] == 'В':
            scores.append(float(student['test_score']))
    average_score = sum(scores) / len(scores)
    print(f"Средний тестовый балл у учеников Восточного округа: {average_score}")

def task3(students):
    count = 0
    for student in students:
        if student['district'] in ['З', 'ЮЗ', 'Ц']:
            count += 1
    percentage = (count / len(students)) * 100
    print(f"Процент участников из округов З, ЮЗ и Ц: {percentage}%")

def task4(students, output_file):
    math_students = [student for student in students if student['favorite_subject'] == 'математика']
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=math_students[0].keys())
        writer.writeheader()
        for student in math_students:
            writer.writerow(student)
    print(f"Файл {output_file} успешно создан.")
            

file_name = 'var3.csv'
output_file = 'var3_output.csv'
students = read_csv_file(file_name)

task1(students)
task2(students)
task3(students)
task4(students, output_file)
