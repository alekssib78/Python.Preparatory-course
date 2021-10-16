#   Дан список, заполненный произвольными числами. Получить список из элементов исходного,
# удовлетворяющих следующим условиям:
# 		    Элемент кратен 3,
# 		    Элемент положительный,
# 		    Элемент не кратен 4.
#      	Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда
# отрицательные числа. 10-20 чисел в списке вполне достаточно.

num = [
    12, 45, -76, 48, 3, -9, 69, 123, -56, -22, 10, 55
]
# 1_____________________________________________________
num_ok = []
for i in num:
    if i % 3 == 0 and i > 0 and i % 4 != 0:
        num_ok.append(i)
print(f'{num_ok} {"num_ok"}')
# 2____________________________________________________
num_1 = [
    n for n in num
    if n % 3 == 0 and n % 4 != 0 and n > 0
]
print(f'{num_1} {"num_1"}')