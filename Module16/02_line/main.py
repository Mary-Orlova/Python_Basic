first_class = []
second_class =[]
common_class = []

for member in range(160,176,2):
    first_class.append(member)

for classmate in range(162,180,3):
    second_class.append(classmate)

print(first_class,second_class)
common_class.extend(first_class)
common_class.extend(second_class)

print('Отсортированный список учеников:',sorted(common_class))



