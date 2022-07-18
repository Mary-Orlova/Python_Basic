class Date:
    def __init__(self, *args) -> None:
        """Инициализация класса для вывода строки в формате даты
        Передаем в *args =self.day, self.month, self.year """
        self.day, self.month, self.year = args

    @classmethod
    def date_string(cls, str_date: str) -> tuple:
        """Метод возвращает кортежем строку в формате int без разделяющего знака '-'
         """
        return tuple(map(int, str_date.split('-')))

    @classmethod
    def from_string(cls, str_date: str) -> 'Date':
        """"Метод для работы со строкой-выводом
        Инструкция assert -это булевые выражения, которые проверяют, является ли условие истинным
        Если не является = выводится ошибка, что дата не верна указана
        Возвращается класс в заданной строке из основой программы

        """
        assert cls.is_date_valid(str_date), 'Дата не верна указана.'
        return cls(*cls.date_string(str_date))

    def __str__(self):
        """Метод вывода на экран в формате = День: N Месяц: N Год: N"""
        return 'День: %d Месяц: %d Год: %d' % (self.day, self.month, self.year)

    @classmethod
    def is_date_valid(cls, str_date: str) -> tuple:
        """Метод проверки корректности ввода даты"""
        day, month, year = cls.date_string(str_date)
        return 0 < day <= 31 and 0 < month <= 12 and year > 0


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
