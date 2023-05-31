count = 0
for i in range(500, 1500):
    if i % 13 == 0 or i % 17 == 0:
        print(i)
        count += 1
        if count == 20:
            break