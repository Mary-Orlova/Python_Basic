def recuracy(number):
    if number != 0:
        recuracy(number - 1)
        print(number)

number = int(input('Введите num: '))
recuracy(number)

