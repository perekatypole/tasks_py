teams = {'Team1': [10, 5], 'Team2': [8, 7], 'Team3': [6, 10], 'Team4': [10, 2]}
num_teams_winning = sum(1 for team in teams.values() if team[0] > team[1])
print(num_teams_winning)