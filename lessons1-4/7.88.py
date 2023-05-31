p = 6
a = [1, -5, -2, -4, 7, 3]
neg_count = 0
for num in a:
    if num < 0:
        neg_count += 1
print(neg_count > p)