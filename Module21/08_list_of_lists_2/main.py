def get_open_list(right_list): #получить открытые список(прямой список)
    if right_list == []: #когда прямой список является пустым списком
        return right_list #вернуть прямой список
    if isinstance(right_list[0], list): #является ли 1элемент списка-вложенным списком
        return(get_open_list(right_list[0]) + get_open_list(right_list[1:])) #целиком передать ф-ии в кач-ве аргумента+ ост.часть осн.списка
    return(right_list[:1] + get_open_list(right_list[1:])) #до первого элемента и вызвать ф-цию передав прямой список с 1 элемента

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print('Выпрямленный список: ', get_open_list(nice_list))
