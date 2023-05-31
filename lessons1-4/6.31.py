deposit = 1000.0
increment = 0.02
increase_month = 0
while deposit < 1200:
    deposit *= (1 + increment)
    increase_month += 1
print("The deposit will exceed 1200 rubles in", increase_month, "months")

deposit = 1000.0
increment = 0.02
increase_month = 0
while (deposit * increment) < 30:
    deposit *= (1 + increment)
    increase_month += 1
print("The monthly increment will exceed 30 rubles in", increase_month, "months")