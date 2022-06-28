from typing import Any, Optional


class QHofstadter:
    """Инициализация стартовой точки self.start"""
    def __init__(self, start: list):
        self.start = start[:]

    def __next__(self):
        """Последовательное предоставление чисел по Хофштадтеру
        Попробовать высчитать q и вернуть его пользователю
        Иначе ошибка и остановка итерации
        """
        try:
            q = self.start[-self.start[-1]] + self.start[-self.start[-2]]
            self.start.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self) -> Optional[Any]:
        """Возврат итерируемого объекта"""
        return self

    def current_state(self):
        """Возврат стартового значения"""
        return self.start


hofstadter = QHofstadter([1, 1])
count = 0

for element in range(20):
    """Для каждого элемента из 20
    Если счетчик < 20 и стартовое значение не [1,2]-- вывод итерируемых объектовм и счетчик +1
    Иначе - сообщение об ошибке и выход из цикла
    """""
    if count < 20:
        if hofstadter.start == [1, 2]:
            print('\nВведено не допустимое значение [1, 2]')
            break
        else:
            print(next(hofstadter))
    count += 1
