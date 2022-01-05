def find_third_number(last_year,next_year):
  print()
  print('Годы от', last_year, 'до', next_year, 'с тремя одинаковыми цифрами:')
  while last_year < next_year:
    for every_year in range(10):
      if 3 == str(last_year).count(str(every_year)):
        print(last_year)
    last_year += 1

last_year = int(input('Введите первый год:'))
next_year = int(input('Введите второй год:'))

find_third_number(last_year,next_year)
