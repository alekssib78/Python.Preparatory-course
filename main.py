import sys
from core import complete_list, copy_to_copy, create_folder, create_file, remove_file, save_info, future
from game_t import game
save_info('начало')
command = sys.argv[1]

if command == 'список':
    try:
        folders_only = sys.argv[2]
    except IndexError:
        complete_list()
    else:
        complete_list(folders_only)
elif command == 'help':
    print('команды вводятся на русском')
    print('<<список>> - выводит список файлов и папок')
    print('<<удалить>> - удаляет объекты')
    print('<<создать_файл>> - создает файл')
    print('<<создать_папку>> - создает папку')
    print('<<копировать>> - копирует объект')
    print('<<переместить>> - перемещение папок и файлов')
    print('<<игра>> - запустить игру копм угадывает число')
elif command == 'удалить':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название файла')
    else:
        remove_file(name)

elif command == 'создать_файл':
    #   обрабатываем ошибку если нет названия файла _____________________________________
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введдите название файла')
    #   если в файле есть текст добавляем ________________________________________________
    try:
        name = sys.argv[2]
        text = sys.argv[3]
    except IndexError:
       create_file(name)
    else:
        create_file(name, text)

elif command == 'создать_папку':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название папки')
    else:
        create_folder(name)

elif command == 'копировать':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Что будем копировать???')
    else:
        try:
            new_name = sys.argv[3]
        except IndexError:
            print('Куда копируем???')
        else:
            copy_to_copy(name, new_name)
elif command == 'переместить':
    try:
        current_place = sys.argv[2]
    except IndexError:
        print('Что будем перемещать???')
    else:
        try:
            future_site = sys.argv[3]
        except IndexError:
            print('Куда копируем???')
        else:
            future(current_place, future_site)
elif command == 'играть':
    game()





save_info('конец')