import math
class Circle:

    def __init__(self, abscissa = 0, ordinate = 0,radius = 1):
        self.abscissa = abscissa #x
        self.ordinate = ordinate #y
        self.radius = radius

    def get_square(self): #площадь круга
        return math.pi * (self.radius ** 2)

    def perimeter(self): #длина окружности круга
        perimeter = (2 * math.pi )* self.radius
        return perimeter

    def increase_two(self, increase): #k увеличение
        self.radius *= increase

    def print_info(self):
        print(
            'X: {}\nY: {}\nРадиус: {}\nПлощадь: {}\nПериметр: {}\n'.format(
                self.abscissa, self.ordinate, self.radius, self.get_square(), self.perimeter()

            ))

    def get_increase(self,circle_1):
        if (self.abscissa - circle_1.abscissa) ** 2 + (self.ordinate - circle_1.ordinate) ** 2 <= (self.radius + circle_1.radius) ** 2:
            print('Пересекаются')
        else:
            print('Не пересекаются')
