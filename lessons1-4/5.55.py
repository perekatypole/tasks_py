from math import sin, pi

T = 2
h = 1
n = 1000
dx = T / n
area = 0
for i in range(n):
    x1 = i * dx
    x2 = x1 + dx
    y1 = h * sin(2 * pi * x1 / T)
    y2 = h * sin(2 * pi * x2 / T)
    area += (y1 + y2) * dx / 2
print(area)