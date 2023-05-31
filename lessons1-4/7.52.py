values = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
over_20 = [x for x in values if x > 20]
less_than_50 = [x for x in values if x < 50]
sum_over_20 = sum(over_20)
sum_less_than_50 = sum(less_than_50)

if sum_over_20 > 100:
    print(f"The sum of values over 20 ({sum_over_20}) is greater than 100.")
else:
    print(f"The sum of values over 20 ({sum_over_20}) is not greater than 100.")

if sum_less_than_50 % 2 == 0:
    print(f"The sum of values less than 50 ({sum_less_than_50}) is an even number.")
else:
    print(f"The sum of values less than 50 ({sum_less_than_50}) is not an even number.")