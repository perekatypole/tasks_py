sum_of_odds = 0
i = 1
while i % 2 != 0:
    num = int(input("Enter an odd number (enter an even number to stop): "))
    sum_of_odds += num
    i += 1
print(f"Sum of all odd numbers at the beginning of the sequence: {sum_of_odds}")