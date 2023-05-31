b_list = [80, 101, 120, 95, 150] # список чисел
p = 5

# номер последнего числа больше 100
last_index = None
for i in range(p-1, -1, -1):
    if b_list[i] > 100:
        last_index = i
        break
print(last_index)