message = input('Сообщение: ')
message_2 = ''
correct_message = ''

for symbol in message:
    if symbol != ' ':
        if symbol.isalpha():
            message_2 += symbol
        else:
            correct_message += message_2[::-1] + symbol
            message_2 = ''
    else:
        correct_message += message_2[::-1] + symbol
        message_2 = ''
print(correct_message)

