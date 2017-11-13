import re
string = input()
pattern1 = r'.+ -> .+ : [0-9]+'
pattern2 = r'.+ = .+'
trains = {}

while string != 'It\'s Training Men!':
    if re.match(pattern1, string):
        string = string.split(' -> ')
        train = string[0]
        wagon_stuff = string[1].split(' : ')
        wagon, power = wagon_stuff[0], int(wagon_stuff[1])
        if train in trains:
            trains[train][wagon] = power
        else:
            trains[train] = {wagon: power}
    elif re.match(pattern2, string):
        string = string.split(' = ')
        train, other_train = string[0], string[1]
        trains[train] = {}
        for wagon in trains[other_train]:
            trains[train][wagon] = trains[other_train][wagon]
    else:
        string = string.split(' -> ')
        train, other_train = string[0], string[1]
        if train not in trains:
            trains[train] = {}
        for wagon in trains[other_train]:
            trains[train][wagon] = trains[other_train][wagon]
        trains.pop(other_train)
    string = input()

totalWagonPower = dict()
for train in trains:
    temp = trains[train].values()
    totalWagonPower[train] = (-sum(temp), len(temp))
for train in sorted(totalWagonPower.keys(), key = lambda x: totalWagonPower[x]):
    print('Train: {0}'.format(train))
    for wagon in sorted(trains[train].items(), key = lambda x: (x[1]), reverse = True):
            print('###{0} - {1}'.format(wagon[0], wagon[1]))
