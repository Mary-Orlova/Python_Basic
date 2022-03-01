
text = input('Введите строку: ')

subsequence = text[text.find('h') + 1:text.rfind('h')]
text = subsequence[::-1]

print(text)