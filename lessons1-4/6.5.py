def find_max_number():
    max_num = 0
    for i in range(1, 5001):
        if i % 139 == 0:
            max_num = i
    return max_num