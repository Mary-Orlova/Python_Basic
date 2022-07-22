from typing import Callable, Any

app = {}


def callback(key: str):
    """Метод - вызова функции,
    в обертку передается функция example по ключу (//)
    если передается другой ключ - то вызывается ошибка в 27 строке при проверке словаря
    """
    def wrapped(func: Callable) -> Any:
        app[key] = func
    return wrapped


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
