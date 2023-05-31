number = 123321
digits = [int(d) for d in str(number)]
if sum(digits[:3]) == sum(digits[3:]):
    print("Число", number, "является счастливым")
else:
    print("Число", number, "не является счастливым")