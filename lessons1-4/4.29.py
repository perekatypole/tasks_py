number = int(input("Введите двузначное число: "))
sum_of_digits = (number // 10) + (number % 10)

if sum_of_digits % 3 == 0:
    print("Сумма цифр кратна трем")
else:
    print("Сумма цифр не кратна трем")

if sum_of_digits == number:
    print("Сумма цифр равна числу")
else:
    print("Сумма цифр не равна числу")

    print("Число не является палиндромом")