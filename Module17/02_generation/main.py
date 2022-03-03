
diaposon = int(input('Введите длину списка: '))
list = [(1 if i_num % 2 == 0
         else i_num % 5)
        for i_num in range(diaposon)]

print(list)
