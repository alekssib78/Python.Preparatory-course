#     Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список из квадратных
# корней чисел (если число положительное) и самих чисел (если число отрицательное) и возвращает результат (желательно
# применить генератор и тернарный оператор при необходимости). В результате работы функции исходный список не должен
# измениться.
# Например:
#
# 		old_list = [1, -3, 4]
# 		result = [1, -3, 2]
# 	Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить
#  туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
import math

num = [
    12, 45, -76, 48, 3, -9, 69, 123, -56, -22, 10, 55, 232, 8, 11, -6, -78, 1
]


# 1 лохонулся и вывел число в квадрате вместо квадратного корня
def num_v_kvadrate(nums):
    num_1 = [n ** 2 if n > 0 else n for n in nums]
    print(num_1)
num_v_kvadrate(num)
print(num)

# 2 попытка №2 вывести корень квадратный

def square_root(nums):
    num_2 = [math.sqrt(n) if n > 0 else n for n in nums]
    print(num_2,'корень из числа больше ноля')
square_root(num)
print(num)
