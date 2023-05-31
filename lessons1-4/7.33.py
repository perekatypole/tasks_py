jan_precip = [5, 10, 8, 6, 7, 11, 12, 15, 9, 7, 6, 4]
mar_precip = [3, 6, 4, 5, 8, 9, 11, 13, 10, 6, 5, 4]
avg_jan_precip = sum(jan_precip) / len(jan_precip)
avg_mar_precip = sum(mar_precip) / len(mar_precip)
print(f"Среднедневное количество осадков за январь: {avg_jan_precip}")
print(f"Среднедневное количество осадков за март: {avg_mar_precip}")