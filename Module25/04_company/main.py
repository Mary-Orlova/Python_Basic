from Persons import Manager, Agent, Worker
import random

names = ['Анатолий', 'Гоша', 'Грирорий', 'Роман', 'Владлен', 'Егор', 'Михаил', 'Саша', 'Олег', 'Ян']
surnames = ['Косторных', 'Иванов', 'Бржезовски', 'Ахматов', 'Петров', 'Борисенко', 'Калачев', 'Зяблых', 'Сидоров']


def generate_person():
    """ Генерирование имени, фамилии, возраста"""
    name = random.choice(names)
    surname = random.choice(surnames)
    age = random.randint(18, 50)
    return name, surname, age


if __name__ == '__main__':
    employees = list()

    """ Генерирование для класса  managers """
    for _ in range(3):
        employees.append(Manager(*generate_person()))

    """ Генерирование для класса agents """
    for _ in range(3):
        agent = Agent(*generate_person())
        agent.sales = random.randint(2000, 10000)
        employees.append(agent)

    """Генерирование для класса Worker"""
    for _ in range(3):
        worker = Worker(*generate_person())
        worker.hours = random.randint(20, 50)
        employees.append(worker)

    """" Вывод сгенерированных списка и данных"""
    for person in employees:
        print(person)
