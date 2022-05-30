import random

syma, number = 0, 0

try:
    while syma < 777:
        with open('out_file.txt','a') as out_file:
            number = int(input('Введите число:'))
            choise = random.randint(1,13)
            if choise == 13:
                raise BaseException('Вас постигла неудача!')
            out_file.write(str(number))
            out_file.write('\n')
            syma += number
except ValueError:
    print('Ошибка: введено не число!')
else:
    print('Вы успешно выполнили условие для выхода из порочного ')

finally:
    print('\nСодержимое файла out_file.txt: ')
    print(open('out_file.txt','r').read())
