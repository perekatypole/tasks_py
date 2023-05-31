removals = [("team_A", 5), ("team_B", 10), ("team_A", 2)]

team_A_count = sum(1 for t, d in removals if t == "team_A")
team_B_count = sum(1 for t, d in removals if t == "team_B")

team_A_time = sum(d for t, d in removals if t == "team_A")
team_B_time = sum(d for t, d in removals if t == "team_B")

print("Количество удалений команды A:", team_A_count)
print("Количество удалений команды B:", team_B_count)
print("Общее время удалений команды A:", team_A_time)
print("Общее время удалений команды B:", team_B_time)