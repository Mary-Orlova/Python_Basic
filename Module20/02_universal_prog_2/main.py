a = 'О Дивный Новый мир!'
b = [100, 200, 300, 'буква', 0, 2, 'а']
c = 1,2,3,4,5
d = {'one': 65,'two': 87,'three':12,'four':453}
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def crypto(s):# вернуть индекс для индекса и значения в функции is_prime
    return [index for index, value in enumerate(s) if is_prime(index)]

def is_prime(i_num): #счетчик-проверка на простоту индексов
    count = 0
    for index in range(2,i_num//2+1):
        if i_num % index == 0:
            count = count + 1
    if count <= 0:
        return True
    else:
        return False

def new_dict(test):
    if isinstance(test,dict):#если переменная является словарем
        test = list(test.items()) #Возвращает пары (ключ, значение) для каждого элемента словаря.
    for index in simple_index: #для каждого индекса из списка простых индексов
        simple_values.append(test[index]) #добавляем в список значение по индексу
    print(simple_values[2:]) #вывод спика -значений простых индексов(0 и 1 не являются такими,
# поэтому выводим со второго индекса)

test = n #подставляем сюда для теста данные
simple_values = [] #список для вывода значений простых индексов
simple_index = crypto(test) #список, где храним индексы
new_dict(test) #вывод списка-значений простых индексов

