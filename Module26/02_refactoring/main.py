def generator(number: int):
    """Генератор для поиска x,y, ктр в результате = 56"""
    for x in list_1:
        for y in list_2:
            result = x * y
            try:
                if result == to_find:
                    print('\nFound!!!')
                    raise StopIteration
            except StopIteration:
                print('x =', x, 'y =', y, 'result =', result)


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

generation = generator(to_find)
