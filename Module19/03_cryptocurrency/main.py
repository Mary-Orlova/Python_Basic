data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [ #тут нет ключей -есть индексы - словарь в списке
        {
            "fst_token_info": { #в[0]-словарь,а по нужному ключу еще словарь
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


print('Вывод списков ключей и значений словаря:\n',data)
data['ETH']['total_diff'] = 100
# print('\n “ETH” добавить ключ “total_diff” со значением 100:\n',data['ETH'])

data['tokens'][0]['fst_token_info']['name'] = 'doge'
# print('Поменять значение ключа “name”:\n',data['tokens'][0]['fst_token_info'])

data['ETH']['total_out'] = data['tokens'][0].pop('total_out')
# Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”


data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
# Внутри "sec_token_info" изменить название ключа “price” на “total_price

#print(data)


