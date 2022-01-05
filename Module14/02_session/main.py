print("Введите первую точку")

x1 = float(input('X: '))
y1 = float(input('Y: '))

print("\nВведите вторую точку")

x2 = float(input('X: '))
y2 = float(input('Y: '))

#y = k * x + b, где k и b — числа, означающие угловой коэффициент и вертикальное смещение прямой.
x_diff = x1 - x2
y_diff = y1 - y2

if x1 == x2:
    print('x =', x1, 'При любом Y')

elif y_diff == 0:
    print('y= ', y1, 'При любом X')

elif x1 == x2 and y1 == y2:
    print('По данным координатам задача имеет бесконечное множество решений')
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print('Уравнение прямой,проходящей через эти точки: ')
    print('y=',k,'* x + ',b)
