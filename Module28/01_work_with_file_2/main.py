from typing import Any


class File:

    def __init__(self, filename: str, regim: str) -> None:
        """Инициализация файла
        self.file_name - название файла из переданныз данных ('example.txt')
        self.regim - режим записи текста в файл
        self.file - обозначение, что файл не создан/отсутствует
        """
        self.file_name = filename
        self.regim = regim
        self.file = None

    def __enter__(self) -> 'File':
        """Метод открытия файла:
        Ввод данных - аналог функции open для открытия файла
        Присваиваем значение(команду) для self.file
        open(self.file_name, self.regim) - передаем название и режим файла
        Возвращаем созданный клас return self ('File')
        """
        self.file = open(self.file_name, self.regim)
        return self


    def write(self, text: Any) -> None:
        """Метод записи в файл"""
        try:
            """Пробуем записать текст в файл как есть"""
            self.file.write((text) + '\n')
        except BaseException:
            """Если вылезла ошибка -> приводим текст к формату str"""
            self.file.write(str(text) + '\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Метод - закрытие файла"""
        self.file.close()

with File('example.txt', 'w') as file:
    file.write([45])