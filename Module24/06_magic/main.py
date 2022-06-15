from magic import Water, Air, Fire, Earth, Storm, Steam, Dirt
from magic import Lightning, Dust, Lava, Spark, Fireworks, Earthquake


def get_magic(new_element):
    if new_element is None:
        print('\nНе удалось совершить магию! Попробуй еще раз с другим элементом.')
    else:
        print('\nШалость удалась!')
        print(new_element.answer)


water = Water()
air = Air()
fire = Fire()
earth = Earth()

storm = Storm()
steam = Steam()
dirt = Dirt()
lightning = Lightning()
dust = Dust()
lava = Lava()
spark = Spark()
fireworks = Fireworks()
earthquake = Earthquake()

new_element = Water() + Water()
# new_element = Fire() + Fly_powder()
get_magic(new_element)
