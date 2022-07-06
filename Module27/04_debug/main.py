from typing import Callable
import functools


def debug(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Оборачиваем функцию в декораторе
            В результ заносим передаваемые значения из основной функции result = func(*args, **kwargs)
            Указываем какую функцию вызываем и какое значение возвращаем
            Возвращаем обернутую функцию и декаратор
            """
        result = func(*args, **kwargs)
        print('\nВызывается  {func}\n{func} вернула значение', repr(result).format(
            func=func.__name__
        ))
        print(result)
        return func(*args, **kwargs)
    return wrapper


@debug
def greeting(name, age=None):
    """Метод-приветствие
    Если есть возраст age - выводим сообщение с указанием возраста,
    иначе - привествие только по имени"""
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
