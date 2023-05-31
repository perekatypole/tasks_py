numbers = [5.2, 14.8, 6.3, 10.5, 12, 20, 3, 8.9, 11, 9.7, 18.5, 7, 16, 4.1, 2.8]
avg_over_10 = sum([num for num in numbers if num > 10])/len([num for num in numbers if num > 10])

print("Average of numbers over 10:", avg_over_10)