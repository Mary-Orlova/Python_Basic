def sum_recursive(*args):
    def get_numbers_list(nums_list):
        result = []
        for number in nums_list:
            if isinstance(number, int):
                 result.append(number)
            else:
                result.extend(get_numbers_list(number))
        return result
    return sum(get_numbers_list(args))

# print('Ответ в консоли:' ,sum_recursive([[1, 2, [3]], [1], 3]))
# print('Ответ в консоли: ', sum_recursive(1, 2, 3, 4, 5))

