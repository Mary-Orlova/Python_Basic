diaposon = int(input('Кол-во чисел: '))
num_list = []

for i_num in range(diaposon):
    i_num = 0
    num = int(input('Число: '))
    num_list.append(num)
print('Последовательность: ', num_list)

while num_list != num_list[::-1]:
    num_list.insert(diaposon, num_list[i_num])
    i_num  += 1
print('Нужно приписать чисел: ',i_num)
print('Сами числа:',num_list[:i_num ][::-1])
