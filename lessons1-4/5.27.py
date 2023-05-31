sum_ = 0
for i in range(200, 601):
    sum_ += i
print(sum_)
a = int(input("Введите значение a: "))
sum1 = 0
for i in range(a, 401):
    sum1 += i
print(sum1)
b = int(input("Введите значение b: "))
sum2 = 0
for i in range(-15, b+1):
    sum2 += i
print(sum2)
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
if b < a:
    print("Ошибка! b должно быть больше чем a.")
else:
    n = b - a + 1  # количество чисел в диапазоне
    sum4 = (a + b) * n / 2  # формула для суммы
    print(sum4)