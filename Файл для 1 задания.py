import os
import shutil

def print_state(state):
    input("Нажмите Enter для продолжения...")
    print(state)

def main():
    # 1. Вывести текущую директорию
    current_dir = os.getcwd()
    print_state(f"Текущая директория: {current_dir}")

    # 2. Вывести логин текущего пользователя
    current_user = os.getlogin()
    print_state(f"Логин текущего пользователя: {current_user}")

    # 3. Вывести тип операционной системы
    os_type = os.name
    os_type_desc = "Windows" if os_type == "nt" else "POSIX"
    print_state(f"Тип операционной системы: {os_type_desc}")

    # 4. Проверить, существует ли файл 'test.txt'
    file_exists = os.path.exists('test.txt')
    print_state(f"Файл 'test.txt' существует: {file_exists}")

    # 5. Вывести содержимое текущей папки
    contents = os.listdir('.')
    print_state(f"Содержимое текущей папки: {contents}")

    # 6. Вывести файловую структуру
    print_state("Файловая структура:")
    for dirpath, dirnames, filenames in os.walk('.'):
        print(f"Директория: {dirpath}")
        for file in filenames:
            print(f"Файл: {os.path.join(dirpath, file)}")

    # 7. Создать папку 'test'
    if not os.path.exists('test'):
        os.mkdir('test')
        print_state("Папка 'test' успешно создана")

    # 8. Перейти в папку 'test'
    os.chdir('test')
    print_state("Перешли в папку 'test'")

    # 9. Запросить у пользователя имя файла и создать файл с таким именем
    filename = input("Введите имя файла для создания: ")

    with open(filename, 'w') as f:
        f.write(current_user)

    # 10. Проверить, успешно ли создан файл
    file_path = os.path.join(os.getcwd(), filename)
    is_file = os.path.isfile(file_path)
    print_state(f"Файл успешно создан: {is_file}")

    # 11. Вывести абсолютный путь и размер файла
    file_size = os.path.getsize(file_path)
    print_state(f"Абсолютный путь: {file_path}, Размер: {file_size} байт")

    # 12. Скопировать файл на уровень выше
    shutil.copy(filename, os.path.join('..', filename))
    print_state("Файл скопирован на уровень выше")

    # 13. Подняться на уровень выше и вывести содержимое
    os.chdir('..')
    print_state("Вернулись на уровень выше")
    print_state("Содержимое текущей папки:")
    for item in os.listdir('.'):
        print(item)

    # 14. Вывести содержимое скопированного файла
    with open(filename, 'r') as f:
        copied_content = f.read()
    print_state(f"Содержимое скопированного файла '{filename}': {copied_content}")

    # 15. Удалить папку 'test'
    shutil.rmtree('test')
    print_state("Папка 'test' со всем содержимым удалена")

    # 16. Удалить скопированный файл
    os.remove(filename)
    print_state(f"Файл '{filename}' удален")

    # 17. Проверить удаление
    print_state("Проверка:")
    print_state(f"Папка 'test' существует: {os.path.exists('test')}")
    print_state(f"Файл '{filename}' существует: {os.path.exists(filename)}")

if __name__ == "__main__":
    main()
