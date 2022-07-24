from typing import Callable
import time
import functools
from datetime import datetime


def log_method(time_format: str, cls_name: str) -> Callable:
    """ Декоратор. Выводит имена класса, метода, время запуска и время его работы."""

    def method_decorator(func: Callable) -> Callable:
        """"В обертку передаем функцию со всеми параметрами *args, **kwargs
        в wrapped_func:
        formatted_time b d Y - H:M:S
        вывод инфо о запускаемой функции - имени и дате запуска, времени окончания функции
        возврат результата, обертки и самого декоратора
        """
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            formatted_time = ''.join('%' + sbl if sbl.isalpha() else sbl for sbl in time_format)
            print('- Запускается {}.{}. Дата и время запуска: {}'
                  .format(cls_name, func.__name__, datetime.now().strftime(formatted_time)))
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print('- Завершение {}.{}, время работы = {}s'
                  .format(cls_name, func.__name__, round(end - start, 3)))
            return result
        return wrapped_func
    return method_decorator


def log_methods(time_format: str) -> Callable:
    """Декоратор -логирующий работу кода """

    def wrapped(cls):
        """В методе-обертке проверяем, каждый метод из присутствующих в cls
        если метод не является магическим, то логируем метод
         метод получаем с помощью getattr и затем меняем с setattr, после возвращем cls и обертку """
        for method in dir(cls):
            if method.endswith('__') is False:
                method = getattr(cls, method)
                if callable(method):
                    decorated_method = log_method(time_format, cls.__name__)(method)
                    setattr(cls, method.__name__, decorated_method))
        return cls
    return wrapped


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
