class Student:
    N_group = 12

    def __init__(self,FI,perfomance):
        self.FI = FI
        self.performance = perfomance
        self.avg = sum(self.performance) / len(self.performance)  # средний бал

    def give_average(self):
        return self.avg

    def print_info(self):
        print('Фамилия Имя: {}\n№ группы: {}\nУспеваемость:{}\nСредний балл: {}\n'.format
              (self.FI, self.N_group, self.performance, self.avg))
