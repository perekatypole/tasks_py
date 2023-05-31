a = int(input("Введите час прибытия поезда: "))
b = int(input("Введите минуту прибытия поезда: "))
c = int(input("Введите час отправления поезда: "))
d = int(input("Введите минуту отправления поезда: "))
p = int(input("Введите час прихода пассажира на платформу: "))
t = int(input("Введите минуту прихода пассажира на платформу: "))

arrival_time = a * 60 + b
departure_time = c * 60 + d
passenger_time = p * 60 + t

if passenger_time <= arrival_time and passenger_time >= departure_time:
    print("Поезд стоит на платформе")
else:
    print("Поезд не стоит на платформе")