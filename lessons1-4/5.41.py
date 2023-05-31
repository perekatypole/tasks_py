num = int(input())
p = int(input())
sum = 0
product = 1
while p > 0:
    digit = num % 10
    sum += digit
    product *= digit
    num //= 10
    p -= 1
print("Sum of last", p, "digits:", sum)
print("Product of last", p, "digits:", product)