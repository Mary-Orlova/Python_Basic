import random

max_number = int(input('Введите максимальное число: '))
secret_number = random.randint(0,max_number)
secret_number = str(secret_number)
print(secret_number)
result = set()

print('\nВведите несколько чисел через пробел, которые Вы считаете мог загадать Артём')
count = 0

while True:
    answer = input('\nНужное число есть среди вот этих чисел: ')
    if secret_number in answer:
        print('Ответ Артёма: Да')
        if secret_number == answer:
            print('Угадал!')
            break
        for _ in range(len(answer)):
            result.add(answer[_])
    elif answer == secret_number:
        print('Верно')
        break
    elif answer == 'Помогите!':
        print('Артём мог загадать следующие числа: ', result)
    else:
        print('Ответ Артёма: Нет')
        for _ in range(len(answer)):
            result.discard(answer[_])







