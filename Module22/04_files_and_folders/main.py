import os

def get_sizes(path):
    files_stat = [0, 0, 0] #размер каталога - файлы - подпапки

    for element in os.listdir(path): #походим по составу директории
        if os.path.isfile(os.path.abspath(os.path.join(path, element))):
            file_path = os.path.abspath(os.path.join(path, element))
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size #Размер каталога (в Кб)
            files_stat[2] += 1 #кол-ва файлов

        else:
            files_stat[0] += (get_sizes(os.path.abspath(os.path.join(path, element))))[0] #Размер каталога (в Кб)
            files_stat[2] += (get_sizes(os.path.abspath(os.path.join(path, element))))[2]
            files_stat[1] += 1 #кол-ва подкаталогов
    return files_stat

path = os.path.abspath(os.path.join('..', '..', 'Module14'))
files_stat = get_sizes(path)
print('Размер каталога (в Кб):',files_stat[0] / 1024)
print('Количество подкаталогов:', files_stat[1])
print('Количество файлов:', files_stat[2])