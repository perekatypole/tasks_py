count = 0
for i in range(100, 1000):
    if i % 19 == 0:
        print(i)
        count += 1
        if count == 15:
            break