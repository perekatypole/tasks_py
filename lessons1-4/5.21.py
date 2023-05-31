price_per_kg = float(input("Введите стоимость 1 кг конфет: "))

for weight in range(100, 2100, 100):
    price = price_per_kg / 1000 * weight
    print(f"{weight} г конфет стоят {price} рублей")