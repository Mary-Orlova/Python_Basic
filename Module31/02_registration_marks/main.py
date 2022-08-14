import re


car_number = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"
auto_pattern = re.findall(r'\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', car_number)
taxi_pattern = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', car_number)

if __name__ == "__main__":
    print('\nСписок номеров частных автомобилей:', auto_pattern)
    print('\nСписок номеров такси:', taxi_pattern)
