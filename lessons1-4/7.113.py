x = 5
nums = [7, 3, 6, 8, 9, 10, 2, 1, 4, 5, 12, 13]
p = 6

nums_gt_p = [num for num in nums if num > p]
if len(nums_gt_p) > 0:
    avg_gt_p = sum(nums_gt_p)/len(nums_gt_p)
    print("Average of numbers greater than p:", avg_gt_p)
else:
    print("No numbers greater than p.")