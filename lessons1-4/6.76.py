def spiral_fence_length(a, b):
    if a == 0 or b == 0:
        return 0
    length = 2 * (a + b) - 4
    return length + spiral_fence_length(a - 2, b - 2)

length = spiral_fence_length(4, 6)
print(length) # 15