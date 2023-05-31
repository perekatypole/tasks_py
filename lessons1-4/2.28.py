import math
a = int(input())
b = int(input())
k = int(input())
s = 1/2 * (b * b - a * a) * math.tan(k)
print(s)