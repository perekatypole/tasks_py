points = []
games_count = int(input("Введите количество сыгранных матчей: "))
for i in range(games_count):
    game_points = int(input("Введите количество очков в матче (0 - проигрыш, 1 - ничья, 3 - победа): "))
    points.append(game_points)
total_points = sum(points)
print("Общее число очков:", total_points)