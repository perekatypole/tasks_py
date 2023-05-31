numbers = [1.2, 2.5, 3.7, 4.8, 5.1, 6.3, 7.4, 8.6, 9.2, 10.3, 11.1, 12.5, 13.9, 14.7, 15.4]
number_p = 7.8
sum_numbers = sum([number for number in numbers if number < number_p])
print("Сумма чисел последовательности, меньших", number_p, ": ", sum_numbers)