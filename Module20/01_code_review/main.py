students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def id_and_age():
    for student in students:
        id.append(student)
        age.append(students[student]['age'])

def find(dict):
    interests, string = [], ''
    for student in dict:
        interests += dict[student]['interests']
        string += dict[student]['surname']
    return set(interests), len(string)

id, age = [], []
id_and_age()
people = list(zip(id, age))
print('ID студента - возраст: ',people)
surname_and_interests,long_surname = find(students)
print('Все интересы студентов:',surname_and_interests,'\nДлина всех фамилий студентов:',long_surname)
