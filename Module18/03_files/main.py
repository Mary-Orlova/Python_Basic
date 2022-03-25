symbols_special = '@№$%^&*).'
file = input('Название файла: ')

if any(file.startswith(symbol) for symbol in symbols_special):
    print('Ошибка: название начинается на один из специальных символов')
elif not file.endswith(('.txt','.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно')
