from typing import Callable, Any


def counter(func: Callable) -> Any:
    def wrapper(*args, **kwargs):
        """В функции-оберке подсчет кол-ва раз вызываемости ф-ции
        Каждый раз увеличиваем на единицу wrapper.count += 1
         Возвращем полученные значения оборачивываемой функции и декоратора"""
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


@counter
def get_count() -> None:
    """Функция, вызовы которой нужно считать"""
    print("<Тут что-то происходит ... >")


get_count()
get_count()
get_count()

print('\nКоличество вызовов функции: ', get_count.count)
