class Human:
    def __init__(self, name, satiety=50):
        self.name = name
        self.satiety = satiety

    def eat(self, home):
        self.satiety += 5
        home.food -= 5

    def earn_money(self, home):
        self.satiety -= 15
        home.money += 50

    def play(self, satiety):
        self.satiety -= 10

    def go_grossery(self, home):
        home.food += 50
        home.money -= 35


class Home:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money
