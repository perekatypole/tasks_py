p = 10
a = [1]
for k in range(1, p+1):
    a_k = a[k-1] * k + 1/k
    a.append(a_k)
print(a)