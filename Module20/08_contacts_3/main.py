phonebook = dict()
print('Текущие контакты на телефоне:\n<Пусто>')

while True:
    choose = int(input('Введите номер действия: 1-добавить контакт; 2-найти человека: '))
    if choose == 1:
        name = tuple(input('Введите имя и фамилию: ').split())
        if name in phonebook:
            print('Ошибка. Такой контакт уже существует')
        else:
            numbers = int(input('Введите номер телефона: '))
            phonebook[name] = numbers
            print('\nТекущие контактные на телефоне: ')
            for _ in phonebook:
                print(_,phonebook[_])
    elif choose == 2:
        surname = input('Введите фамилию для поиска: ')
        for person in phonebook:
            if surname in person:
                print(person[0],person[1],phonebook[person])
    else:
        print('Ошибка ввода')
