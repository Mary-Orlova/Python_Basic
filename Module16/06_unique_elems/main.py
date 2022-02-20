
def first():
    print('Введите в первый список 3 числа.')
    for i_num in range(3):
        print('Введите',i_num + 1,'число для первого списка: ', end='')
        num = int(input())
        num_first.append(num)
    second()

def second():
    print('\nВведите во второй список 7 чисел.')
    for i_number in range(7):
        print('Введите', i_number + 1, 'число для второго списка: ', end='')
        num = int(input())
        num_second.append(num)
    result()

def result():
    print('\nПервый список: ', num_first)
    print('Второй списко: ', num_second)
    num_first.extend(num_second)
    print('Новый первый список с уникальными элементами: ', set(num_first))

num_first = []
num_second =[]

first()

#В примере уникальные элементы - [4, 6, 3, 2, 1] -как будто с конца списка
#А у меня в результате - [1, 2, 3, 4, 6]