a = 10
b = 5
while a != b:
    if a > b:
        print(b, b)
        a -= b
    else:
        print(a, a)
        b -= a
print(a, b)