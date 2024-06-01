import array  
import struct  

def bmp_negative(in_file, out_file):
    """Создает негативное изображение из BMP-файла."""
    with open(in_file, 'rb') as in_pic, open(out_file, 'wb') as out_pic:  
        head = in_pic.read(54)  
        a = array.array('B', in_pic.read())  # Считываем данные пикселей в массив байтов
        for i in range(len(a)):  # Проходимся по каждому байту в массиве
            a[i] = 255 - a[i]  # Инвертируем значение пикселя
        out_pic.write(head)  # Записываем заголовок в выходной файл
        out_pic.write(a.tobytes())  # Записываем измененные данные пикселей

def bmp_brightness(in_file, out_file, brightness):
    """Регулирует яркость BMP-изображения."""
    with open(in_file, 'rb') as in_pic, open(out_file, 'wb') as out_pic:  # 
        head = in_pic.read(54)  
        a = array.array('B', in_pic.read())  # Считываем данные пикселей
        for i in range(len(a)):  # Проходимся по каждому пикселю
            a[i] = max(0, min(a[i] + brightness, 255))  # Добавляем яркость, ограничивая значения от 0 до 255
        out_pic.write(head)  
        out_pic.write(a.tobytes())  

def bmp_mirror(in_file, out_file, direction):
    """Зеркально отражает BMP-изображение по горизонтали или вертикали."""
    with open(in_file, 'rb') as in_pic, open(out_file, 'wb') as out_pic:  
        head = in_pic.read(54)  
        width = struct.unpack('<i', head[18:22])[0]  # Извлекаем ширину из заголовка
        height = struct.unpack('<i', head[22:26])[0]  # Извлекаем высоту из заголовка
        a = array.array('B', in_pic.read())  # Считываем данные пикселей
        if direction == 'horizontal':  # Отражение по горизонтали
            for y in range(height):  # Проходимся по строкам
                for x in range(width // 2):  # Проходимся по половине столбцов
                    i = (y * width + x) * 3  # Индекс пикселя в исходном массиве
                    j = (y * width + width - x - 1) * 3  # Индекс пикселя, симметричного относительно середины
                    a[i:i+3], a[j:j+3] = a[j:j+3], a[i:i+3]  # Меняем местами данные пикселей
        elif direction == 'vertical':  # Отражение по вертикали
            for y in range(height // 2):  # Проходимся по половине строк
                for x in range(width):  # Проходимся по столбцам
                    i = (y * width + x) * 3  # Индекс пикселя в исходном массиве
                    j = ((height - y - 1) * width + x) * 3  # Индекс пикселя, симметричного относительно середины
                    a[i:i+3], a[j:j+3] = a[j:j+3], a[i:i+3]  # Меняем местами данные пикселей
        out_pic.write(head)  # Записываем заголовок
        out_pic.write(a.tobytes())  

def bmp_grayscale(in_file, out_file, weighted=False):
    """Преобразует BMP-изображение в оттенки серого."""
    with open(in_file, 'rb') as in_pic, open(out_file, 'wb') as out_pic:  
        head = in_pic.read(54)  
        a = array.array('B', in_pic.read())  # Считываем данные пикселей
        for i in range(0, len(a), 3):  # Проходимся по пикселям с шагом 3 (RGB)
            if weighted:  # Взвешенное вычисление оттенка серого
                gray = int(0.299 * a[i] + 0.587 * a[i+1] + 0.114 * a[i+2])  # Вычисляем среднее значение с учетом цветового восприятия
            else:  # Простое среднее значение
                gray = int((a[i] + a[i+1] + a[i+2]) / 3)  # Вычисляем среднее значение
            a[i] = gray  # Устанавливаем значение оттенка серого для красного канала
            a[i+1] = gray  # Устанавливаем значение оттенка серого для зеленого канала
            a[i+2] = gray  # Устанавливаем значение оттенка серого для синего канала
        out_pic.write(head)  # Записываем заголовок
        out_pic.write(a.tobytes()) 

def bmp_rotate(in_file, out_file, angle):
    """Поворачивает BMP-изображение на заданный угол."""
    with open(in_file, 'rb') as in_pic, open(out_file, 'wb') as out_pic:  
        head = in_pic.read(54)  
        width = struct.unpack('<i', head[18:22])[0]  # Извлекаем ширину
        height = struct.unpack('<i', head[22:26])[0]  # Извлекаем высоту
        a = array.array('B', in_pic.read())  # Считываем данные пикселей
        if angle == 90:  # Поворот на 90 градусов
            new_a = array.array('B', [0 for _ in range(width * height * 3)])  # Создаем новый массив для повернутых данных
            for y in range(height):  # Проходимся по строкам
                for x in range(width):  # Проходимся по столбцам
                    i = (y * width + x) * 3  # Индекс пикселя в исходном массиве
                    j = (x * height + height - y - 1) * 3  # Индекс пикселя в повернутом массиве
                    new_a[j:j+3] = a[i:i+3]  # Копируем данные пикселя
            head = head[:18] + struct.pack('<i', height) + struct.pack('<i', width) + head[26:]  # Обновляем заголовок
            out_pic.write(head)  
            out_pic.write(new_a.tobytes())  # Записываем повернутые данные
        elif angle == 180:  # Поворот на 180 градусов
            for y in range(height):  # Проходимся по строкам
                for x in range(width // 2):  # Проходимся по половине столбцов
                    i = (y * width + x) * 3  # Индекс пикселя в исходном массиве
                    j = (y * width + width - x - 1) * 3  # Индекс пикселя, симметричного относительно середины
                    a[i:i+3], a[j:j+3] = a[j:j+3], a[i:i+3]  # Меняем местами данные пикселей
            for y in range(height // 2):  # Проходимся по половине строк
                for x in range(width):  # Проходимся по столбцам
                    i = (y * width + x) * 3  # Индекс пикселя в исходном массиве
                    j = ((height - y - 1) * width + x) * 3  # Индекс пикселя, симметричного относительно середины
                    a[i:i+3], a[j:j+3] = a[j:j+3], a[i:i+3]  # Меняем местами данные пикселей
            out_pic.write(head)  
            out_pic.write(a.tobytes())  # Записываем измененные данные
        elif angle == 270:  # Поворот на 270 градусов
            new_a = array.array('B', [0 for _ in range(width * height * 3)])  # Создаем новый массив для повернутых данных
            for y in range(height):  # Проходимся по строкам
                for x in range(width):  # Проходимся по столбцам
                    i = (y * width + x) * 3  # Индекс пикселя в исходном массиве
                    j = (height - y - 1) * width + (width - x - 1) * 3  # Индекс пикселя в повернутом массиве
                    new_a[j:j+3] = a[i:i+3]  # Копируем данные пикселя
            head = head[:18] + struct.pack('<i', width) + struct.pack('<i', height) + head[26:]  # Обновляем заголовок
            out_pic.write(head)  # Записываем заголовок
            out_pic.write(new_a.tobytes())  # Записываем повернутые данные

bmp_negative('in.bmp', 'out_negative.bmp')
bmp_brightness('in.bmp', 'out_brightness.bmp', 50)
bmp_mirror('in.bmp', 'out_horizontal_mirror.bmp', 'horizontal')
bmp_mirror('in.bmp', 'out_vertical_mirror.bmp', 'vertical')
bmp_grayscale('in.bmp', 'out_grayscale.bmp')
bmp_grayscale('in.bmp', 'out_grayscale_weighted.bmp', weighted=True)
bmp_rotate('in.bmp', 'out_rotate_90.bmp', 90)
bmp_rotate('in.bmp', 'out_rotate_180.bmp', 180)
bmp_rotate('in.bmp', 'out_rotate_270.bmp', 270)

"""
a: Это массив байтов, представляющий данные пикселей изображения.
i: Индекс первого пикселя, который нужно поменять местами.
j: Индекс второго пикселя, который нужно поменять местами.
i:i+3: Срез массива a от i до i+3 (включительно), представляющий 3 байта RGB-данных для одного пикселя.
j:j+3: Срез массива a от j до j+3, представляющий 3 байта RGB-данных для другого пикселя.
Как работает обмен:
Считывание данных: Python создает две временные копии:
a[i:i+3] - копирует 3 байта RGB-данных пикселя с индексом i.
a[j:j+3] - копирует 3 байта RGB-данных пикселя с индексом j.
Запись данных: Python записывает эти скопированные данные обратно в массив a, меняя их местами:
a[i:i+3] = a[j:j+3] - 3 байта RGB-данных из пикселя j записываются в позицию i.
a[j:j+3] = a[i:i+3] - 3 байта RGB-данных из пикселя i записываются в позицию j.
"""