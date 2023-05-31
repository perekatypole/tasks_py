import math

r = 5 # радиус круга
a = 4 # сторона квадрата

s_circle = math.pi * r ** 2 # площадь круга
s_square = a ** 2 # площадь квадрата

if s_circle > s_square:
    print("Площадь круга больше")
else:
    print("Площадь квадрата больше")