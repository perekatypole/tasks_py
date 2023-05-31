price_per_kg = float(input("Введите стоимость 1 кг сыра: "))
for weight in range(50, 1050, 50):
    price = price_per_kg / 1000 * weight
    print(f"{weight} г сыра стоят {price} рублей"