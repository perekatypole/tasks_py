heights = [170, 167, 165, 162, 160, 159, 158, 157, 155, 152, 150, 148, 145, 142, 140]
new_height = 156
rank = 1
for height in heights:
    if new_height > height:
        rank += 1
    else:
        break
print("Место в перечне ростов: ", rank)