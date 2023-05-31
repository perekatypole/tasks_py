number = 12345

# Знакочередующаяся сумма цифр
sum = 0
for i in range(len(str(number))):
    digit = int(str(number)[i])
    sum += ((-1)**i) * digit
print("Знакочередующаяся сумма цифр:", sum)
# Знакочередующаяся сумма цифр без первой и последней
sum = 0
for i in range(1, len(str(number))-1):
    digit = int(str(number)[i])
    sum += ((-1)**i) * digit
print("Знакочередующаяся сумма цифр без первой и последней:", sum)