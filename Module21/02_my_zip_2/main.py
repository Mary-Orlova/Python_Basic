import itertools

def check(dictionary): # ПРОВЕРКА НА СЛОВАРЬ:
    try:
        isinstance(dictionary) in (list, str, int, list)  #  вместо dictionary подставляем остальные переменные
        print('Переменная не является словарем, проверьте остальные переменные.')
    except TypeError:
        dictionary = list(dictionary.items())  # вместо dictionary подставляем остальные переменные
        return  dictionary

def my_zip(*args):
    my_zip = []
    zip_files = itertools.zip_longest(*args,fillvalue=0)
    #контейнер для объединения файлов из каждой переменной -если кол-во переменных различны будет выводится 0
    #в переменную result кладем = генерирование добавления в список my_zip по элементно для каждого
    # элемента в списке контейнера zip_files
    result = [my_zip.append(everything) for everything
              in list(zip_files)]
    print(my_zip)

# string = 'abcd'
# numbers_tuple = (10, 20, 30, 40)
# list_number_and_letter = [100, 300, 'буква', 'а']
# numbers = 1,2,3,4
# dictionary = {'one': 65,'two': 87,'three':12, 'four':453}
#
# dictionary = check(dictionary) #Проверка на словарь
# my_zip(string,numbers_tuple,list_number_and_letter,numbers,dictionary) #Вызов осн ф-ции
#
