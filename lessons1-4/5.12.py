import math

p0 = 1.29  # плотность воздуха на уровне моря
z = 1.25e-4  # постоянная

for height in range(0, 1001, 100):
    density = p0 * math.exp(-height * z)
    print("Высота:", height, "м, Плотность воздуха:", round(density, 2), "кг/м^3")