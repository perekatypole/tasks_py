p = int(input("Введите натуральное число p: "))
sum_ = 0
for i in range(1, 2*p+1, 2):
    sum_ += i**2
print(sum_)