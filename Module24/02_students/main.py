from Students import Student

student_1 = Student('Иванов Иван', [4, 5, 4, 3, 4])
student_2 = Student('Столяров Станислав', [5, 5, 4, 5, 3])
student_3 = Student('Базанин Антон', [4, 3, 4, 3, 3])
student_4 = Student('Чумаков Егор', [4, 4, 4, 4, 5])
student_5 = Student('Троянов Павел', [3, 3, 4, 3, 4])
student_6 = Student('Сидорова Елена', [4, 5, 5, 4, 5])
student_7 = Student('Чуракова Жанна', [4, 5, 5, 5, 5])
student_8 = Student('Иванова Света', [5, 5, 5, 5, 4])
student_9 = Student('Глазунова Наталья', [4, 5, 4, 5, 5])
student_10 = Student('Воронцова Рая', [5, 5, 5, 3, 4])

students = [student_1,student_2,student_3,student_4,student_5,
            student_6,student_7, student_8,student_9,student_10]

students.sort(key = lambda x : x.give_average(), reverse=True)


print('Отсортированный список студентов по среднему баллу\n')
for student in students:
    student.print_info()
