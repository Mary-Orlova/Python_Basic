caple_count = int(input('Введите количество пар слов: '))
caple_dict = dict()

for word in range(caple_count):
    first, second = input('{} пара слов: '.format(word + 1)).lower().split(' - ')
    caple_dict[first] = second
    caple_dict[second] = first

print(caple_dict)

while True:
    word_find = input('\nВведите слово: ')
    if word_find in caple_dict:
        print('Синоним: ', caple_dict.get(word_find).title())
    else:
        print('Такого слова в словаре нет.')


