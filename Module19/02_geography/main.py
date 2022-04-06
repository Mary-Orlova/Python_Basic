count_country = int(input('Кол-во стран: '))
data_country = {}

for cities in range(count_country):
    # создаю словарь со значением страны
    country_and_cities = input('{} страна: '.format(cities + 1)).split()
    for city in country_and_cities[1:]:
        data_country[city] = country_and_cities[0]
print()

for choice_city in range(count_country + 1):
    city = input('{} город: '.format(choice_city + 1))
    country = data_country.get(city) #находим страну(значение) по ключу(город)
    if country:
        print('Город {} расположение в стране {}.'.format(city,country))
    else:
        print('По городу {} данных нет.'.format(city))

