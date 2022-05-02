import copy
import json

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def find_key(struct,
             key,
             count):
    while count > 0:
        phone = input('Название: ')
        if key_one and key_two in new_site:
            return struct[key_one] ,struct[key_two]
        else:
            result = None
        for sub_struct in new_site:
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, count)
            new_site['html']['head']['title'] = 'Куплю/продам {} недорого'.format(phone)
            new_site['html']['body']['h2'] = 'У нас самая низкая цена на {}'.format(phone)
            print(f"Структура сайта:{phone}")
        count -=1
        result = json.dumps(new_site, indent=3, ensure_ascii=False,sort_keys=False)
        print("site = ",result)


count = int(input('Кол-во сайтов: '))
new_site = copy.deepcopy(site)
key_one = new_site['html']['head']['title']
key_two = new_site['html']['body']['h2']
key = [key_one,key_two]
find_key(new_site,key,count)

