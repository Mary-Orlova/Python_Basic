import os

def save_file(string):
    way = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')
    file_name = input('Введите имя файла: ')
    path = way.replace(" ", "/")
    real_path = os.path.join(path, file_name)
    path = str('/' + real_path)
    check_file = os.path.exists(path)
    if check_file:
        print('Файл с таким именем уже существует!')
        answer = input('Вы действительно хотите перезаписать файл? ').lower()
        if answer == 'да':
            new_file = open(path, 'w')
            new_file.write(string)
            print('Файл успешно перезаписан!')
        else:
            print('Файл не перезаписан')
    else:
        new_file = open(path, 'w')
        new_file.write(string)
        print('Файл успешно сохранён!')

string = input('Введите строку: ')
save_file(string)
#куда записывала Users mariaorlova PycharmProjects Python_Basic Module22
