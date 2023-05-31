total_rainfall = 0
for i in range(1, 32):
    if i % 2 == 0:
        daily_rainfall = int(input(f"How many mm of rain fell on day {i}? "))
        total_rainfall += daily_rainfall
print(f"Total rainfall on even days: {total_rainfall}")