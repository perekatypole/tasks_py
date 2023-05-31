residents = [52, 38, 21, 45, 29, 34, 27, 56, 67, 49]
total_residents_odd = 0
total_residents_even = 0
for i in range(len(residents)):
    if i % 2 == 0:
        total_residents_even += residents[i]
    else:
        total_residents_odd += residents[i]
if total_residents_odd > total_residents_even:
    print("Больше жителей живет на стороне нечетных домов")
else:
    print("Больше жителей живет на стороне четных домов")