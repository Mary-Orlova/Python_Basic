people_count = int(input('Кол-во человек: '))
people = []
count = 0
num = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый',num,'человек')

for man in range(1,people_count+1):
    people.append(man)

while len(people) > 1:
    print('Текущий круг людей: ', people)
    print('Начало счёта с номера:', people[count])
    count = (count + num - 1) % len(people)
    if people[count] == people[-1]:
        print('Выбывает человек под номером:', people.pop(count))
        count = 0
    else:
        print('Выбывает человек под номером:', people.pop(count))
print('Остался человек под номером:', people[0])


