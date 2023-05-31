import numpy as np

numbers = [1.2, 2.5, 3.7, 6.1, 5.3, 4.8, 7.2, 8.4, 9.9, 10.1, 11.3, 12.6, 14.7, 13.2, 15.9, 10000]

is_sorted = True
for i in range(len(numbers)-1):
  if numbers[i] > numbers[i+1]:
    is_sorted = False
    print("Порядковый номер первого числа, нарушающего упорядоченность: ", i+1)
    break
if is_sorted:
  print("Последовательность упорядоченная по возрастанию")