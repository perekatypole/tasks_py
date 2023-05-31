t = 6
d = [2, 3, -6, 8, 12, -9]
pos_count = 0
for num in d:
    if num > 0 and num % 3 == 0:
        pos_count += 1
print(pos_count == t)