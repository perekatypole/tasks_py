import numpy as np

numbers = [4, 6, 2, 8, 3, 7, 9999]

for i in range(len(numbers)-1):
  if numbers[i] % 2 == 0 and numbers[i+1] % 2 == 0:
    print("Пара соседних четных чисел: ", numbers[i], numbers[i+1])
    print("Порядковый номер первого числа: ", i+1)
    break
else:
  print("В последовательности нет пары соседних четных чисел")