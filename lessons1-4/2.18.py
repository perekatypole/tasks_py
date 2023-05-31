import math
x = int(input())
y = int(input())
a = x + ((2 + y) / x * x)
b = y + (1 / math.sqrt(x * x + 10))
q = 7.25 * math.sin(x) - abs(y)
print(a / b, q)
