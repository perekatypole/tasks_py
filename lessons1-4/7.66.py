seq = [-4.5, -3.2, -1.0, 2.1, 3.5, -1.8, 0.5, 1.2]
num_negative = sum(1 for x in seq if x < 0)
print(num_negative)
