from random import shuffle


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        """Возращает количество очков которое дает карта"""
        if self.rank in ["10", "валет", "дама", "король", "туз"]:
            # TJQKA 10 очков за 10, валетаJ, дамуD и короляQ и тузA
            return 10
        else:
            return "0123456789".index(self.rank)  # число очков = цифре

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Player(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        """ Функция добавление карты в руку"""
        self.cards.append(card)

    def get_value(self):
        """ Метод получения числа очков на руке """
        result = 0
        aces = 0  # туз
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == "туз":
                aces += 1
            # туз идет за -11 очков пока общая сумма не больше 21, далее 1)
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = "\n{} держит в руке:\n".format(self.name)
        for card in self.cards:
            text += str(card) + "; "
        text += "\nСумма очков: " + str(self.get_value())
        return text


class Deck(object):
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "валет", "дама", "король", "туз"]  # ранги "23456789TJQKA"
        suits = [" бубен", " треф", " червей", " пик"]  # масти бубны-трефы-черви-пики
        self.cards = [Card(r, s) for r in ranks for s in suits]  # генератор создающий колоду из 52карт
        shuffle(self.cards)  # перетасовать колоду

    def deal_card(self):
        """ Функция сдачи карты """
        return self.cards.pop()
