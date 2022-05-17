first_tour = open('first_tour.txt', 'w')
info = '80,Ivanov Serg 80,Sergeev Petr 92,Petrov Vasiliy 98,Vasiliev Maxim 78'

for string in info.split(','):
    first_tour.write(string+'\n')
first_tour.seek(0)

first = list(open('first_tour.txt', 'r'))
points = first[0]
first.pop(0)
winner =[]

for line in first:
    member_list = line.split()
    member_list[0],member_list[1] = member_list[1],member_list[0]
    if int(member_list[2]) > 80:
        winner.append(member_list)

winner.sort(key=lambda a: int(a[-1]))
winner.reverse()
count = str(len(winner))
win = []
number = 1

for man in winner:
    name = str(man[0][0]) + '.'
    winners_info = str(number) + ') ' + name + ' ' + man[1] + ' ' + man[-1]
    win.append(winners_info)
    number += 1

with open('second_tour.txt', 'w') as second_tour:
    second_tour.write(count + '\n')
    result = '\n'.join(win)
    second_tour.write(result)

first_tour.close()
second_tour.close()