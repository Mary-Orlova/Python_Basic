import random


class Human:
    def __init__(self, name, satiety=30, happy=100, summa_food=0):
        """Инициализация класса людей:
           -имя name
           -сытость satiety
           -счастье happy
           -кол-во съеденой еды summa_food
           """
        self.name = name
        self.satiety = satiety
        self.happy = happy
        self.summa_food = summa_food

    def eat(self, home):
        """Инициализация метода еды с помощью генерации random"""
        food = random.randint(25, 30)
        """Условие -если сгенерированный ур-нь еды выше или равен той, что дома:
        считать за кол-во еды максимальное кол-во еды из холодильника"""
        if food >= home.food:
            food = home.food
        """Повышение ур-ня сытости"""
        self.satiety += food
        """Снижение ур-ня еды в холодильнике"""
        home.food -= food
        """Подсчет съеденной еды"""
        self.summa_food += food

    def play_cat(self, cat):
        """Метод игры / гладить кота
        -увеличивает счастье на 5 единиц
        -понижает сытости человека и кота
        """
        self.happy += 5
        self.satiety -= 10
        cat.satiety -= 10


class Home:
    def __init__(self, food=50, money=0, dirt=0, cat_food=50):
        """Инициализация класса Дом:
        -еда для людей food
        -еда для кота cat_food
        -деньги money
        -грязь dirt
        """
        self.food = food
        self.money = money
        self.dirt = dirt
        self.cat_food = cat_food


class Man(Human):
    def __init__(self, name):
        """Инициализация муж
        присвоение имени self.name = 'Артём'
        """
        super().__init__(name)
        self.name = 'Артём'

    def play(self, satiety):
        """Метод игры в приставку/ компьютер
        -увеличение уровня счастья
        -снижение сытости - 10 пунктов"""
        self.satiety -= 10
        self.happy += 20

    def earn_money(self, home):
        """Метод работы
        -увеличение кол-ва денег
        -снижение ур-ня сытости
        """
        self.satiety -= 10
        home.money += 150


class Woman(Human):
    def __init__(self, name, amount_fur_coat=0):
        """Инициализация класса жен
        -присвоение имени
        -счетчик кол-ва купленых шуб
        """
        super().__init__(name)
        self.name = 'Агата'
        self.amount_fur_coat = amount_fur_coat

    def go_grossery(self, home):
        """Метод хождения за покупками(едой)
        -увеличение кол-ва еды для людей home.food
        -увеличение кол-ва еды для кота home.cat_food
        -уменьшение кол-ва денег home.money
        -снижение ур-ня сытости на 10 пунктов """
        home.food += 50
        home.cat_food += 20
        home.money -= 70
        self.satiety -= 10

    def go_shopping(self, home):
        """Метод покупки шубы
        -увеличение счастья
        -уменьшение денег
        -уменьшение сытости
        -увеличение счетчика покупки шуб
        """
        self.happy += 60
        home.money -= 350
        self.satiety -= 10
        self.amount_fur_coat += 1

    def cleaning(self, home):
        """Метод уборки дома
        -генерация чистоты
        -снижение ур-ня сытости"""
        clear = random.randint(1, 100)
        """Если сгенерированное число больше, чем грязи дома, то
        считаем уровень очищения за это число"""
        if clear > home.dirt:
            clear = home.dirt
        home.dirt -= clear
        self.satiety -= 10


class Cat:
    def __init__(self, name, satiety=30, summa_cat_food=0):
        """Инициалищация класса кота
        -имя name
        -уровень сытости satiety
        -счетчик потребляемой еды summa_cat_food
        """
        self.name = name
        self.satiety = satiety
        self.summa_cat_food = summa_cat_food

    def eat(self, home):
        """Метод потребления кошачьей еды котом
        -генератор еды для кота
        -уровень сытости увеличивается
        -уменьшение кошачьей еды дома"""
        food = random.randint(1, 10)
        """Если сгенерированное кол-во кошачьей еды больше,
        чем имеется - считаем максимальное число еды как ту, которую скармливаем"""
        if food > home.cat_food:
            food = home.cat_food
        self.satiety += food * 2
        self.summa_cat_food += food
        home.cat_food -= food

    def tear_wallpaper(self, home):
        """Метод кота - драть обои
        -увеличивает грязь в доме
        -снижает уровень сытости
        """
        home.dirt += 5
        self.satiety -= 10
