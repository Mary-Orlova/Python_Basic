notes = int(input('Сколько записей вносится в протокол? '))
print('Введите через пробел результаты участника (целое не отрицательное число) и игровое имя (без пробелов)')
score_table = {}

for note in range(notes): #для каждого поля в списке записей
    print(note + 1, 'запись.',end=' ')
    score, name = input('Результат и имя: ').split()
    score = int(score)
    if name in score_table: #для каждого игрока в таблице очков
        if score > score_table[name][0]: #словарь очов> очков по имени игрока по 0 индексу
            score_table[name][0] = score #словарь очков по имени 0 индекса присвоить очки -большие
            score_table[name][1] = note #словарь очков по имени 1 индекса присвоить индекс,когда получил
    else:
        score_table[name] = [score, note] #в словарь(игрок -очки,индекс, когда получил максимальное кол-во очков)

scores = list(score_table.items()) #индекс и значение

def key_sort(gamer):
    return gamer[1][0]- gamer[1][1] #вернуть имя
scores.sort(key=key_sort, reverse = True)
#сортировка-люч забираем из функции+перестройка в обратном порядке

for winner_place in range(3):
    print(winner_place + 1, 'место.', scores[winner_place][0], end =' ')
    print('(', scores[winner_place][1][0], ')', sep='')
    #в scores[winner_place][1]-имя, в scores[winner_place][0]-очки