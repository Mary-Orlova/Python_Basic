def find_result(line): #тут находим результат действия
    split_text = line.split(' ', 2)
    if len(split_text) == 3:
        operand_one, action, operand_two  = split_text
        operand_one, operand_two = int(operand_one), int(operand_two)
        if action == '+':
            result_line = operand_one + operand_two
        elif action == '-':
            result_line = operand_one - operand_two
        elif action == '/':
            result_line = operand_one / operand_two
        elif action == '*':
            result_line = operand_one * operand_two
        result.append(result_line)
    else:
        raise ValueError('НЕ присутствуют все три поля')

    return True

result = []

with open('calc.txt','r') as text:
    for line in text.read().splitlines():
        try:
            find_result(line)
        except Exception as error:
            print('Обнаружена ошибка в строке: ', line, end=' ')
            choise = input('Хотите исправить? ').lower()
            if choise == 'да':
                line = input('Введите исправленную строку: ')
                find_result(line)


print(sum(result))