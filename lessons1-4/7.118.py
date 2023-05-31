a_list = [4, 5, 8, 10, 2, 10, 1] # список чисел
p = 7

# а) номер последнего числа равного 10
last_index_of_10 = None
for i in range(p-1, -1, -1):
    if a_list[i] == 10:
        last_index_of_10 = i
        break
print(last_index_of_10)

# б) номер первого числа равного 10
first_index_of_10 = None
for i in range(p):
    if a_list[i] == 10:
        first_index_of_10 = i
        break
print(first_index_of_10)