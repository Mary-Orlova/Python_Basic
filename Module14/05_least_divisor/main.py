def find(number, nod):
    while nod <= number:
        nod = nod + 1
        if number % nod == 0:
            print('Наименьший делитель, отличный от единицы:', nod)
            break


number = int(input('Введите число:'))
nod = 1
find(number, nod)