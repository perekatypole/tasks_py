number = 191283768
a = '1'
b = '3'
a_index = str(number).rfind(a)
b_index = str(number).rfind(b)
if a_index > b_index:
    print(f"Цифра {a} расположена в числе правее, чем цифра {b}")
elif a_index < b_index:
    print(f"Цифра {b} расположена в числе правее, чем цифра {a}")
else:
    print(f"Цифры {a} и {b} находятся на одной позиции")
