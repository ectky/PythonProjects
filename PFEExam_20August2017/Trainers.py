n = int(input())
teams = {'Technical': 0, 'Practical': 0, 'Theoretical': 0}

if n > 0:
    for i in range(n):
        distance_in_miles = int(input())
        cargo_in_tons = float(input())
        team = input()

        distance_in_meters = distance_in_miles * 1600
        cargo_in_kg = cargo_in_tons * 1000
        participant_earned_money = (cargo_in_kg * 1.5) - (0.7 * distance_in_meters * 2.5)

        if team in teams:
            teams[team] += participant_earned_money

    teams = sorted(teams.items(), key=lambda kv: kv[1], reverse=True)

    for team in teams:
        print('The {0} Trainers win with ${1:.3f}.'.format(team[0], team[1]))
        break
