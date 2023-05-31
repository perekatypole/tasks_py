t = int(input("Enter a natural number: "))
nums = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]
nums_multiple_p = [num for num in nums if num % p == 0]
mean_multiple_p = sum(nums_multiple_p) / len(nums_multiple_p)
print(mean_multiple_p)