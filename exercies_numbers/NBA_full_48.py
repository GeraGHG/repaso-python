def nba_extrap(points_game, minutes_game):
    if minutes_game == 0:
        return 0
    elif minutes_game > 48:
        print("Enter on time minus to 48")
    return points_game * 48 / minutes_game
