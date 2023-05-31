seq = [3, 2, 2, 1, 5, 6, 6, 6, 8, 9, 7]
num_eq_elements = sum(1 for i, x in enumerate(seq) if x == seq[i-1] and i > 0)
print(num_eq_elements)