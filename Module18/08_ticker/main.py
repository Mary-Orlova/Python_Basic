line = input('Первая строка: ')
line_second = input('Вторая строка: ')
count = 1

if line == line_second:
    print('Строки одинаковые')

else:
    flag = False
    for i in range(len(line_second)-1):
        line_2 = line_2[-1] + line_2[:-1]
        if line_2 == line:
            flag = True
            print('Первая строка получается из второй со сдвигом',count)
            break
        else:
            count += 1
    if not flag:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')