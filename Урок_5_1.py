#  Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой
# музыкальной группы, например:
#
# my_favourite_group = {
#     ‘name’: ‘Г.М.О.’,
#     ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
#     ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
#     {‘name’: ‘Шапито’,‘year’: 2014}]
#  }
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести
# результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно.
#  В файле group.json указать кодировку utf-8.


my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
               {'name': 'Шапито', 'year': 2014}]
}


#import pickle

# with open('group.pickle', 'wb') as poh:
#     pickle.dump(my_favourite_group, poh)
#
# print('Объект group.pickle, успешно записан!!!')

# with open('group.pickle', 'rb') as poh:
#     album = pickle.load(poh)
#
# print(album)


import json
# with open('group.json', 'w', encoding='utf-8') as poh:
#     json.dump(my_favourite_group, poh)
#
# print('Усе готово шеф файл group.json записан!!!')

with open('group.json', 'r', encoding='utf-8') as poh:
    group = json.load(poh)
print(group)




