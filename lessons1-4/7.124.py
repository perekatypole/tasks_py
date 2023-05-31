points = [52, 49, 45, 40, 36, 33, 30, 26, 23, 20, 17, 14, 11, 8, 5, 2, 0, 0, 0, 0]
n = 36
for i in range(len(points)):
    if points[i] == n:
        print("Место команды: ", i + 1)
        break