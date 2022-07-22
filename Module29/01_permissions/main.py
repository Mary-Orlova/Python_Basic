from typing import Callable
import functools


def check_permission(user_name: str) -> Callable:
    """В user_permissions заносим имя пользователя - в основной программе присвоен admin """
    # user_permissions = ['admin']

    def check_permission_2(func: Callable) -> Callable:
        """Метод проверки доступа к функции у текущего пользователя(user_permissions) """
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Callable:
            try:
                """Проверка и отлов ошибки:
                если у пользователя есть доступ к вызываемой функции то - выполняется функция,
                если нет - выдается исключение PermissionError"""
                if user_name in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError as error:
                print(error)
                print('У пользователя недостаточно прав, чтобы выполнить функцию {func_name}'.format(
                    func_name=func.__name__))
        return wrapped
    return check_permission_2


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    """Метод для удаления сайта- только у администратора admin"""
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    """Метод добавления комментария - только у пользователя user_1"""
    print('Добавляем комментарий')


delete_site()
add_comment()
