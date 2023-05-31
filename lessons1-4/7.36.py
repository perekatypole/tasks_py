district_areas = [100, 120, 130, 105, 95, 110, 115, 125, 140, 150]
district_yields = [50, 55, 60, 45, 40, 53, 58, 62, 70, 75]
total_wheat_yield = sum(district_areas[i] * district_yields[i] for i in range(len(district_areas)))
avg_district_yield = sum(district_yields) / len(district_yields)
print(f"Количество пшеницы, собранное в области: {total_wheat_yield} центнеров")
print(f"Средняя урожайность по области: {avg_district_yield} центнеров")