import datetime

k = int(input("Введите число k: "))
date = datetime.date(datetime.date.today().year, 1, 1) + datetime.timedelta(k-1)
if date.weekday() == 5 or date.weekday() == 6:
    print("Выходной день")
else:
    print("Рабочий день")