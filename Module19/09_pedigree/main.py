def height(man):
    if man not in tree:
        return 0
    else:
        return 1 + height(tree[man])

def caple():
    for member in range(people_count-1):
        name_child, name_parent = input('{} пара: '.format(member + 1)).split(' ')
        tree[name_child] = name_parent

def find():
    for man in set(tree.keys()).union(set(tree.values())):
        heights[man] = height(man)
    for key, value in sorted(heights.items()):
        print(key, value)

people_count = int(input('Введите количество человек: '))
tree = dict()
heights = dict()
caple()
print('\n“Высота” каждого члена семьи: ')
find()
