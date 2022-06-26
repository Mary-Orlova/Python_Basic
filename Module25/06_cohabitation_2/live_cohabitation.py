import random


class Human:
    def __init__(self, name, satiety=30, happy=100, summa_food=0):
        """Инициализация класса людей:
           -имя name
           -сытость satiety
           -счастье happy
           -кол-во съеденой еды summa_food
           """
        self._name = name
        self._satiety = satiety
        self._happy = happy
        self._summa_food = summa_food
        self._is_alive = True

    def get_human(self):
        return self._name, self._satiety, self._happy, self._summa_food

    def set_eat(self, home):
        """Инициализация метода еды с помощью генерации random"""
        food = random.randint(25, 30)
        """Условие -если сгенерированный ур-нь еды выше или равен той, что дома:
        считать за кол-во еды максимальное кол-во еды из холодильника"""
        if food >= home._food:
            food = home._food
        """Повышение ур-ня сытости"""
        self._satiety += food
        """Снижение ур-ня еды в холодильнике"""
        home._food -= food
        """Подсчет съеденной еды"""
        self._summa_food += food

    def get_eat(self, home):
        return self._summa_food, self._satiety, home._food

    def set_play_cat(self, cat):
        """Метод игры / гладить кота
        -увеличивает счастье на 5 единиц
        -понижает сытости человека и кота
        """
        self._happy += 5
        self._satiety -= 10
        cat._satiety -= 10

    def get_play_cat(self, cat):
        return self._happy, self._satiety, cat._satiety


class Home:
    def __init__(self, food=50, money=0, dirt=0, cat_food=50):
        """Инициализация класса Дом:
        -еда для людей food
        -еда для кота cat_food
        -деньги money
        -грязь dirt
        """
        self._food = food
        self._money = money
        self._dirt = dirt
        self._cat_food = cat_food

    def get_home(self):
        return self._food, self._money, self._dirt, self._cat_food


class Man(Human):
    def __init__(self, name, satiety=30, happy=100, summa_food=0):
        """Инициализация муж
        присвоение имени self.name = 'Артём'
        """
        super().__init__(name)
        self._name = name
        self._satiety = satiety
        self._happy = happy
        self._summa_food = summa_food

    def get_human(self):
        return self._name, self._satiety, self._happy, self._summa_food

    def set_play(self):
        """Метод игры в приставку/ компьютер
        -увеличение уровня счастья
        -снижение сытости - 10 пунктов"""
        self._satiety -= 10
        self._happy += 20

    def get_play(self):
        return self._satiety, self._happy

    def set_earn_money(self, home):
        """Метод работы
        -увеличение кол-ва денег
        -снижение ур-ня сытости
        """
        self._satiety -= 10
        home._money += 150

    def get_earn_money(self, home):
        return self._satiety, home._money


class Woman(Human):
    def __init__(self, name, amount_fur_coat=0):
        """Инициализация класса жен
        -присвоение имени
        -счетчик кол-ва купленых шуб
        """
        super().__init__(name)
        self.name = name
        self._amount_fur_coat = amount_fur_coat

    def get_human(self):
        return self._name, self._amount_fur_coat

    def set_go_grossery(self, home):
        """Метод хождения за покупками(едой)
        -увеличение кол-ва еды для людей home.food
        -увеличение кол-ва еды для кота home.cat_food
        -уменьшение кол-ва денег home.money
        -снижение ур-ня сытости на 10 пунктов """
        home._food += 130
        home._cat_food += 20
        home._money -= 150
        self._satiety -= 10

    def get_go_grossery(self, home):
        return home._food, home._cat_food, home._money, self._satiety

    def set_go_shopping(self, home):
        """Метод покупки шубы
        -увеличение счастья
        -уменьшение денег
        -уменьшение сытости
        -увеличение счетчика покупки шуб
        """
        self._happy += 60
        home._money -= 350
        self._satiety -= 10
        self._amount_fur_coat += 1

    def get_go_shopping(self, home):
        return self._happy, home._money, self._satiety, self._amount_fur_coat

    def cleaning(self, home):
        """Метод уборки дома
        -генерация чистоты
        -снижение ур-ня сытости"""
        clear = random.randint(1, 100)
        """Если сгенерированное число больше, чем грязи дома, то
        считаем уровень очищения за это число"""
        if clear > home._dirt:
            clear = home._dirt
        home._dirt -= clear
        self._satiety -= 10

    def get_cleaning(self, home):
        return self._satiety, home._dirt


class Cat:
    def __init__(self, name, satiety=30, summa_cat_food=0):
        """Инициалищация класса кота
        -имя name
        -уровень сытости satiety
        -счетчик потребляемой еды summa_cat_food
        """
        self._name = name
        self._satiety = satiety
        self._summa_cat_food = summa_cat_food
        self._is_alive = True

    def get_cat(self):
        return self._name, self._satiety, self._summa_cat_food

    def set_eat(self, home):
        """Метод потребления кошачьей еды котом
        -генератор еды для кота
        -уровень сытости увеличивается
        -уменьшение кошачьей еды дома"""
        food = random.randint(1, 10)
        """Если сгенерированное кол-во кошачьей еды больше,
        чем имеется - считаем максимальное число еды как ту, которую скармливаем"""
        if food > home._cat_food:
            food = home._cat_food
        self._satiety += food * 2
        self._summa_cat_food += food
        home._cat_food -= food

    def get_eat(self, home):
        return self._satiety, self._summa_cat_food, home._cat_food

    def set_tear_wallpaper(self, home):
        """Метод кота - драть обои
        -увеличивает грязь в доме
        -снижает уровень сытости
        """
        home._dirt += 5
        self._satiety -= 10

    def get_tear_wallpaper(self, home):
        return home._dirt, self._satiety
