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
        home._dirt += 5
        human = random.choice([human_1, human_2])

        if human._satiety < 0 or cat._satiety < 0:
            if cat._satiety < 0:
                cat._is_alive = False
                print('Увы, не уследили за котиком - {} умер'.format(cat._name))
                raise ValueError
            else:
                print('\nНеудача.....Сытость у домочадца {} < 0, жизнь обовалась!'.format(human._name))
                human._is_alive = False
                raise ValueError
        elif human_1._satiety < 20:
            print('\nВнимание сытость стала < 20.')
            human_1.set_eat(home)
            human_1.get_eat(home)
            print('{} ест. Сытость: {}, еда в холодильнике: {}.'.format(human_1._name, human_1._satiety, home._food))
        elif human_2._satiety < 20:
            print('\nВнимание сытость стала < 20.')
            human_2.set_eat(home)
            human_2.get_eat(home)
            print('{} ест. Сытость: {}, еда в холодильнике: {}.'.format(human_2._name, human_2._satiety, home._food))
        elif cat._satiety < 20:
            print('Внимание кот голодный! Сытость < 20.')
            cat.set_eat(home)
            cat.get_eat(home)
            print('Кот {} ест. Cытость: {}, кошачья еда: {}'.format(cat._name, cat._satiety, home._cat_food))
        elif home._food < 30 or home._cat_food < 30:
            print('\nВ холодильнике еды < 10.')
            human_2.set_go_grossery(home)
            human_2.get_go_grossery(home)
            print('{} закупается продуктами. Осталось: {} долларов, теперь еды: {}, у кота {}.'.format(
                human_2._name, home._money, home._food, home._cat_food))
        elif home._money < 50:
            print('\nДенег < 50, а именно сейчас на тумбе {} долларов.'.format(home._money))
            human_1.set_earn_money(home)
            human_1.get_earn_money(home)
            print('{} уже на работе. Заработано {} долларов, сытость снизилась до {}.'.format(
                human_1._name, home._money, human_1._satiety))
        elif home._dirt > 90:
            human_1._satiety -= 10
            human_2._satiety -= 10
            print('{} сделал уборку, грязь дома: {}, сытость: {}'.format(human_2._name, home._dirt, human_2._satiety))
        elif human_1._happy < 10 or human_2._happy < 10:
            print('Человек умер от депрессии!')
        day += 1

        if cube == 1:
            human_1.set_earn_money(home)
            human_1.get_earn_money(home)
            print('Кубик выпал с гранью = 1, {} уходит на работу за 150 $.'.format(human_1._name))
            print('Теперь денег: {} долларов, сытость: {}.\n'.format(home._money, human_1._satiety))
        elif cube == 2:
            if home._food <= 20:
                human_2.set_go_grossery(home)
                human_2.get_go_grossery(home)
                print('{} отправилась за продуктами, еда: {}, кошачья еда: {}\n'.format(
                    human_2._name, home._food, home._cat_food))
            else:
                human.set_eat(home)
                human.get_eat(home)
                print('Кубик выпал с гранью = 2, {} идёт есть.'.format(human._name))
                print('Сытость: {}, еда в холодильнике: {}.\n'.format(human._satiety, home._food))
        elif cube == 3:
            if home._money >= 350:
                human_2.set_go_shopping(home)
                human_2.get_go_shopping(home)
                cat.set_tear_wallpaper(home)
                cat.get_tear_wallpaper(home)
                print('Кубик выпал с гранью 3 - жена покупает шубу')
                print('Потрачено 350 $, уровень счастья: {}\n'.format(human_2._happy))
                print('Кот дерет обои, уровень грязи: {}'.format(home._dirt))
            else:
                if human_1._satiety < 20:
                    cube = 2
                else:
                    human_1.set_eat(home)
                    human_1.get_eat(home)
                    human_1.set_earn_money(home)
                    human_1.get_earn_money(home)
                    print('Жена хочет купить шубу, денег не хватает, {} поел и сходил на работу, еда: {},'
                          ' сытость: {}, деньги: {} $\n'.format(human_1._name, home._food, human_1._satiety, home._money))
        elif cube == 4:
            human.set_play_cat(cat)
            human.get_play_cat(cat)
            print('{} гладит котика, сытость = {}, сытость котика: {}.\n'.format(
                human._name, human._satiety, cat._satiety))
        elif cube == 5:
            if human_2._satiety <= 20:
                cube = 2
            else:
                human_2.cleaning(home)
                print('{} убралась дома, грязь: {}, сытость: {}\n'.format(human_2._name, home._dirt, human_2._satiety))
        elif cube == 6:
            human_1.set_play()
            human_1.get_play()
            print('Выпал кубик с гранию 6, {} играет и наслаждается, сытость = {}.\n'.format(
                human_1._name, human_1._satiety))

except ValueError:
    print('Удалось прожить {}'.format(day))
    print('Вас постигла неудача. Попробуйте еще раз.')

else:
    print('Прожили {} дней, съедено еды людьми: {}, котом: {}, куплено шуб: {} '.format(
        day, human_1._summa_food + human_2._summa_food, cat._summa_cat_food, human_2._amount_fur_coat))
    print('=' * 5, 'Эксперимент удался. Выжили!', '=' * 5)
