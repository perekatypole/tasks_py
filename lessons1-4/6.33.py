crop_yield = 20
crop_area = 100
year = 1
total_yield = 0
while crop_yield <= 22:
    crop_yield *= 1.02
    year += 1
print("Crop yield will exceed 22 tons per hectare in", year, "years")

crop_yield = 20
crop_area = 100
year = 1
total_yield = 0
while crop_area <= 120:
    crop_area *= 1.05
    year += 1
print("The crop area will exceed 120 hectares in", year, "years")

crop_yield = 20
crop_area = 100
year = 1
total_yield = 0
while total_yield <= 800:
    total_yield += (crop_area * crop_yield)
    crop_yield *= 1.02
    crop_area *= 1.05
    year += 1
print("The total crop yield will exceed 800 tons in", year, "years")