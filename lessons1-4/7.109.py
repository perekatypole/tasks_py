x = int(input("Enter a natural number: "))
nums = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
nums_gt_p = [num for num in nums if num > p]
mean_gt_p = sum(nums_gt_p) / len(nums_gt_p)
print(mean_gt_p)