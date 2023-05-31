x = 2
sum = 0
for i in range(0, 6):
    sum += ((-1)**i * (x**(2*i+1))) / (2*i+1)
print(sum)