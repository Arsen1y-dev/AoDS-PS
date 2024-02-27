import os
import shutil

def print_current_directory():
    print("Текущая директория:", os.getcwd())

def print_current_user():
    print("Логин текущего пользователя:", os.getlogin())

def print_os_type():
    print("Тип операционной системы:", os.name)
    if os.name == 'posix':
        print("Unix (Linux/Mac OS X)")
    elif os.name == 'nt':
        print("Windows")

def check_file_existence(filename):
    if os.path.exists(filename):
        print("Файл '{}' существует.".format(filename))
    else:
        print("Файл '{}' не существует.".format(filename))

def print_directory_contents():
    print("Содержимое текущей папки:")
    for item in os.listdir():
        print(item)

def print_file_structure():
    print("Файловая структура текущей директории:")
    for root, dirs, files in os.walk(os.getcwd()):
        level = root.replace(os.getcwd(), '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print('{}{}'.format(subindent, file))

def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Папка '{}' успешно создана.".format(directory))
    else:
        print("Папка '{}' уже существует.".format(directory))

def create_file(filename):
    with open(filename, 'w') as f:
        f.write("Создано пользователем {}".format(os.getlogin()))
    print("Файл '{}' успешно создан.".format(filename))

def print_file_info(filename):
    if os.path.isfile(filename):
        print("Абсолютный путь к файлу:", os.path.abspath(filename))
        print("Размер файла:", os.path.getsize(filename), "байт")
    else:
        print("'{}' не является файлом.".format(filename))

def copy_file(source, destination):
    shutil.copyfile(source, destination)
    print("Файл успешно скопирован в '{}'.".format(destination))

def delete_directory(directory):
    shutil.rmtree(directory)
    print("Папка '{}' успешно удалена.".format(directory))

def delete_file(filename):
    os.remove(filename)
    print("Файл '{}' успешно удален.".format(filename))

def main():
    print_current_directory()
    input("Нажмите Enter для продолжения...")

    print_current_user()
    input("Нажмите Enter для продолжения...")

    print_os_type()
    input("Нажмите Enter для продолжения...")

    check_file_existence('test.txt')
    input("Нажмите Enter для продолжения...")

    print_directory_contents()
    input("Нажмите Enter для продолжения...")

    print_file_structure()
    input("Нажмите Enter для продолжения...")

    create_directory('test')
    os.chdir('test')
    print_current_directory()
    input("Нажмите Enter для продолжения...")

    filename = input("Введите имя файла для создания: ")
    create_file(filename)
    input("Нажмите Enter для продолжения...")

    print_file_info(filename)
    input("Нажмите Enter для продолжения...")

    copy_file(filename, os.path.join(os.path.dirname(os.getcwd()), filename))
    input("Нажмите Enter для продолжения...")

    os.chdir(os.path.dirname(os.getcwd()))
    print_current_directory()
    input("Нажмите Enter для продолжения...")

    print_directory_contents()
    input("Нажмите Enter для продолжения...")

    with open(filename, 'r') as f:
        print("Содержимое скопированного файла:")
        print(f.read())
    input("Нажмите Enter для продолжения...")

    delete_directory('test')
    input("Нажмите Enter для продолжения...")

    delete_file(filename)
    input("Нажмите Enter для продолжения...")

    print_directory_contents()

if __name__ == "__main__":
    main()
