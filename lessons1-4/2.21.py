import math
e = int(input())
f = int(input())
g = int(input())
h = int(input())
a = (e + (f / 2)) / 3
b = abs(h * h - g)
k = ((g - h) ** 2) - 3 * math.sin(e)
c =  math.sqrt(k)
print(a, "\n", b, "\n", c)