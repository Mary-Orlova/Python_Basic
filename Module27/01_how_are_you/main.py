from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """Метод "Как дела?" (запрос у пользователя)
     + предоставление ответа с вызовом функции (передается из основной программы)
     Возвращаем значение обернутой функции и декоратора
    """
    def wrapper():
        answer = input('\nКак дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func()
        return func
    return wrapper


@how_are_you
def summer():
    print('<лето на дворе...>')


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
summer()
