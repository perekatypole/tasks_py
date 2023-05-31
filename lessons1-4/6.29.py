count = 0
for i in range(100, 1000):
    if i % 9 == 0 and str(i)[-1] == '7':
        print(i)
        count += 1
        if count == 10:
            break