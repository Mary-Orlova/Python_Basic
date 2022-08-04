print('\nПервый способ \nПростые числа: ')

print(list(filter(lambda number: all(map(lambda i: number % i != 0, range(2, int(
    number ** 0.5) + 1))), range(2, int(1000) + 1))))


print('\nВторой способ \nПростые числа:')

for k in range(2, 1000 + 1):
    prime = True
    for i in range(2, k):
        if k % i == 0:
            prime = False
            break

    if prime:
        print(k, end=' ')
