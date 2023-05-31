import math
a = int(input())
b = int(input())
x = ((2 / a * a + 25) + b) / math.sqrt(b) + ((a + b) / 2)
y = (abs(a) + 2 * math.sin(b)) / 5.5 * a
print(x, "\n",  y)
