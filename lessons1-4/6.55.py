number = 123456789
a = '2'
b = '5'
a_count = str(number).count(a)
b_count = str(number).count(b)
if a_count < b_count:
    print(f"Цифра {a} встречается в числе реже, чем цифра {b}")
else:
    print(f"Цифра {a} встречается в числе не реже, чем цифра {b}")