import math
import random


class Car:
    """Создание основного класса Car"""
    def __init__(self, x, y, corner):
        """Инициализация точек Х, Y и угла {corner}"""
        self.__x = x
        self.__y = y
        self.__corner = corner

    def move(self, dist):
        """Метод для вычисления точек Х, Y"""
        self.__x = self.__x + dist * math.cos(self.__corner)
        self.__y = self.__y + dist * math.sin(self.__corner)


class Bus(Car):
    """Создание под-класса от родительского Car"""
    """Константы:
    -ставка за проезд (коэффициент) = {PAY}
    -вместимость автобуса (максимальное кол-во пассажиров) = {MAX_PASSENGERS}
    """
    PAY = 0.01
    MAX_PASSENGERS = 60

    def __init__(self, x, y, direction):
        """Инициализация пассажиров и денег (в начале 0)"""
        super().__init__(x, y, direction)
        self.__passengers = 0
        self.__money = 0

    def move(self, distance):
        """Перезапись метода для расчета денег за проезд - учитывается коэфф оплаты + кол-во пассажиров + дистанция"""
        self.__money += Bus.PAY * self.__passengers * distance
        super().move(distance)

    def enter(self):
        """Метод для генерации и инициализации входа пассажиров в автобус, а так же предупреждение и действия,
         если будет автобус заполнен"""
        print('В автобусе: ', self.__passengers)
        new_passengers = random.randint(30, 60)
        if self.__passengers + new_passengers > Bus.MAX_PASSENGERS:
            print('Собираются войти:', new_passengers)
            print('Достигнута максимальная вместимость автобуса')
            print('Уехать смогли: {:d}'.format(Bus.MAX_PASSENGERS - self.__passengers))
            print('Остались {:d}'.format(new_passengers - (Bus.MAX_PASSENGERS - self.__passengers)))
            passengers = Bus.MAX_PASSENGERS - self.__passengers
        else:
            print('В автобус вошли: ', new_passengers)
            self.__passengers += new_passengers
        return self.__passengers

    def exit(self):
        """Метод для генерации и инициализации выхода пассажиров из автобуса"""
        out_passengers = random.randint(0, self.__passengers)
        print('Из автобуса вышли: ', out_passengers)
        if out_passengers > self.__passengers:
            passengers = self.__passengers
        self.__passengers -= out_passengers
        return self.__passengers

    def __str__(self):
        """Вывод информации строкой о кол-ве пассажиров в автобусе и денег у водителя"""
        lines = [
            f'В автобусе осталось: {self.__passengers}',
            f'У водителя: {round(self.__money, 2)} денег\n',
        ]
        return '\n'.join(lines)
