p = 5
a = [4, 8, 10, 15, 17, 23, 25, 28, 35, 42, 48, 50]

# Count numbers greater than p
greater_than_p = len([i for i in a if i > p])
print("Number of elements greater than", p, ":", greater_than_p)

# Count numbers ending in 5
ends_with_5 = len([i for i in a if str(i)[-1] == '5'])
print("Number of elements ending with 5:", ends_with_5)

# Count numbers divisible by k
k = 5
divisible_by_k = len([i for i in a if i % k == 0])
print("Number of elements divisible by", k, ":", divisible_by_k)