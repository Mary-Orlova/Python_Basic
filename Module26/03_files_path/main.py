from collections.abc import Iterable
import os


path = os.path.abspath(os.path.join('..', '..'))


def gen_files_path(folder: str, path=None) -> Iterable[str]:
    """Генератор путей файлов по указанному пути"""
    if path is None:
        path = os.path.abspath(os.path.join('..', 'Python_Basic', '..'))
        # path = os.path.abspath(os.path.join(os.path.sep))
    for i_elem in os.listdir(path):
        temp = os.path.abspath(os.path.join(path, i_elem))
        if os.path.isdir(temp) and i_elem != folder:
            gen_files_path(temp)
        yield temp
        if i_elem == folder:
            return


function = gen_files_path(path)

for element in function:
    print('\n', element)
