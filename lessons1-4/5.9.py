price = 20.4  # стоимость одной штуки товара

for quantity in range(2, 21):
    total_price = price * quantity
    print(quantity, round(total_price, 2))  # округляем до 2 знаков после запятой