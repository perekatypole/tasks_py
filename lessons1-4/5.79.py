def find_numbers_2():
    for i in range(1000, 10000):
        if i % 133 == 125 and i % 134 == 111:
            print(i)