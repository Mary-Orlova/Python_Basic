text = input('Введите строку: ')
correct_text = ''
count = 1

for symbol in range(len(text)-1):
    if text[symbol] == text[symbol + 1]:
       count +=1
    elif text[symbol] != text[symbol + 1] or i_sym == len(text) - 2:
        correct_text += text[symbol] + str(count)
        count = 1

if text[-2] != text[-1]:
    correct_text += text[-1] + '1'
print(correct_text)

