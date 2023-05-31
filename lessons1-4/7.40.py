numbers = [10.5, 15.2, 16.8, 9.3, 7.4, 11.0, 20.7] # вещественные числа а1, а2, ..., ап
sum_above_10_75 = sum([number for number in numbers if number > 10.75])
print("Сумма чисел, больших 10.75: ", sum_above_10_75)