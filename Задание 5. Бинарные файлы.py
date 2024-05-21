import array

def negative(a):
    for i in range(0, len(a), 3):
        a[i], a[i+1], a[i+2] = 255-a[i], 255-a[i+1], 255-a[i+2]

def brighten(a, factor):
    for i in range(0, len(a), 3):
        a[i] = min(a[i] * factor, 255)
        a[i+1] = min(a[i+1] * factor, 255)
        a[i+2] = min(a[i+2] * factor, 255)

def darken(a, factor):
    brighten(a, 1/factor)

def mirror_horizontal(a, width):
    for i in range(len(a) // 2):
        mirror_index = width * 3 - (i % (width * 3)) - 3
        a[i], a[mirror_index] = a[mirror_index], a[i]
        a[i+1], a[mirror_index+1] = a[mirror_index+1], a[i+1]
        a[i+2], a[mirror_index+2] = a[mirror_index+2], a[i+2]

def mirror_vertical(a, width, height):
    for y in range(height // 2):
        for x in range(width):
            index1 = (y * width + x) * 3
            index2 = ((height - y - 1) * width + x) * 3
            a[index1], a[index2] = a[index2], a[index1]
            a[index1+1], a[index2+1] = a[index2+1], a[index1+1]
            a[index1+2], a[index2+2] = a[index2+2], a[index1+2]

def grayscale(a):
    for i in range(0, len(a), 3):
        brightness = int(0.2126 * a[i] + 0.7152 * a[i+1] + 0.0722 * a[i+2])
        a[i] = a[i+1] = a[i+2] = brightness

def rotate_90(a, width, height):
    new_a = array.array('B', [0] * len(a))
    for y in range(height):
        for x in range(width):
            new_x = height - y - 1
            new_y = x
            index1 = (y * width + x) * 3
            index2 = (new_y * height + new_x) * 3
            new_a[index2] = a[index1]
            new_a[index2+1] = a[index1+1]
            new_a[index2+2] = a[index1+2]
    return new_a

def process_image(filename, output_filename, operation):
    with open(filename, 'rb') as in_pic, open(output_filename, 'wb') as out_pic:
        head = in_pic.read(54)  
        a = array.array('B', in_pic.read())
        width, height = struct.unpack("<II", head[18:26])
        
        # Выберите нужную операцию
        if operation == "negative":
            negative(a)
        elif operation == "brighten":
            brighten(a, 2)
        # ... и так далее

        out_pic.write(head)
        out_pic.write(a.tobytes())

# Пример использования:
process_image("in.bmp", "out.bmp", "grayscale")