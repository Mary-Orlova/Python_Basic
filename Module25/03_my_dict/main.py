class MyDict(dict):
    """Метод возвращения значения по ключу словаря"""
    def get_value(self, key):
        return super().get(key, 0)


mydict = MyDict({"one": 1, "two": 2, "three": 3, "four": 4})
print("\nПолучить значение по ключу 'four':", end=' ')
print(mydict.get_value("four"))
print("Получить значение по ключу 'five':", end=' ')
print(mydict.get_value("five"))
