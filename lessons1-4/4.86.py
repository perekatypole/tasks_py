year_birth = int(input("Введите год рождения: "))
month_birth = int(input("Введите номер месяца рождения: "))
day_birth = int(input("Введите день рождения: "))
year_today = int(input("Введите текущий год: "))
month_today = int(input("Введите текущий месяц: "))
day_today = int(input("Введите текущий день: "))

age = year_today - year_birth
if month_birth > month_today or (month_birth == month_today and day_birth > day_today):
    age -= 1

print("Возраст:", age)