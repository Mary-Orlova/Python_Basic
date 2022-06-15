import random

class Unit:
    Unit = 'Unit 1'
    heal = 100

    def print_info(self):
        print('Unit: {}\nHeal: {}\n'.format(self.Unit,self.heal))

    def attak(self,unit_1,unit_2):
        while unit_1.heal > 0 and unit_2.heal > 0:
            attak_unit = random.randint(1, 2)
            if attak_unit == 1:
                unit_1.heal = unit_1.heal - 20
                print('Unit 1 атакован! Осталось {} здоровья'.format(unit_1.heal))
            else:
                unit_2.heal = unit_2.heal - 20
                print('Unit 2 атакован! Осталось {} здоровья'.format(unit_2.heal))
        if unit_1.heal > 0:
            print('\nПобедил: Unit 1')
        else:
            print('\nПобедил: Unit 2')

