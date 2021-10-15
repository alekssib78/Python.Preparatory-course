import os
import shutil
import datetime


# создание директорий(папок) os.mkdir ошибка если папка существует
# создание файла "with open(имя файла,encoding = 'utf-8') as файл
# функция выводит содержимое директории
# удаление файла os.remove(имя)


def create_file(name, text=None):  # функция создания файла
    with open(name, 'w', encoding='utf-8') as f:  # сохраняем файл в переменную f
        if text:  # если есть текст записываем если нет создаем пустой файл
            f.write(text)  # записываем текст
    print(f'файл <<{name}>> создан')


def create_folder(name):  # Функция создания папок
    try:  # обрабатываем ошибку если папка уже существует
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже создана')
    else:
        print(f'папка <<{name}>> создана')


def complete_list(folders_only=False):  # функция выводит содержимое директорий
    result = os.listdir()  # выводит все содержимое директории если аргумент False
    if folders_only:  # если аргумент True
        result = [f for f in result if os.path.isdir(f)]  # выводит только папки
    print(result)


def remove_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
            print(f'Папка <<{name}>> была успешно удалена')
        else:
            os.remove(name)
            print(f'Файл <<{name}>> был успешно удален')
    except FileNotFoundError:
        print(f' <<{name}>> не существует')


def copy_to_copy(name, new_name):
    try:
        if os.path.isdir(name):
            try:
                shutil.copytree(name, new_name)
                print(f'папка <<{name}>> скопирована в <<{new_name}>>')
            except FileExistsError:
                print(f'папка <<{new_name}>> уже существует')
        else:
            shutil.copy(name, new_name)
            print(f'файл <<{name}>> успешно скопирован в <<{new_name}>>')
    except FileNotFoundError:
        print(f' файла <<{name}>> не существует')


def save_info(message):
    now = datetime.datetime.now()
    result = f'{now} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def future(current_place, future_site):
    try:
        shutil.move(current_place, future_site)
        print('Файл успешно перемещен')
    except FileNotFoundError:
        print('Нет такого файла')


if __name__ == "__main__":
    # 1 создаем файл______________________________________________
    try:
        create_file()  # вызываем функцию создания файла  и обрабатываем исключения если нет аргумента
    except TypeError:
        print('Нужно ввести название файла')
    # 2 создаем папку_____________________________________________
    try:
        create_folder('reut')
    except TypeError:
        print('Нужно ввести название папки')
    # 3 вывести список папок и файлов____________________________
    try:
        complete_list()
    except NameError:
        print(' Введите True, False - по умолчанию. ')
    # 4 удаляет файл или папку___________________________________
    try:
        remove_file()
        remove_file()
    except TypeError:
        print('Что будем удалять???')
    # 5 копирует файл или папку_________________________________
    try:
        copy_to_copy('dfdf', 'sdsds')
    except TypeError:
        print('Куда копируем?')

    # 6 запись лога  выполнения действий________________________
    save_info('Привет')

    # 7 перемещение файлов и папок______________________________

    try:
        future()
    except TypeError:
        print('Что и куда перемещаем?')