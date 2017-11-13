string = input()
dict = {}
unique = []

while string != 'shopping time':
    list = [i for i in string.split(' ')]
    key = list[1]
    value = int(list[2])
    if key in dict:
        dict[key] += value
    else:
        dict[key] = value
        unique.append(key)
    string = input()

string = input()
while string != 'exam time':
    list2 = [item for item in string.split(' ')]
    key = list2[1]
    value = int(list2[2])
    if key in dict:
        if dict[key] == 0:
            print('{} out of stock'.format(key))
        elif value > dict[key]:
            dict[key] = 0
        else:
            dict[key] -= value
    else:
        print('{} doesn\'t exist'.format(key))
    string = input()

for i in unique:
    if dict[i] > 0:
        print('{} -> {}'.format(i, dict[i]))
