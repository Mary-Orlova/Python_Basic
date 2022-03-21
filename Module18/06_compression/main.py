text = input('Введите строку: ')
correct_text = ''
count = 1

for i_sym in range(len(text)-1):
    if text[i_sym] == text[i_sym + 1]:
       count +=1
    elif text[i_sym] != text[i_sym+1] or i_sym == len(text) - 2:
        correct_text += text[i_sym] + str(count)
        count = 1

if text[-2] != text[-1]:
    correct_text += text[-1] + '1'
print(correct_text)

