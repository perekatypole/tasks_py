sequence = [1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 11, 12, 12, 12, 13, 14, 15, 15, 1000]
count = 0
for i in range(1, len(sequence)):
    if sequence[i] == sequence[i-1]:
        count += 1
print(count)