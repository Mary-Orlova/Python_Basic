class Child:

    def __init__(self, name, age=16, dormant_state='спокойствие', feed_state="тревожность" ):
        self.name = name
        self.age = age
        self.dormant_state = dormant_state
        self.feed_state = feed_state

    def print_info(self):
        print('Имя: {}\nВозраст: {}\nСостояние спокойствия: {}\nСостояние голода: {}\n'.format(
            self.name, self.age, self.dormant_state, self.feed_state)
        )