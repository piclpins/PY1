list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

players_in_team = len(list_players) // 2
team1 = list_players[:players_in_team]
team2 = list_players[players_in_team:]

print(team1, team2, sep='\n')
