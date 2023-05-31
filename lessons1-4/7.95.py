def sign_change(seq):
    count = 0
    for i in range(1, len(seq)):
        if seq[i] * seq[i-1] < 0:
            count += 1
    return count

seq = [10, -4, 12, 56, -4]
print(sign_change(seq))