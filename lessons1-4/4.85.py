k = int(input("Введите натуральное число k: "))
if k % 10 == 1 and k != 11:
    print("Мы нашли", k, "гриб в лесу")
elif 2 <= k % 10 <= 4 and (k < 10 or k > 20):
    print("Мы нашли", k, "гриба в лесу")
else:
    print("Мы нашли", k, "грибов в лесу")