number_file = open('numbers.txt', 'r')
numbers = number_file.read().split()
summa = 0

for line in numbers:
    summa += int(line)
print('Сумма чисел: ', summa)
number_file.close()

answer_file = open('answer.txt', 'w')
answer_file.write(str(summa))
answer_file.close()
