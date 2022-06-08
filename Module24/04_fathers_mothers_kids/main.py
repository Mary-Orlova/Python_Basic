from Children import Child
from Parents import Parent

child_1 = Child('Егор', 16, 'спокойствие', 'голод')
child_2 = Child('Владимир', 17, 'тревожность', 'голод')
child_3 = Child('Надя', 18, 'тревожность', 'сыт')
father = Parent('Евгений', 37)
mother = Parent('Людмила', 36)

Parent.calm_down(father,child_1)
Parent.feed(father, child_1)
Parent.calm_down(father,child_2)
Parent.feed(father, child_2)
Parent.calm_down(father, child_3)
Parent.feed(father,child_3)

Parent.age(father,child_1)
Parent.age(father,child_2)
Parent.age(father,child_3)

Parent.age(mother,child_1)
Parent.age(mother,child_2)
Parent.age(mother,child_3)

father.print_info()
mother.print_info()
child_1.print_info()
child_2.print_info()
child_3.print_info()