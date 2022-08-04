from collections import Counter


def can_be_poly(string: str) -> bool:
    return len([v for v in Counter(string).values() if v % 2]) <= 1


if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
