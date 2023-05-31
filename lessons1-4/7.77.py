penalty_time_total_team_a = 0
penalty_time_total_team_b = 0
while True:
    penalty_time = int(input("Введите время удаления игрока (2, 5, 10 минут) или 0 для окончания игры: "))
    if penalty_time == 0:
        break
    team = input("Введите команду, в которой удален игрок (A или B): ")
    if team == "A":
        penalty_time_total_team_a += penalty_time
    elif team == "B":
        penalty_time_total_team_b += penalty_time
print("Общее число удалений команды A:", penalty_time_total_team_a)
print("Общее число удалений команды B:", penalty_time_total_team_b)