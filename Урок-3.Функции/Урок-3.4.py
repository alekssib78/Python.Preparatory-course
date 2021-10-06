#    Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр
# - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по
# формуле damage / armor
# Следовательно, у вас должно быть 2 функции:

#    Наносит урон. Это улучшенная версия функции из задачи 3.

#    Вычисляет урон по отношению к броне.

#    Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и
# вычитания его из здоровья персонажа.
# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:

#    name - строка полученная от пользователя,
#    health = 100,
#    damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь

import random

name_1, name_2 = input('Введите имя игрока № 1 :'), input('Введите имя игрока № 2 :')
player = {
    'name': name_1,
    'health': 100,
    'damage': 15,
    'armore': 1.2
}
enemy = {
    'name': name_2,
    'health': 150,
    'damage': 10,
    'armore': 1.3
}
print(f'За player играет {name_1}')
print(f" {name_1} обладает силой {player['health']}, его максимальный урон {player['damage']},"
      f"сила его брони {player['armore']}")

print(f'За enemy играет {name_2}')
print(f" {name_2} обладает силой {enemy['health']}, его максимальный урон {enemy['damage']},"
      f"сила его брони {enemy['armore']}")


# надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать
# свои. ### Функция в качестве аргумента будет принимать атакующего и атакуемого. ### В теле
# функция должна получить параметр damage атакующего и отнять это количество от health
# атакуемого. Функция должна сама работать со словарями и изменять их значения.
# функция в качестве аргумента будет принимать атакующего и атакуемого. ### В теле
# функция должна получить параметр damage атакующего и отнять это количество от health
# атакуемого. Функция должна сама работать со словарями и изменять их значения.
def player_attak():
    print(f"Удар наносит {name_1},")
    udar = random.randint(0, player['damage'])
    print(f" его удар равен {udar}")
    if udar >= 13:
        print('А держика мою короночку !!!')
    elif udar == 0:
        print(f'лохонулся я немного {name_2}')
    else:
        print('Да это я бью от нехуй делать')


    def udar_player():
        enemy['health'] = round(enemy['health'] - (udar / enemy['armore']), 0)
    if udar != 0:
        udar_player()
    print(f"У игрока {name_2} осталось {enemy['health']} очков жизни")


def enemy_attak():
    print(f"Удар наносит {name_2}")
    udar = random.randint(0, enemy['damage'])
    print(f" его удар равен {udar}")

    print(f"У игрока {name_1} осталось {player['health']} очков жизни")

    def udar_enemy():
        player['health'] = round(player['health'] - (udar / player['armore']), 0)

    if udar != 0:
        udar_enemy()
    print(f"У игрока {name_1} осталось {player['health']} очков жизни")


while player['health'] > 0 or enemy['health'] > 0:
    player_attak()
    if enemy['health'] > 0:
        print(f"сейчас я тебе {name_1} въебу ответочку")
    else:
        print(f"{name_1} отмудохал ты меня !!!")
        break
    enemy_attak()
    if player['health'] > 0:
        print(f"а держика {name_2} сука с левой")
    else:
        print(f"{name_2} ну ты силен однако !!!")
        break
