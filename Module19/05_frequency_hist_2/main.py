def histogram(string):
    symbol_dict = dict()
    for symbol in string:
        if symbol in symbol_dict:
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    return symbol_dict

def original():
    for symbol in sorted(hist.keys()):
        print(symbol, ':', hist[symbol])

def inverted():
    for letter, number in hist.items():
        if number not in words:
            words[number] = []
            words[number].append(letter)
        else:
            words[number].append(letter)
    for symbol in words:
        print(symbol, ':', words[symbol])


text = input('Введите текст: ').lower()
hist = histogram(text)
print('Оригинальный словарь частот: ')
original()
print('Инвертированный словарь частот: ')
words = dict()
inverted()
