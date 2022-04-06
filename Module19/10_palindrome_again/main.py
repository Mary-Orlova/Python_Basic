text = input('Введите строку: ')
letters = set()

for letter in text:
    if letter in letters:
        letters.remove(letter)
    else:
        letters.add(letter)

if len(letters) > 1:
    print('Нельзя сделать палиндром')
else:
    print('Можно сделать палиндром')

