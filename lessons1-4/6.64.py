import math

num = int(input())
denoms = [64, 32, 16, 8, 4, 2, 1]
i = 0
count = 0

while num > 0:
  count += math.floor(num / denoms[i])
  num %= denoms[i]
  i += 1

print(count)