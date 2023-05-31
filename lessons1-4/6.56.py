number = 9825732
if '2' in str(number) and '5' in str(number):
    two_index = str(number).index('2')
    five_index = str(number).index('5')
    if two_index < five_index:
        print("Цифра 2 расположена в числе левее, чем цифра 5")
    elif two_index > five_index:
        print("Цифра 5 расположена в числе левее, чем цифра 2")
    else:
        print("Цифры 2 и 5 расположены на одной позиции")
else:
    print("В числе нет цифр 2 и 5")