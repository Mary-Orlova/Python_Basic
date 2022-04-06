orders = int(input('Введите кол-во заказов: '))
count = 1 #для счетчика в цикле
pizza_dict = dict()

for _ in range(orders):
    customer = input('{} заказ: '.format(count + 1))
    count += 1
    surname, pizza, summa = customer.rsplit(maxsplit=3)
    summa = int(summa)
    if surname not in pizza_dict:
        pizza_dict[surname] = {pizza:summa}
    else:
        if pizza not in pizza_dict[surname]:
            pizza_dict[surname] |= {pizza:summa}
        else:
            pizza_dict[surname][pizza] += summa

for surname, order in sorted(pizza_dict.items()):
    print(f'{surname}:')
    for pizza, summa in sorted(order.items()):
        print('  ',pizza,':',summa)




