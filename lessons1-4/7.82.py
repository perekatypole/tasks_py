p = 5
av = [1, 2, 3, 3, 4]

count_same = 0
count_zero = 0
count_even = 0
count_ending_five = 0

for i in range(p-1):
    if av[i] == av[i+1]:
        count_same += 1
    if av[i] == 0 or av[i+1] == 0:
        count_zero += 1
    if av[i] % 2 == 0 and av[i+1] % 2 == 0:
        count_even += 1
    if av[i+1] % 10 == 5:
        count_ending_five += 1

print("Количество пар «соседних» чисел а, равных между собой:", count_same)
print("Количество пар «соседних» чисел а, равных нулю:", count_zero)
print("Количество пар «соседних» чисел а, являющихся четными числами:", count_even)
print("Количество пар «соседних» чисел а., оканчивающихся на цифру 5:", count_ending_five)