letters = [item for item in input()]

counter = {}
unique = []

for i in letters:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
        unique.append(i)

for key in unique:
    print('{0} -> {1}'.format(key, counter[key]))
