elements_resistance = [10, 20, 30, 40]
total_resistance = sum(1/i for i in elements_resistance)**-1
print(total_resistance) # выведет 6.666666666666667