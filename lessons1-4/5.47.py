k = 5  # номер искомого элемента
frac = [(1, 1), (2, 1)]  # первые два элемента
for i in range(2, k):
    numerator = frac[i-1][0] + frac[i-2][0]  # числитель
    denominator = frac[i-1][1] + frac[i-2][1]  # знаменатель
    frac.append((numerator, denominator))
print(frac[k-1])  # k-ый элемент
print(frac[:k])  # первые k элементов