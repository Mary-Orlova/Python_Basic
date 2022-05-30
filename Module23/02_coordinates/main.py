import random

def division_x_y(x, y): #f
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def division_y_x(x, y): #f2
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    file_1 = open('coordinates.txt', 'r')
    file_2 = open('result.txt', 'w')
    for line in file_1:
        nums = line.split() #nums_list
        result1 = division_x_y(int(nums[0]), int(nums[1]))
        result2 = division_y_x(int(nums[0]), int(nums[1]))
        number = random.randint(0, 100)
        nums_sorted = sorted([result1, result2, number]) #my_list
        file_2.write(''.join(str(nums_sorted)))
        file_2.write('\n')
except ValueError:
    print("Внимание: Попытка передать x,y не в формате цифр")
    print('В файл записаны только цифровые значения при верных парах')
finally:
    file_1.close()
    file_2.close()

