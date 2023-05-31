grades = []
num_fives = 0
num_fours = 0
num_threes = 0
num_twos = 0
students_count = int(input("Введите количество учеников в классе: "))
for i in range(students_count):
    grade = int(input("Введите оценку ученика (от 2 до 5): "))
    grades.append(grade)
    if grade == 5:
        num_fives += 1
    elif grade == 4:
        num_fours += 1
    elif grade == 3:
        num_threes += 1
    elif grade == 2:
        num_twos += 1
print("Количество оценок 5:", num_fives)
print("Количество оценок 4:", num_fours)
print("Количество оценок 3:", num_threes)
print("Количество оценок 2:", num_twos)