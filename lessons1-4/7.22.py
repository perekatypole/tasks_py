set1 = [10, 20, 30, 40, 50, 60, 70, 80]
set2 = [15, 25, 35, 45, 55, 65, 75, 85]

if sum(set1) < sum(set2):
    print("Набор 1 дешевле")
elif sum(set1) == sum(set2):
    print("Цена наборов одинаковая")
else:
    print("Набор 2 дешевле")