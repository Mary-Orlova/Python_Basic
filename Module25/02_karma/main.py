import random

class KillError(BaseException):
    pass


class DrunkError(BaseException):
    pass


class CarCrashError(BaseException):
    pass


class GluttonyError(BaseException):
    pass


class DepressionError(BaseException):
    pass


class Karma:

    def __init__(self):
        """ Инициация: дней кармы __karma_day
            вероятности случайного исключения __sudden_exception
        """
        self.__karma_day = random.randint(1, 7)
        self.__sudden_exception = random.randint(1, 10)

    def get_karma_day(self):
        """Возврат дневных очков кармы """
        return self.__karma_day

    def get_sudden_exception(self):
        """Возврат сгененированного вероятности случайного исключения"""
        return self.__sudden_exception

    def set_karma_day(self, karma_day):
        """ Проверка дневных очков кармы """
        if karma_day > 0 and karma_day < 7:
            self.__karma_day = karma_day
        else:
            raise ValueError('Ошибка в очках кармы!')

    def set_sudden_exception(self, sudden_exception):
        """ Проверка случайного исключения """
        if sudden_exception > 0 and sudden_exception < 11:
            self.__sudden_exception = sudden_exception
        else:
            raise ValueError('Ошибка!')

    def one_day(self):
        """ Информация о номере дня и обработка исключений """
        print('Сегодня заработано: {} оч. кармы'.format(self.__karma_day))
        return self.__karma_day
        # return self.__karma_day, self.__sudden_exception


karma = Karma()
all_karma = 0
MAX_KARMA = 500
day = 1

while True:
    print('Прошел день № {}\nОбщее кол-во кармы: {}\n'.format(day, all_karma))
    if all_karma < MAX_KARMA:
        all_karma += Karma.one_day(Karma())
        try:
            if Karma.get_sudden_exception(Karma()) == 1 or Karma.get_sudden_exception(Karma()) == 6:
                raise BaseException("KillError")
            elif Karma.get_sudden_exception(Karma()) == 2 or Karma.get_sudden_exception(Karma()) == 7:
                raise BaseException("DrunkError")
            elif Karma.get_sudden_exception(Karma()) == 3 or Karma.get_sudden_exception(Karma()) == 8:
                raise BaseException("CarCrashError")
            elif Karma.get_sudden_exception(Karma()) == 4 or Karma.get_sudden_exception(Karma()) == 9:
                raise BaseException("GluttonyError")
            elif Karma.get_sudden_exception(Karma()) == 5 or Karma.get_sudden_exception(Karma()) == 10:
                raise BaseException("DepressionError")
        except BaseException as exc:
            print('|Поймана ошибка|')
            with open('karma_log', 'a') as karma_log:
                karma_log.write(str(f'{type(exc)} {exc.args}\n'))
        day += 1
    else:
        break
