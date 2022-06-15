class Water:
    def __add__ (self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth) or isinstance(other, Fly_powder):
            return Dirt()

class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Fly_powder):
            return Spark()

class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Fly_powder):
            return Fireworks()

class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other,Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()

class Fly_powder:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Spark()
        elif isinstance(other, Fire):
            return Fireworks()
        elif isinstance(other, Earth):
            return Earthquake()

class Storm:
    answer = 'Cложили два класса и вывели Шторм.'

class Steam:
    answer = 'Cложили два класса и вывели Пар.'

class Dirt:
    answer = 'Cложили два класса и вывели Грязь.'

class Lightning:
    answer = 'Cложили два класса и вывели Молнию.'

class Dust:
    answer = 'Cложили два класса и вывели Пыль.'

class Lava:
    answer = 'Cложили два класса и вывели Лаву.'

class Spark:
    answer = 'Cложили два класса и вывели Искру.'

class Fireworks:
    answer = 'Cложили два класса и вывели Феерверк.'

class Earthquake:
    answer = 'Cложили два класса и вывели Землетрясение.'
