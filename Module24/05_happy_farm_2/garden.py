class Gardener:

    def __init__(self, name):
        self.name = name
        self.my_garden = PotatoGarden(5)
        self.my_garden.are_all_ripe()

    def garden_care(self):
        for _ in range(3):
            print('*Садовник {} ухаживает за грядкой*\n'.format(self.name))
            self.my_garden.grow_all()
            self.my_garden.are_all_ripe()

    def crop(self):
        print('{} собрал урожай. '.format(self.name))


class Potato:
    states = {0 : 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3:'Зрелая'}

    def __init__(self,index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {}  сейчас {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела! Можно собирать!\n')