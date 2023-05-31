rate = float(input("Введите текущий курс доллара: "))

for dollars in range(1, 21):
    rubles = dollars * rate
    print("$", dollars, "=", round(rubles, 2), "руб.")