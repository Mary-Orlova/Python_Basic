goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product in goods:
    product_name = product
    product_id = goods[product]
    product_count, product_sum = 0, 0

    for commodity in store[product_id]:
        product_count += commodity['quantity']
        product_sum += commodity['price'] * commodity['quantity']

    print(product_name, '-', product_count, ' шт, стоимость', product_sum, 'рублей.' )
