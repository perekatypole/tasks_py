number = 12340980
zero_count = str(number).count('0')
nine_count = str(number).count('9')
if zero_count > nine_count:
    print("В этом числе чаще встречается 0")
elif zero_count < nine_count:
    print("В этом числе чаще встречается 9")
else:
    print("В этом числе 0 и 9 встречаются одинаковое количество раз")