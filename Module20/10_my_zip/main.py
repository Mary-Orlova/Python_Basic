
def my_zip(string,numbers_tuple):
        my_zip = []
        for index, value in zip(string, numbers_tuple):
            result = (index, value)
            my_zip.append(result)
        print(zip(string, numbers_tuple))
        print(*my_zip)

string = 'abcd'
numbers_tuple = (10,20,30,40)
# list_number_and_letter = [100, 200, 300, 'буква', 0, 2, 'а']
# numbers = 1,2,3,4,5
# dictionary = {'one': 65,'two': 87,'three':12,'four':453}
# if isinstance(dictionary,dict):#если переменная является словарем
#     test = list(dictionary.items()) #Возвращает пары (ключ, значение) для каждого элемента словаря.

my_zip = my_zip(string,numbers_tuple)