class Parent:

    def __init__(self, name, age=36):
        self.name = name
        self.age = age
        self.kids = []

    def age(self, Child):
        if self.age - Child.age >= 16:
            self.kids.append(Child.name)
        else:
            print('Ошибка в возрасте - разница с ребенком должна быть >= 16 лет')
            age = int(input('Ввести корректный возраст родителя: '))
            self.age = age

    def calm_down(self, Child):
        if Child.dormant_state == 'тревожность':
            Child.dormant_state = 'спокойствие'
            print('{} рассказывает интересную историю.'.format(self.name))
            print('{} успокаивается.\n'.format(Child.name))

    def feed(self, Child):
        if  Child.feed_state == 'голод':
            Child.feed_state = 'сыт'
            print('{}: Еда готова можно есть! '.format(self.name))
            print('{} ест, появляется чуство сытости.\n'.format(Child.name))

    def print_info(self):
        print('Имя: {}\nВозраст: {}\nДети: {}\n'.format(
            self.name, self.age, self.kids)
        )
