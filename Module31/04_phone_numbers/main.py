import re


phone_numbers = ['9999999999', '999999-999', '99999x9999']


def check():
    for number in phone_numbers:
        if re.match(r'[8-9]{1}[0-9]{9}', number) and len(number) == 10:
            print('всё в порядке')
        else:
            print('не подходит')


if __name__ == "__main__":
    check()
