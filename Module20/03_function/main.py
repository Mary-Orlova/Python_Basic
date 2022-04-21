def find(test,element):
    if element in test:
        if test.count(element) > 1:
            first_index = test.index(element)
            second_index = test.index(element, first_index + 1) + 1
            return test[first_index:second_index]
        else:
            return test[test.index(element):]
    else:
        return ()

# print(find((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
