from collections import Counter

sequence = [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 9, 9, 10, 11, 11, 11, 11, 12, 13]
counts = Counter(sequence)
duplicates = [(num, count) for num, count in counts.items() if count > 1]
print(duplicates)