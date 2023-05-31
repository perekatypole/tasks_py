t = 5
av = [3, 6, 10, 15, 12]
r = 3
count = 0
for num in av:
    if num > t and num % r == 0:
        count += 1
print(count > 0)