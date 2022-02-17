def friends_list():
    for i_friend in range(count_friends):
        friends.append(0)
    receipt()

def receipt():
    for i in range(credits):
        print(i+1,'расписка')
        bank = int(input('Кому: ')) #кому должен
        borrower = int(input('От кого: '))  # должник
        money = int(input('Сколько: '))
        friends[borrower - 1] += money
        friends[bank - 1] -= money
        print()
    balance()

def balance():
    print('Баланс друзей: ')
    for index in range(len(friends)):
        print(index + 1, ": ", friends[index])

count_friends = int(input('Кол-во друзей: '))
friends = []
credits = int(input('Кол-во долговых расписок: '))
friends_list()