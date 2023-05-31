games = []
matches_count = 20
for i in range(matches_count):
    goals_scored = int(input("Введите количество забитых мячей: "))
    goals_lost = int(input("Введите количество пропущенных мячей: "))
    games.append((goals_scored, goals_lost))
games_with_difference_more_three = 0
for i in range(matches_count):
    if abs(games[i][0] - games[i][1]) >= 3:
        games_with_difference_more_three += 1
print("Количество игр с разностью забитых и пропущенных мячей больше или равной 3:", games_with_difference_more_three)