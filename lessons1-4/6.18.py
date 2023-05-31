import math

# Цикл с предусловием
a = 10
b = 5
while a > b:
    print(math.sqrt(a))
    a -= 1

# Цикл с постусловием
a = 10
b = 5
while True:
    print(math.sqrt(a))
    a -= 1
    if a <= b:
        break