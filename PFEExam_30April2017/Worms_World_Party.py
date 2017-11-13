command = input()
teams = {}
team_scores = {}
team_len = {}
worms = []
sub = ''

while command != 'quit':
    list_of_commands = command.split(' -> ')
    worm_name, team_name, worm_score = list_of_commands[0], list_of_commands[1], int(list_of_commands[2])

    if worm_name not in worms:
        worms.append(worm_name)
        if team_name in teams:
            teams[team_name][worm_name] = worm_score
            team_scores[team_name] += worm_score
            team_len[team_name] += 1
        else:
            teams[team_name] = {worm_name: worm_score}
            team_scores[team_name] = worm_score
            team_len[team_name] = 1

    command = input()

team_new_scores = {}
for current_score in team_scores:
    for key in team_scores:
        if current_score != key:
            if team_scores[current_score] == team_scores[key]:
                team_new_scores[current_score] = team_scores[current_score] // team_len[current_score]
                team_new_scores[key] = team_scores[key] // team_len[key]
            else:
                team_new_scores[current_score] = team_scores[current_score]


teams_sorted_by_score = sorted(team_new_scores.items(), key=lambda kv: kv[1], reverse=True)




i = 1
for team in teams_sorted_by_score:
    print('{}. Team: {} - {}'.format(i, team[0], team_scores[team[0]]))

    worms_sorted_by_score = sorted(teams[team[0]].items(), key=lambda kv: kv[1], reverse=True)
    for worm in worms_sorted_by_score:
        print('###{} : {}'.format(worm[0], worm[1]))

    i += 1





