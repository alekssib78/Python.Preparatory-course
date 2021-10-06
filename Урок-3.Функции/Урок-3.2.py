# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них

def num_max(a, b, c):                              # находим максимальное число при помощи объявленной функции
    n_max = max(a, b, c)
    return n_max
n_m = num_max(int(input('число№1 :')),int(input('число №2 :')),int(input('число №3 :')))
print(n_m)


a, b, c = int(input('число №1 :')), int(input('число №2 :')), int(input('число №3 :'))  # находим число без объявления функции
print(max(a, b, c))


if a >= b and a >= c:      # находим число при помощи if
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


def num_max_2(*args):
    return print(max(args))
num_max_2(1,2,3,4,5,6,7,8,9,0,)