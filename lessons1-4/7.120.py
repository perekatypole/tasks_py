c_list = [35, 40, 25, 10, 25, 80] # список чисел
p = 6

# номер последнего числа равного 25
last_index_of_25 = None
for i in range(p-1, -1, -1):
    if c_list[i] == 25:
        last_index_of_25 = i
        break
print(last_index_of_25)