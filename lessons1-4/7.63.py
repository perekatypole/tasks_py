grades = [5, 4, 3, 2, 4, 5, 5, 3, 2, 3, 4, 5, 4, 3, 5, 2, 2, 4, 4, 5]
fives = len([g for g in grades if g == 5])
twos = len([g for g in grades if g == 2])
print("Number of fives:", fives)
print("Number of twos:", twos)