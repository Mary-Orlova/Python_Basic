import functools
import time
from typing import Callable


def slow_down(func: Callable) -> Callable:
    """Ждем 2 секунды, затем вызваем переданную функцию"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Передаем число 5 из основной программы
        + вызываем time.sleep - в скобках секунды(2)
        Возвращаем декоратор и обернутую функцию"""
        time.sleep(2)
        return func(*args, **kwargs)
    return wrapper


@slow_down
def count(from_number: int) -> None:
    """Метод - счетчик
    Если переданное число из основной программы < 1 - то код сработал,
    иначе - выводим номер и затем уменьшаем его"""
    if from_number < 1:
        print("Код сработал")
    else:
        print(from_number)
        count(from_number - 1)


count(5)
