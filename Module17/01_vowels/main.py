text = input('Введите текст: ')


list_vowels = ['а','у','о','ы','и','э','я','ю','ё','е']
list_add = []

for i_symbol in range(len(text)):
    if text[i_symbol] in list_vowels:
        list_add.append(text[i_symbol])
print('Список гласных букв: ',list_add,'\nДлина списка:',len(list_add))



