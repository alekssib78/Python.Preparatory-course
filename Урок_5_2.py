#    Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и
# group.pickle, прочитать из них информацию. И получить объект: словарь из предыдущего
# задания.
import pickle, json

with open('group.pickle', 'rb') as h:
    my_favourite_group = pickle.load(h)

print(my_favourite_group)


with open('group.json', 'r', encoding='utf-8') as h:
    my_favourite_group = json.load(h)

print(my_favourite_group)

