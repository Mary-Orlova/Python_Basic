import os
from collections.abc import Iterable


def gen_files_dir(path: str, depth=1) -> Iterable[str]:
    """Рекурсивно перебираем файлы и каталоги до определенной глубины"""
    depth -= 1
    with os.scandir(path) as path_now:
        for entry in path_now:
            yield entry.path
            if entry.is_dir() and depth > 0:
                yield from gen_files_dir(entry.path, depth)


directory = os.path.abspath(os.path.join('..', '..'))
files = list(gen_files_dir(directory))
line_count = 0

for file_dir in files:
    """Если "файл" директории не является файлом- продолжаем"""
    if not os.path.isfile(file_dir):
        continue

    """Только файлы с расширением .py"""
    files_filtered = [x for x in files if x.endswith('.py')]

    if not files_filtered:
        """Если "файл" не попал в фильтр файлов, то попробовать:
        открыть в режиме чтения и вводим счетчик строки local_count
        Для каждой строки в файле - если не пустая и не с комментарием и нет анотации, то
        прибавляем 1 к счетчику строк
        В конце файл закрываем
        Если же поймана ошибка - продолжаем
        """
        try:
            file = open(file_dir, 'r')
            local_count = 0
            for line in file.read().split('\n'):
                if (not line.strip() == '') and (not line.strip().startswith("#")) and (
                        not line.strip().startswith('"')):
                    local_count += 1
            print('\n{} - {} ст'.format(file_dir, local_count))
            line_count += local_count
            file.close()
        except ValueError:
            continue

print('\nВсего строк:', line_count)
