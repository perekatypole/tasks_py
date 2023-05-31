number = int(input("Введите трехзначное число: "))
sum_of_cubes = (number // 100) ** 3 + ((number // 10) % 10) ** 3 + (number % 10) ** 3

if number ** 2 == sum_of_cubes:
    print("Квадрат числа равен сумме кубов его цифр")
else:
    print("Квадрат числа не равен сумме кубов его цифр")
