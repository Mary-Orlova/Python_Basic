def find_coin(x,y):
  if x <= r and y <= r:
   print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')

x = float(input('Введите координату по горизонтали: '))
y = float(input('Введите координату по вертикали: '))
r = int(input('Введите радиус:'))
find_coin(x,y)
