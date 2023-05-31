d = sqrt((2 * R * h) + (h ** 2))
import math

R = 6350  # радиус Земли

for height in range(1, 11):
    distance = math.sqrt((2 * R * height * 1000) + (height * 1000) ** 2)
    print("Высота:", height, "км, Расстояние до линии горизонта:", round(distance / 1000, 2), "км")