from typing import Any, Optional


class CountIterator:
    """Инициация класса итератор"""
    def __init__(self, number: int):
        """self.count = текущее перебираемое значение
        self.number = передаваемое максимальное значение
        """
        self.count = 0
        self.number = number

    def __iter__(self) -> Optional[Any]:
        """ Метод возврата итерируемого значения"""
        return self

    def __next__(self) -> int:
        """Метод следующего итерируемого значения
        Увеличиваем текущее значение на 1 единицу"""
        self.count += 1
        """ Проводим поверку - если текущее значение = максимальному,
        то останавливаем данный метод, а иначе выводим на экран тек знач,
         ктр возводим во вторую степень и возвращаем результ """
        if self.count == self.number:
            raise StopIteration
        else:
            print(self.count, '** 2', end=' ')
            return self.count ** 2


my_iter = CountIterator(number=6)

print('Вывод квадратов - класс итератор')

for element in my_iter:
    """Класс- итератор -построчно вывод полученного значения из класса Итератор"""
    print('=', element)


def generator(number: int):
    """Генератор квадратов от 1 до максимального"""
    for number in range(1, number):
        print(number, '** 2', end=' ')
        yield number ** 2


choose_number = int(input('\nВведите максимальное число: '))

# второй способ
generation = generator(choose_number)

print('Вывод функции - генератор')
for element in generation:
    print('=', element)

# третий способ
print('\nВывод функции - генераторное выражение')
generation_two = (element ** 2 for element in range(1, choose_number))

for element in generation_two:
    print(element)
