recipitations = [2, 5, 7, 4, 1, 0, 3, 8, 6, 9, 3, 2]
even_precipitations = 0
odd_precipitations = 0
for i in range(len(precipitations)):
    if i % 2 == 0:
        even_precipitations += precipitations[i]
    else:
        odd_precipitations += precipitations[i]
if even_precipitations > odd_precipitations:
    print("По четным числам больше осадков")
else:
    print("По нечетным числам больше осадков")