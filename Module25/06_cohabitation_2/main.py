import random
from live_cohabitation import Man, Woman, Cat
from live_cohabitation import Home


human_1 = Man('Артём')
human_2 = Woman('Агата')
cat = Cat('Васька')
home = Home()
day = 0


try:
    while day < 366:
        cube = random.randint(1, 6)
        home.dirt += 5
        human = random.choice([human_1, human_2])

        if human.satiety < 0 or cat.satiety < 0:
            if cat.satiety < 0:
                print('Увы, не уследили за котиком - {} умер'.format(cat.name))
            else:
                print('\nНеудача.....Сытость у домочадца {} < 0, жизнь обовалась!'.format(human.name))
            raise ValueError
        elif human_1.satiety < 20:
            print('\nВнимание сытость стала < 20.')
            human_1.eat(home)
            print('{} ест. Сытость: {}, еда в холодильнике: {}.'.format(human_1.name, human_1.satiety, home.food))
        elif human_2.satiety < 20:
            print('\nВнимание сытость стала < 20.')
            human_2.eat(home)
            print('{} ест. Сытость: {}, еда в холодильнике: {}.'.format(human_2.name, human_2.satiety, home.food))
        elif cat.satiety < 20:
            print('Внимание кот голодный! Сытость < 20.')
            cat.eat(home)
            print('Кот {} ест. Cытость: {}, кошачья еда: {}'.format(cat.name, cat.satiety, home.cat_food))
        elif home.food < 30 or home.cat_food < 30:
            print('\nВ холодильнике еды < 10.')
            human_2.go_grossery(home)
            print('{} закупается продуктами. Осталось: {} долларов, теперь еды: {}, а у кота {}.'
                  .format(human_2.name, home.money, home.food, home.cat_food))
        elif home.money < 50:
            print('\nДенег < 50, а именно сейчас на тумбе {} долларов.'.format(home.money))
            human_1.earn_money(home)
            print('{} уже на работе. Заработано {} долларов, сытость снизилась до {}.'
                  .format(human_1.name, home.money, human_1.satiety))
        elif home.dirt > 90:
            human_1.satiety -= 10
            human_2.satiety -= 10
            print('{} сделал уборку, грязь дома: {}, сытость: {}'.format(human_2.name, home.dirt, human_2.satiety))
        elif human_1.happy < 10 or human_2.happy < 10:
            print('Человек умер от депрессии!')
        day += 1

        if cube == 1:
            human_1.earn_money(home)
            print('Кубик выпал с гранью = 1, {} уходит на работу за 150 $.'.format(human_1.name))
            print('Теперь денег: {} долларов, сытость снизилась до {}.'.format(home.money, human_1.satiety))
        elif cube == 2:
            human.eat(home)
            print('Кубик выпал с гранью = 2, {} идёт есть.'.format(human.name))
            print('Сытость: {}, еда в холодильнике: {}.'.format(human.satiety, home.food))
        elif cube == 3:
            if home.money >= 350:
                human_2.go_shopping(home)
                print('Кубик выпал с гранью 3 - жена покупает шубу')
                print('Потрачено 350 $, уровень счастья: {}'.format(human_2.happy))
            else:
                human_1.eat(home)
                human_1.earn_money(home)
                print('{} поел и сходил на работу, теперь {} $'.format(human_1.name, home.money))
        elif cube == 4:
            human.play_cat(cat)
            print('{} гладит котика, сытость = {}, сытость котика: {}.'.format(human.name, human.satiety, cat.satiety))
        elif cube == 5:
            human_2.cleaning(home)
            print('{} убралась дома, грязь: {}, сытость: {}'.format(human_2.name, home.dirt, human_2.satiety))
        elif cube == 6:
            human_1.play(human_1.satiety)
            print('Выпал кубик с гранию 6, {} играет и наслаждается, сытость = {}.'.format(
                human_1.name, human_1.satiety))

except ValueError:
    print('Удалось прожить {}'.format(day))
    print('Вас постигла неудача. Попробуйте еще раз.')

else:
    print('Прожили {} дней, съедено еды людьми: {}, котом: {}, куплено шуб: {} '.format(
        day, human_1.summa_food + human_2.summa_food, cat.summa_cat_food, human_2.amount_fur_coat))
    print('=' * 5, 'Эксперимент удался. Выжили!', '=' * 5)
