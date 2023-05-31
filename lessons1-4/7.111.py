heights = [168, -160, 170, -155, 172, 175, 180, -155, 172, 173, 165, 169]
avg_male_height = sum([h for h in heights if h < 0])/len([h for h in heights if h < 0])
avg_female_height = sum([h for h in heights if h >= 0])/len([h for h in heights if h >= 0])

print("Average male height:", avg_male_height)
print("Average female height:", avg_female_height)
