num = 123456789
a = int(input("Enter a (0 < a < 8): "))
count_a = 0
sum_gt_a = 0

while num > 0:
    digit = num % 10
    if digit == a:
        count_a += 1
    if digit > a:
        sum_gt_a += digit
    num //= 10

print("Count of", a, ": ", count_a)
print("Sum of digits greater than", a, ": ", sum_gt_a)