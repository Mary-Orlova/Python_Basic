import random

numbers = [random.randint(0,10) for number in range(10)]
print(f'Оригинальный список: {numbers}')
result = dict()
for index, value in enumerate(numbers):
    if index % 2 == 0:
        result[index] = value

result = [(key, value + 1) for key, value in result.items()]
print(f'Новый список: {result}')

# Второй способ
# numbers = [random.randint(0,10) for number in range(10)]
# print(f'Оригинальный список: {numbers}')
# dictionary = dict()
# result = list()
#
# for i in numbers[0::2]:
#     if len(dictionary) == 0:
#         dictionary = {i:i + 1}
#     else:
#         dictionary.update({i:i + 1})
#
# result = [(key, value + 1) for key, value in dictionary.items()]
# print(f'Новый список: {result}')