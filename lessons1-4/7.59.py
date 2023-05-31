grades = [5, 4, 3, 5, 2, 5, 4, 3, 4]
count_of_5 = 0
for i in range(len(grades)):
    if grades[i] == 5:
        count_of_5 += 1
print("Количество пятерок:", count_of_5)