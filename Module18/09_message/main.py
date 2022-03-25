message = input('Сообщение: ')
message_two = ''
correct_message = ''

for symbol in message:
    if symbol != ' ':
        if symbol.isalpha():
            message_two += symbol
        else:
            correct_message += message_two[::-1] + symbol
            message_two = ''
    else:
        correct_message += message_two[::-1] + symbol
        message_two = ''
print(correct_message)

