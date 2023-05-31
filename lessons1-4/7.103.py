def sort_teams_by_points(teams_points_dict):
    return sorted(teams_points_dict, key=teams_points_dict.get, reverse=True)