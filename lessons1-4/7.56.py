p = 5 # примерное значение
c = [2, 4, 6, 8, 10] # примерное значение
sum_c = sum([i for i in c if i <= p])
print(sum_c % p == 0)