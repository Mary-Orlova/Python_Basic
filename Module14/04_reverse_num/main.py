def opposite(num):
    parts = str(num).split('.')
    reversed_parts = [''.join(reversed(part)) for part in parts]

    return float( '.'.join(reversed_parts) )

n = opposite(input('Введите N: '))
k = opposite(input('Введите K: '))

print('Первое число наоборот:', n)
print('Второе число наоборот:', k)
print('Сумма:', n + k)




