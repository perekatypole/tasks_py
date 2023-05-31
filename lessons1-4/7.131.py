sequence = [1, 3, 3, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10, 11, 12, 12, 12, 12, 15, 16]
count = 0
for i in range(len(sequence)-1):
    if sequence[i] == sequence[i+1]:
        count += 1
print(count)