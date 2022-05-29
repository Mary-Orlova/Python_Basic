sym_sum, line_count = 0, 0

with open('people.txt', 'r') as people_file:
    for line in people_file:
        try:
            lenght = len(line)
            line_count += 1
            if line.endswith('\n'):
                lenght -= 1
            sym_sum += lenght
            if lenght < 3:
                print('Ошибка: менее трёх символов в строке {} строке'.format(line_count))
                raise BaseException
        except FileNotFoundError:
            print('Файл не найден')
        except BaseException:
            with open('error.log', 'w') as error_file:
                error_file.write('Ошибка: менее трёх символов в строке {} строке'.format(line_count))

print('Общее количество символов:', sym_sum)

