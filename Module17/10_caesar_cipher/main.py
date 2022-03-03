alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = input('Введите сообщение:  ').lower()
step = int(input('Введите сдвиг: '))
secret_message = ''

for i_letter in message:
    if i_letter in alphabet:
        t = alphabet.find(i_letter)
        new_step = (t + step ) % len(alphabet)
        secret_message += alphabet[new_step]
    else:
        secret_message += i_letter
print('Зашифрованное сообщение:', secret_message)