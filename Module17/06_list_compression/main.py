import random

diaposon = int(input('Кол-во чисел в списке: '))

list_word = [random.randint(0,2) for i in range(diaposon)]
print('Список до сжатия: ', list_word)

list_word_2 = [i for i in list_word if i]
print('Список после сжатия: ', list_word_2)


