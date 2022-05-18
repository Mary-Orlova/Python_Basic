import os
import string
from collections import Counter

zen_file = open(os.path.join('..', '02_zen_of_python', 'zen.txt'))
file_read = zen_file.read()
zen_file.seek(0)

file_words = zen_file.read().split()
zen_file.seek(0)

file_rls = zen_file.readlines()
chars = [letter for letter in file_read if letter in string.ascii_letters]
zen_common = ''.join(filter(str.isalnum, file_read.lower())) #текст без спец символов -как строка
rare_letter = Counter(zen_common).most_common()[-1] #последний элемент массива - встречается реже всего, выводится буква и кол-во


print('Количество букв в файле:', len(chars))
print('Количество слов в файле: ', len(file_words))
print('Количество строк в файле:' , len(file_rls))
print('Наиболее редкая буква: ', rare_letter)

zen_file.close()
