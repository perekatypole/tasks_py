p = 5 # примерное значение
dx = [10.0, 15.6, 20.7, 21.0, 22.5] # примерное значение
sum_d = sum([d for d in dx if d > 20.5])
print(sum_d < p)