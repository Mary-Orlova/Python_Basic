import random
from Human_and_home import Human
from Human_and_home import Home


human_1 = Human('Артём')
human_2 = Human('Тома')
human_3 = Human('Вася')
home = Home()
day = 1


try:
    while day < 366:
        cube = random.randint(1, 6)
        day += 1
        human = random.choice([human_1, human_2, human_3])

        if human.satiety < 0:
            print('\nНеудача.....Сытость у домочадца {} < 0, жизнь обовалась!'.format(human.name))
            raise ValueError
        elif human.satiety < 20:
            print('\nВнимание сытость стала < 20.')
            human.eat(home)
            print('{} ест. Сытость: {}, еда в холодильнике: {}.'.format(human.name, human.satiety, home.food))
        elif home.food < 10:
            print('\nВ холодильнике еды < 10.')
            human.go_grossery(home)
            print('{} закупается продуктами. Осталось: {} долларов, куплено: {} еды.'
                  .format(human.name, home.money, home.food))
        elif home.money < 50:
            print('\nДенег < 50, а именно сейчас на тумбе {} долларов.'.format(home.money))
            human.earn_money(home)
            print('{} уже на работе. Заработано {} долларов, сытость снизилась до {}.'
                  .format(human.name, home.money, human.satiety))

        if cube == 1:
            human.earn_money(home)
            print('Кубик выпал с гранью = 1, {} уходит на работу.'.format(human.name))
            print('Заработано {} долларов, сытость снизилась до {}.'.format(home.money, human.satiety))
        elif cube == 2:
            human.eat(home)
            print('Кубик выпал с гранью = 2, {} идёт есть.'.format(human.name))
            print('Сытость: {}, еда в холодильнике: {}.'.format(human.satiety, home.food))
        elif cube in [3, 4, 5, 6]:
            human.play(human.satiety)
            print('{} играет и наслаждается, сытость = {}.'.format(human.name, human.satiety))

except ValueError:
    print('Вас постигла неудача. Попробуйте еще раз.')

else:
    print('=' * 5, 'Эксперимент удался. Выжили!', '=' * 5)
