from typing import Callable, Any
import time
from datetime import datetime


def timer(func: Callable) -> Callable:
    """Декоратор -выводящий время, ктр заняло выполнение декорируемой функции"""
    def wrapper_func(*args, **kwargs) -> Any:
        """Стартовая точка работы программы started_at = time.time()
        Результат работы функции result = func(*args, **kwargs)
        Конечная точка работы программы ended_at = time.time()
        Расчет затраченного времени на программу run_time = round(ended_at - started_at, 4)
        Округляем до 4 знаков
        Вывод итога времени на экран
        """
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print('Фун-ция работала {} сек'.format(run_time))
        return result
    return wrapper_func


def logging(func: Callable) -> Callable:
    """Декоратор -логирующий работу кода """
    def wrapper_func(*args, **kwargs) -> Any:
        try:
            print('\nВызывается функция {func}\nДокументация: {doc}'.format(
                func=func.__name__, doc=func.__doc__
            ))
            result = func(*args, **kwargs)
            print('Функция успешно завершила работу')
            return result
        except Exception as error:
            error = f'{datetime.now().strftime("%d.%m.%Y %H:%M:%S")} - {func.__name__} - {error}'
            with open('function_errors.log', 'a', encoding='utf-8') as logs:
                logs.write(error)
    return wrapper_func


@logging
@timer
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result

@logging
@timer
def name_error():
    name = something


my_sum = squares_sum()
name_error()
print(my_sum)
