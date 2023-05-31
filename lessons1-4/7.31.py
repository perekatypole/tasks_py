sequence = [1, 2, 3, 4, -1]
avg_num = sum([x for x in sequence if x >= 0])/len([x for x in sequence if x >= 0])
print("Среднее арифметическое: ", avg_num)