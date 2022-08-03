from typing import List
from functools import reduce


def degree(number: float) -> List:
    result = list(map(lambda number: round(number ** 3, 3), floats))
    print(result)


def new_names(name: str) -> List:
    names_list = list(map(lambda name: name, filter(lambda name: len(name) >= 5, names)))
    print(names_list)


def product(num: int) -> List:
    products = reduce((lambda res, x: res * x), numbers, 1)
    print(products)


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


degree(floats)
new_names(names)
product(numbers)
