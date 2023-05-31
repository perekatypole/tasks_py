def check_neighbor(seq):
    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            return i+1
    return -1

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14]
print(check_neighbor(seq))