p = 10
cv = [3, 4, 10, 18, 20, 25, 27, 30, 40, 50]
count = 0
for c in cv:
    if c < 20:
        count += 1
print(count == 5)