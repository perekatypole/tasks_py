a = [3, 7, 8, 2, 4, 5]   # заданный список целых чисел

p = len(a)    # натуральное число п

if p % 2 == 0:    # проверяем, четное ли п
    s = [a[i] + a[p - i - 1] for i in range(p // 2)]   # если четное, используем сложение соответствующих элементов исходноего списка вместе с "перевернутым" списком второй половины
    print(s)
else:    # если нечетное
    s = [a[i] + a[p - i - 1] for i in range(p // 2)] + [a[p //2]]   # добавляем единственный средний элемент
    print(s)