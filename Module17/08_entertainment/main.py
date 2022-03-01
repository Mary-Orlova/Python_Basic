sticks = list('I' * int(input('Кол-во палок: ')))
part = int(input('Кол-во бросков: '))

for i in range(1, part + 1):
    left = int(input('Сбиты с номера '))
    right = int(input('по номер '))
    for j in range(left - 1, right):
        print('Бросок', j, ': ')
        sticks[j] = '.'
print('Результат: ', ''.join(sticks))
