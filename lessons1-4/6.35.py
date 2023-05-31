num = 1234578
count_3 = 0
count_even = 0
sum_gt_five = 0
prod_gt_seven = 1
count_0_5 = 0

last_digit = num % 10
while num > 0:
    digit = num % 10
    if digit == 3:
        count_3 += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_gt_five += digit
    if digit > 7:
        prod_gt_seven *= digit
    if digit == 0 or digit == 5:
        count_0_5 += 1
    num //= 10

print("Count of 3s: ", count_3)
print("Last digit: ", last_digit)
print("Count of evens: ", count_even)
print("Sum of digits greater than 5: ", sum_gt_five)
print("Product of digits greater than 7: ", prod_gt_seven)
print("Count of 0s and 5s: ", count_0_5)