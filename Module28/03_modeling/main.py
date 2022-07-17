from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, figure_name: str) -> None:
        """Инициализация базового/родительского класса фигуры Figure
        self.figure_name  - имя объекта фигура
        """
        self.figure_name = figure_name

    @abstractmethod
    def __str__(self: str) -> str:
        """Метод - вывод показать имя фигуры"""
        return self.figure_name


class Square(Figure):
    def __init__(self, side: int) -> None:
        """Инициализация дочернего класса квадрат Square от Figure
        присваивание имени объекта "Квадрат"
        self.side = side Сторона квадрата из переданного значения осн.программы
        """
        super().__init__('Квадрат')
        self.__side = side

    def __str__(self: str) -> str:
        """Метод - вывод показать имя фигуры"""
        return self.figure_name

    @property
    def side(self) -> int:
        """Геттер для стороны квадрата - возвращает значение"""
        return self.__side

    @side.setter
    def side(self, side: int) -> None:
        """Сеттер для проверки нового значения стороны квадрата"""
        if side > 0:
            self.__side = side
        else:
            raise ValueError('Ошибка, сторона квадрата не может быть меньше 0.')

    def square(self) -> int:
        """Метод расчета площади поверхности квадрата"""
        return self.__side ** 2

    def perimeter(self) -> int:
        """"Метод расчета периметра квадрата"""
        return 4 * self.__side


class Triangle(Figure):
    def __init__(self, side_one, side_two, side_three):
        """Инициализация дочернего класса треугольник Triangle от Figure
        стороны треугольника
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        """
        super().__init__('Треугольник')
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three

    def __str__(self: str) -> None:
        """Метод - вывод показать имя фигуры"""
        print(self.figure_name)

    @property
    def side(self) -> tuple:
        """Геттер для сторон треугольника"""
        return self.side_one, self.side_two, self.side_three

    @side.setter
    def side(self, side_one, side_two, side_three) -> None:
        """Сеттер для новых значений сторон треугольника"""
        if side_one > 0 and side_two > 0 and side_three > 0:
            self.side_one = side_one
            self.side_two = side_two
            self.side_three = side_three
        else:
            raise ValueError('Ошибка, сторона треугольника не может быть меньше 0.')

    def square(self):
        """Метод расчета площади треугольника"""
        return (self.side_one * self.side_two * self.side_three)

    def perimeter(self):
        """Метод расчета периметра треугольника"""
        return (self.side_one + self.side_two + self.side_three)


class Cube(Square, ABC):
    def __init__(self, r):
        """Инициализация дочернего класса куб Cube от класса квадрат Square
        self.figure_name = 'Куб' Имя фигуры
        self.sq формула расчета площади поверхности куба
        r радиус
        """
        self.figure_name = 'Куб'
        self.sq = (r ** 2) * 6


class Pyramid(Triangle, ABC):
    def __init__(self, side_base, hight):
        """Инициализация дочернего класса пирамида Pyramid от класса треугольник Triangle
        self.figure_name = 'Пирамида' Имя фигуры
        self.sq формула расчета площади куба
        hight - высота, side_base - основание
        """
        self.figure_name = 'Пирамида'
        self.sq = (1 / 3) * hight * (side_base ** 2)


square = Square(5)
print(square.figure_name, square.side)

triangle = Triangle(2, 2, 2)
print(triangle.figure_name, triangle.side)

cube = Cube(5)
print('Площадь поверхности куба: ', cube.sq)

pyramid = Pyramid(2, 4)
print('Площадь поверхности пирамиды: ', pyramid.sq)
