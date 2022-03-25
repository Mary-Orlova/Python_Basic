# Пароль- Минимум из 8 символов, в нём должна быть хотя бы одна большая буква и хотя бы 3 цифры

while True:
    password = input('Придумайте пароль: ')
    numbers = 0 #счетчик для цифр в пароле
    for symbol in password: #цикл для подсчета кол-ва цифр
        if symbol in '1234567890':
            numbers += 1
    if len(password) >= 8 and numbers >= 3 and not password.islower():
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадежный. Попробуйте еще раз')



