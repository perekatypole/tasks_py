numbers = [1, 5, 7, 9, 10]

found_even = False

for num in numbers:
    if num % 2 == 0:
        found_even = True
        break

if found_even:
    print("В заданном наборе есть хотя бы одно четное число")
else:
    print("В заданном наборе нет четных чисел")