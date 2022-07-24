from typing import Callable


def decorator_with_args_for_any_decorator(func) -> Callable:
    """Декоратор функция, принимает от декорируемого декоратора аргументы, переданные в декорируемый декоратор.
    Принимается декорируемая функция, возвращается объект декорируемой функции"""

    def wrapper(*args, **kwargs) -> Callable:
        """Обертка принимает аргументы от дек. функции, и возвращает объект декорируемой функции"""
        print('Переданные арги и кварги в декоратор: {args}, {kwargs}'.format(args=args, kwargs=kwargs))
        return func
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable):
    """ Декоратор функция, принимает объект функции, возвращает объект декорируемая функция"""

    def wrapper(*args, **kwargs) -> Callable:
        """Обертка возвращает результат работы декорируемой функции"""
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей', 1, test_1=1, test_2='раз-раз')
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)


decorated_function("Юзер", 101)
