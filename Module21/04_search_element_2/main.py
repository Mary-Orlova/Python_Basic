site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def user_choose(choose):
    if choose == 'y':
        deep = int(input('Введите максимальную глубину: '))
    else:
        deep = 4
    return deep

def find_key(struct,key,deep):
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct,dict):
            result = find_key(sub_struct,key,deep)
            if deep == 1:
                result = None
                break
            deep -= 1
            if result:
                break
        else:
            result = None
    return result

user_key = input('Какой ключ ищем? ')
choose = input('Хотите ввести максимальную глубину? Y/N: ').lower()

deep = user_choose(choose)
value = find_key(site,user_key,deep)

if value:
    print(value)
else:
    print('Такого ключа в структуре нет.')




