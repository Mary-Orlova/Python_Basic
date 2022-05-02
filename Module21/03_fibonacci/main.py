def fibonacci(num_pos,first,second):
    for everything in range(2, num_pos):
        first, second = second, first + second
    print('Число: ', second)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи(число > 2):  '))
first = 1
second = 1

fibonacci(num_pos,first,second)

#Числа Фибоначчи — это ряд чисел,
# в котором каждое следующее число равно сумме двух предыдущих

