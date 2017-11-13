import math

year = input().lower()
holidays = int(input())
weekedns = int(input())

sofia_weekends = 48 - weekedns
sofia_saturdays = sofia_weekends * 3.0 / 4
sofia_holidays = holidays * 2.0 /3
games = sofia_saturdays + weekedns + sofia_holidays

if year == 'leap':
    games += games * 0.15

print(math.floor(games))
