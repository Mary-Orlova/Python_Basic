IP = input('Введите IP:').split('.')
count_num = 0

if len(IP) < 4:
    print('Адрес - это четыре числа, разделенные точками')
else:
    for number in IP:
        if number.isdigit():
            if int(number) <= 255:
                count_num += 1
                continue
            else:
                print(number,'превышает 255')
        else:
            print(number,' - не целое число')
            break
    if count_num == 4:
        print('IP - адрес корректен')