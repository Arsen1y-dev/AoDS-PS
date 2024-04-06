import csv

with open('var1.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    
    belarus_cities = sum(1 for row in reader if row['Страна'] == 'Республика Беларусь')
    print("1. Количество городов Республики Беларусь:", belarus_cities)
    
    file.seek(0)
    next(reader)  
    
 
    population_sum = 0
    count = 0
    for row in reader:
        population = float(row['Численность населения'].replace(',', '.'))
        if population <= 100000:
            population_sum += population
            count += 1
    average_population = population_sum / count
    print("2. Средняя численность населения в городах до 100 тыс. человек:", average_population)
    

    file.seek(0)
    next(reader)  
    

    total_cities = sum(1 for row in csv.DictReader(open('var1.csv', encoding='utf-8'), delimiter=';'))
    belarus_percent = belarus_cities / total_cities * 100
    egypt_cities = sum(1 for row in csv.DictReader(open('var1.csv', encoding='utf-8'), delimiter=';') if row['Страна'] == 'Египет')
    egypt_percent = egypt_cities / total_cities * 100
    turkey_cities = sum(1 for row in csv.DictReader(open('var1.csv', encoding='utf-8'), delimiter=';') if row['Страна'] == 'Турция')
    turkey_percent = turkey_cities / total_cities * 100
    print("3. Процентное соотношение количества городов:")
    print("   Республика Беларусь:", belarus_percent)
    print("   Египет:", egypt_percent)
    print("   Турция:", turkey_percent)
    

    file.seek(0)
    next(reader) 
    

    with open('res.csv', mode='w', encoding='utf-8', newline='') as result_file:
        fieldnames = ['Город', 'Численность населения', 'Страна']
        writer = csv.DictWriter(result_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        
        for row in reader:
            if row['Страна'] == 'Россия':
                writer.writerow(row)