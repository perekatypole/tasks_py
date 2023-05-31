d_list = [4, -2, 7, 0, -10] # список чисел
k = 5

# номер последнего отрицательного числа
last_negative_index = None
for i in range(k-1, -1, -1):
    if d_list[i] < 0:
        last_negative_index = i
        break
print(last_negative_index)