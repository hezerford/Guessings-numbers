from random import randrange

def is_valid(text):
    if text.isdigit():
        if 1 <= int(text) <= border:
            return True
        else:
            return False
    else:
        return False    

attemps = 0
print('Добро пожаловать в числовую угадайку \nВыберите правую конечную границу числа (это должно быть целое число)')

while True:
    border = input()
    if border.isdigit():
        border = int(border)
        break
    else:
        print('Вы не выбрали число, поэтому конечная граница равна 100')
        border = 100
        break

number = randrange(1, border+1)

while True:
    num = input(f'Попробуйте угадать число от 1 до {border} ... ')
    if is_valid(num):
        num = int(num)
        if number > num:
            print('Ваше число меньше загаданного, попробуйте ещё раз')
            attemps += 1
        elif number < num:
            print('Ваше число больше загаданного, попробуйте ещё раз')
            attemps += 1
        elif number == num:
            print(f'Вы угадали число за {attemps} попыток! \nПоздравляю! \nСпасибо, что играли в числовую угадайку. Еще увидимся...')
            s = input('Хотели бы вы сыграть ещё раз? \nд-да \nн-нет \n')
            if s == 'д':
                continue
            elif s == 'н':
                break
            else:
                while s != 'д' or s != 'н':
                    print('Я так и не понял, каков ваш ответ?')
                    s = input()
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')