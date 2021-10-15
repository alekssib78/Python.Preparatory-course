import random


def game():



    #  если компьютер вывел число больше чем загадано нужно ввести знак '>' если меньше '<',если угадал '='
    a = 1  # минимальное число по условию равно 1
    b = 100  # максимальное число 100

    print('Загадайте число и никому не говорите')
    chislo = random.randint(a, b)
    while True:

        print(f'Ваше число равно {chislo}?')
        simbol = input('введите знак > если число меньше, < если число больше и = если числа равны  --')
        if simbol == '<' or simbol == '>' or simbol == '=':
            if simbol == '>':
                print(f'загаданое число больше {chislo}')
                a = chislo + 1

            elif simbol == '<':
                print(f'загаданное число меньше {chislo}')
                b = chislo - 1

            elif simbol == '=':
                print(f'Поздравляю угадал ваше число равно {chislo}')
                break
            chislo = random.randint(a, b)
        else:
            print("Введите символы '<' '>' '='")



if __name__ == '__main__':
    game()