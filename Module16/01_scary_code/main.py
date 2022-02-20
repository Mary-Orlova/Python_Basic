basic_list = [1, 5, 3]
first_add = [1, 5, 1, 5]
second_add = [1, 3, 1, 5, 3, 3]

basic_list.extend(first_add)
print('Кол-во цифр 5 при первом объединении:',basic_list.count(5))
for _ in range(basic_list.count(5)):
    basic_list.remove(5)
basic_list.extend(second_add)
print('Кол-во цифр 4 при втором объединении:',basic_list.count(3))
print('Итоговый список',basic_list)
