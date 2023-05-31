heights = [170, 165, 180, 158, 173, 169, 162, 150, 181, 164, 168, 175]
short_heights = len([h for h in heights if h < 165])
print("Number of students with height less than 165cm:", short_heights)