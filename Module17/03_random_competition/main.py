import random

first_team = [round(random.uniform(5,11),2) for x in range(20)]
second_team = [round(random.uniform(5,11),2) for x in range(20)]
third_team = [(first_team[i] if first_team[i] > second_team[i]
              else second_team[i]) for i in range(20)]

print('Первая команда',first_team)
print('Вторая команда',second_team)
print('Третья команда: ',third_team)
