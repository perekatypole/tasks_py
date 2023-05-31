import math
a = int(input()) # верхнее основание
b = int(input())  #нижние основание
h = int(input()) #высота
v = (b - a) / 2
sqrt = math.sqrt(v * v + h)
print(sqrt * 2 + a + b)