import math


class MyMath:

    def circle_len(radius: int) -> float:
        """Метод - возврат длины окружности"""
        return 2 * math.pi * radius

    def circle_sq(radius: int) -> float:
        """Метод - возврат площади окружности"""
        return math.pi * (radius ** 2)

    def circle_perimeter(radius: int) -> float:
        """Метод - возврат периметра окружности"""
        return 2 * math.pi * radius

    def cube_volume(edge: int) -> int:
        """Метод - возврат объема куба"""
        return edge ** 3

    def sphere_sq(radius: int) -> float:
        """Метод - возврат поверхности сферы"""
        return math.pi * 4 * (radius ** 2)


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.circle_sq(radius=5)
res_4 = MyMath.cube_volume(edge=6)
res_5 = MyMath.sphere_sq(radius=4)
print('Длина окружности: ', res_1)
print('Площадь окружности: ', res_2)
print('Периметр окружности: ', res_3)
print('Объем куба: ', res_4)
print('Площадm поверхности сферы: ', res_5)
