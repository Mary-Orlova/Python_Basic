class Property:

    def __init__(self, worth):
        """ Расчет налогов на имущество """
        self.set_worth(worth)

    def tax(self):
        pass

    def get_worth(self):
        """Возврат стоимости после проверки"""
        return self.__worth

    def set_worth(self, worth):
        """Проверка на внесенную стоимость - не должна быть меньше 0 """
        if worth > 0:
            self.__worth = worth
        else:
            raise ValueError('Ошибка в стоимости')


class Apartment(Property):
    """ Инициализация стоимости под-класса квартиры Apartment от родительского класса Property"""
    def __init__(self, worth):
        super().__init__(worth)
        self.__worth = worth

    def tax(self):
        """ Расчет налога """
        return self.__worth / 1000


class Car(Property):
    """ Инициализация под-класса Car от родительского класса Property"""
    def __init__(self, worth):
        """Внесение стоимости под - класа """
        super().__init__(worth)
        self.__worth = worth

    def tax(self):
        """Расчет ставки налога для класса Car"""
        return self.__worth / 200


class CountryHouse(Property):
    """ Инициализация под-класса CountryHouse от родительского класса Property"""
    def __init__(self, worth):
        super().__init__(worth)
        self.__worth = worth

    def tax(self):
        """Расчет ставки налога для класса CountryHouse"""
        return self.__worth / 500


amount_money = float(input('Количество имеющихся денег: '))

wroth_1 = float(input('Стоимость квартиры: '))
nalog_apartment = Apartment(wroth_1)
print('Налог на квартиру {}'.format(nalog_apartment.tax()))

wroth_2 = float(input('Стоимость машины: '))
nalog_car = Car(wroth_2)
print('Налог на машину {}'.format(nalog_car.tax()))

wroth_3 = float(input('Дача: '))
nalog_contrhous = CountryHouse(wroth_3)
print('Налог на дачу {}'.format(nalog_contrhous.tax()))

summa_nalog = nalog_apartment.tax() + nalog_car.tax() + nalog_contrhous.tax()

if amount_money - summa_nalog > 0:
    result = amount_money - summa_nalog
    print('Общий налог: {}\nДенег хватает(у Вас в наличие): {}'.format(summa_nalog, amount_money))
    print('Заплатив налог у вас останется: {}'.format(result))
else:
    print('Общий налог: {}\nДенег не хватает на уплату налога'.format(summa_nalog))
