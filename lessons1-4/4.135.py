month = int(input("Введите порядковый номер месяца: "))

if month == 2:
    days = 28
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 31

print(f"В месяце {month} - {days} дней")