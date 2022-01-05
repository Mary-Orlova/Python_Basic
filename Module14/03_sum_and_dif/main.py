def suma_number(number):
   global suma
   while number > 0:
       digit = number % 10
       suma = suma + digit
       number = number // 10
   print('\nСумма цифр:', suma)

def count_number(number):
   global count
   countnumber = number
   while countnumber > 0:
       count += 1
       countnumber = countnumber // 10
   print('Кол-во цифр в числе:', count)

number = int(input('Введите число: '))
suma = 0
suma_number(number)
count = 0
count_number(number)
print('Разность суммы и кол-ва цифр:',suma - count)
