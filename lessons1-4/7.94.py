def local_maxima(seq):
    count = 0
    for i in range(1, len(seq)-1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            count += 1
    return count

seq = [1, 2, 3, 2, 1, 4, 3, 2, 5, 3, 2, 1]
print(local_maxima(seq))