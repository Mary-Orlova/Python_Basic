def change():
    print('Сейчас на вечеринке', len(guests),'человек', guests)
    action = input('Гость пришел или ушёл? ')
    if action == 'пришел' or action == 'ушел':
        party(action)
    elif action == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
    else:
        print('Ошибка команды. Выберите: пришел, ушел, пора спать')
        change()

def party(action):
    name = input('Имя гостя: ')
    if action == 'ушел':
        if name in guests:
            guests.remove(name)
            print('Пока,', name)
        else:
            print('Проверьте имя гостя')
            party(action)
    elif action == 'пришел':
        if len(guests) < 6:
            guests.append(name)
            print('Привет,', name, '!')
        else:
            print('Прости,', name, ', но мест нет.')
    change()

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
change()




