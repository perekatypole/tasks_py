points = []
wins = 0
losses = 0
draws = 0
games_count = int(input("Введите количество сыгранных матчей: "))
for i in range(games_count):
    game_points = int(input("Введите количество очков в матче (0 - проигрыш, 1 - ничья, 3 - победа): "))
    if game_points == 3:
        wins += 1
    elif game_points == 0:
        losses += 1
    elif game_points == 1:
        draws += 1
    points.append(game_points)
print("Количество выигрышей:", wins)
print("Количество проигрышей:", losses)
print("Количество ничьих:", draws)