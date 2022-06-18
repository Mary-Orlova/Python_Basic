import random


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
            raise ValueError('Ошибка в очках кармы!')

    def one_day(self):
        """ Информация о номере дня и обработка исключений """
        print('Сегодня заработано: {} оч. кармы'.format(self.__karma_day))
        if self.__sudden_exception == 1 or self.__sudden_exception == 6:
            try:
                raise BaseException("KillError")
            except BaseException as exc:
                print(f'Исключение класса - {type(exc)}  | параметры {exc.args}')
                with open('karma_log', 'a') as karma_log:
                    karma_log.write(f'{type(exc)} {exc.args}\n')

        if self.__sudden_exception == 2 or self.__sudden_exception == 7:
            try:
                raise BaseException("DrunkError")
            except BaseException as exc:
                print(f'Исключение класса - {type(exc)}')
                with open('karma_log', 'a') as karma_log:
                    karma_log.write(str(f'{type(exc)} {exc.args}\n'))

        if self.__sudden_exception == 3 or self.__sudden_exception == 8:
            try:
                raise BaseException("CarCrashError")
            except BaseException as exc:
                print(f'Исключение класса - {type(exc)}  | параметры {exc.args}')
                with open('karma_log', 'a') as karma_log:
                    karma_log.write(str(f'{type(exc)} {exc.args}\n'))

        if self.__sudden_exception == 4 or self.__sudden_exception == 9:
            try:
                raise BaseException("GluttonyError")
            except BaseException as exc:
                print(f'Исключение класса - {type(exc)}  | параметры {exc.args}')
                with open('karma_log', 'a') as karma_log:
                    karma_log.write(str(f'{type(exc)} {exc.args}\n'))

        if self.__sudden_exception == 5 or self.__sudden_exception == 10:
            try:
                raise BaseException("DepressionError")
            except BaseException as exc:
                print(f'Исключение класса - {type(exc)}  | параметры {exc.args}')
                with open('karma_log', 'a') as karma_log:
                    karma_log.write(str(f'{type(exc)} {exc.args}\n'))

        return self.__karma_day


all_karma = 0
MAX_KARMA = 500
day = 1

while True:
    print('Прошел день № {}\nОбщее кол-во кармы: {}\n'.format(day, all_karma))
    if all_karma < MAX_KARMA:
        all_karma += Karma.one_day(Karma())
        day += 1
    else:
        break
