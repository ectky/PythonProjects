string = input()
dict = {}
unique = []

while string != 'Over':
    list = [item for item in string.split(' : ')]
    key = list[0]

    try:
        value = int(list[1])
        if key not in unique:
            unique.append(key)
        dict[key] = value
    except:
        value = int(list[0])
        key = list[1]
        if key not in unique:
            unique.append(key)
        dict[key] = value

    string = input()

for i in sorted(unique):
    print('{} -> {}'.format(i, dict[i]))
