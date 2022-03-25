text = input('Введите строку: ').split()
longest_word = max([len(word) for word in text])
print('Самое длинное слово: ',
      *[word for word in text if len(word) == longest_word])
print('Длина этого слова: ', longest_word)
