def calculating_math_func(data):
    if data in factorials:  # Если результат уже содержит факториал
        result = factorials[data]
    else:
        result = max(factorials.values())  # Максимальное значение факториала кладем в result
        for index in range(max(factorials.keys()) + 1, data + 1):
            result *= index
            factorials[index] = result  # Заполнение словаря
    result /= data ** 3
    result = result ** 10
    return result

factorials = {1:1   }
number = int(input('Введите число: '))
num_fact = calculating_math_func(number)
print(num_fact)
