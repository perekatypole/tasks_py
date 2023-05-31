nums = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]
nums_gt_20 = [num for num in nums if num > 20]
mean_gt_20 = sum(nums_gt_20) / len(nums_gt_20)
print(mean_gt_20)