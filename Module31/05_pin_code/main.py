import itertools


pin_code = itertools.product(range(10), repeat=4)

if __name__ == "__main__":
    for combination in pin_code:
        print(combination)
