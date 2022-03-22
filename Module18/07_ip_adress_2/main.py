IP = input('Введите IP:').split('.')
count_num = 0

if len(IP) < 4:
    print('Адрес - это четыре числа, разделенные точками')
else:
    for i_num in IP:
        if i_num.isdigit():
            if int(i_num) <= 255:
                count_num += 1
                continue
            else:
                print(i_num,'превышает 255')
        else:
            print(i_num,' - не целое число')
            break
    if count_num == 4:
        print('IP - адрес корректен')