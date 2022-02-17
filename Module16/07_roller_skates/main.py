def rolls():
    for i_size in range(count_rolls):
        print('Размер', i_size + 1, 'пары: ',end='')
        size_caple = int(input())
        rolls_list.append(size_caple)

def people():
    for i_size_people in range(count_people):
        print('Размер ноги', i_size_people + 1, 'человека: ',end='')
        size_people = int(input())
        people_list.append(size_people)
    find_count_people()

def find_count_people():
    count = 0
    for num in people_list:
        for i in range(len(rolls_list)):
            if rolls_list[i] >= num:
                rolls_list.remove(rolls_list[i])
                count += 1
                break
    print('Наибольшее кол-во людей, которые могут взять ролики: ', count)


count_rolls = int(input('Кол-во коньков: '))
rolls_list = []
rolls()
count_people = int(input('\nКол-во людей: '))
people_list = []
people()



