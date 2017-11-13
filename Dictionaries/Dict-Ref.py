string = input()
dict = {}
unique = []

while string != 'end':
    list = [item for item in string.split(' = ')]
    key = list[0]

    try:
        value = int(list[1])
        if key not in unique:
            unique.append(key)
        dict[key] = value
    except:
        if list[1] in dict:
            value = dict[list[1]]
            if key not in unique:
                unique.append(key)
            dict[key] = value
        else:
            string = input()
            continue


    string = input()

for i in unique:
    print('{} === {}'.format(i, dict[i]))
