num = input("Введите число: ")
digits = [int(digit) for digit in num]

max_digits = sorted(digits)[-2:]
min_digits = sorted(digits)[:2]

max_indexes_rev = [len(digits)-1-i for i in range(len(digits)) if digits[i] in max_digits]
min_indexes_rev = [len(digits)-1-i for i in range(len(digits)) if digits[i] in min_digits]

max_indexes = [i for i in range(len(digits)) if digits[i] in max_digits]
min_indexes = [i for i in range(len(digits)) if digits[i] in min_digits]

print("Порядковые номера двух максимальных цифр, считая от конца: ", max_indexes_rev)
print("Порядковые номера двух максимальных цифр, считая от начала: ", max_indexes)
print("Порядковые номера двух минимальных цифр, считая от конца: ", min_indexes_rev)
print("Порядковые номера двух минимальных цифр, считая от начала: ", min_indexes)