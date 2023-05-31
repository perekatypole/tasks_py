p = int(input("Введите натуральное число p: "))
a = []
for i in range(p):
    a.append(float(input(f"Введите число a{i+1}: ")))
average = sum(a) / len(a)
print(average)