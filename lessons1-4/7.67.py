seq = [2.4, -1.5, 3.0, 0, 5.2, -2.1, 4.4]
num_before_zero = next((i for i, x in enumerate(seq) if x == 0), len(seq))
print(num_before_zero)