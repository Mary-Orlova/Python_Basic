text = input('Введите строку: ').split()
longest_word = max([len(x) for x in text])
print('Самое длинное слово: ',
      *[x for x in text if len(x) == longest_word])
print('Длина этого слова: ', longest_word)
