nums = [2.3, -4.1, 5.5, -1.2]
neg_count = sum(1 for num in nums if num < 0)
print(neg_count)