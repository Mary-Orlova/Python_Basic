class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Имя: {self.__name}\nФамилия: {self.__surname}\nВозраст :{self.__age}'


class Employee(Person):
    def calc_salary(self):
        raise Exception('This method must be overriden')

    def __str__(self):
        return super().__str__() + f'\nЗарплата: {self.calc_salary()}\n'


class Manager(Employee):
    def calc_salary(self):
        return 13000


class Agent(Employee):
    sales: int

    def calc_salary(self):
        return 5000 + 0.05 * self.sales


class Worker(Employee):
    hours: int

    def calc_salary(self):
        return 100 * self.hours
