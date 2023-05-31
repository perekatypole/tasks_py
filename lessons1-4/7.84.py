a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = [-4, 0, 2, 5, -1, 3, -4, 7, -2, -1]

count_pos = 0

if a1 > 0:
    count_pos += 1
if a2 > 0:
    count_pos += 1
if a3 > 0:
    count_pos += 1
if a4 > 0:
    count_pos += 1
if a5 > 0:
    count_pos += 1
if a6 > 0:
    count_pos += 1
if a7 > 0:
    count_pos += 1
if a8 > 0:
    count_pos += 1
if a9 > 0:
    count_pos += 1
if a10 > 0:
    count_pos += 1

if count_pos <= 5:
    print("Количество положительных чисел не превышает 5")
else:
    print("Количество положительных чисел больше 5")