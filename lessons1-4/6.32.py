distance = 10
total_distance = 10
day = 1
while distance <= 20:
    distance *= 1.1
    day += 1
print("The skier will run over 20 kilometers on day", day)

distance = 10
total_distance = 10
day = 1
while total_distance <= 100:
    distance *= 1.1
    total_distance += distance
    day += 1
print("The skier will travel over 100 kilometers in", day, "days")