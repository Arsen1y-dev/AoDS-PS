import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  
        for row in reader:
            data.append(row)
    return data


def count_students_by_subject_and_district(data, subject, district):
    count = 0
    for row in data:
        if row[0] == district and row[2] == subject:
            count += 1
    return count


def calculate_average_score_by_district(data, district):
    scores = []
    for row in data:
        if row[0] == district:
            scores.append(int(row[3]))
    if scores:
        return sum(scores) / len(scores)
    else:
        return 0


def calculate_percentage_of_districts(data, districts):
    total_students = len(data)
    count_districts = 0
    for row in data:
        if row[0] in districts:
            count_districts += 1
    return (count_districts / total_students) * 100


def write_students_by_subject_to_csv(data, subject, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['округ', 'код ученика', 'любимый предмет', 'балл'])
        for row in data:
            if row[2] == subject:
                writer.writerow(row)


if __name__ == "__main__":

    file_path = 'var3.csv'
    students_data = read_csv_file(file_path)


    english_students_in_central_district = count_students_by_subject_and_district(students_data, 'английский язык', 'Ц')
    print("1) Количество учеников в Центральном округе, выбравших английский язык:", english_students_in_central_district)


    average_score_in_eastern_district = calculate_average_score_by_district(students_data, 'В')
    print("2) Средний тестовый балл у учеников Восточного округа:", average_score_in_eastern_district)

    districts_of_interest = ['З', 'ЮЗ', 'Ц']
    percentage_of_districts = calculate_percentage_of_districts(students_data, districts_of_interest)
    print("3) Процентное соотношение числа участников:", percentage_of_districts)

    output_file_path = 'res.csv'
    write_students_by_subject_to_csv(students_data, 'математика', output_file_path)
    print("4) Файл res.csv создан успешно.")