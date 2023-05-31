x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = [-3.5, 2.4, 33.2, 9.1, 18.0, 30.5, 35.6, 20.4, 5.3, 40.0, 29.1, -1.7, 12.5, 8.6, 15.8]

count_less_than_33_2_multiple_4 = 0

if x1 <= 33.2 and x1 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x2 <= 33.2 and x2 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x3 <= 33.2 and x3 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x4 <= 33.2 and x4 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x5 <= 33.2 and x5 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x6 <= 33.2 and x6 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x7 <= 33.2 and x7 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x8 <= 33.2 and x8 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x9 <= 33.2 and x9 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x10 <= 33.2 and x10 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x11 <= 33.2 and x11 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x12 <= 33.2 and x12 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x13 <= 33.2 and x13 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x14 <= 33.2 and x14 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1
if x15 <= 33.2 and x15 % 4 == 0:
    count_less_than_33_2_multiple_4 += 1

if count_less_than_33_2_multiple_4 > 0:
    print("Количество чисел, которые не больше 33.2 и кратны 4, больше нуля")
else:
    print("Количество чисел, которые не больше 33.2 и кратны 4, равно нулю")