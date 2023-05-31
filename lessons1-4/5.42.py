d = 1.0
for i in range(2, 101):
    if i % 2 == 0:
        d += 1/i
    else:
        d -= 1/i
s = 0.5 + 1/3 - 1/4 + 1/5 - 1/6 + 1/7 - 1/8 + 1/9 - 1/10 + d
print("Distance from home:", s, "km")
print("Total distance:", 2*s, "km")