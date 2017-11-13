locomotive_power = int(input())
wagons = []

wagon = input()

while wagon != 'All ofboard!':
    wagon = int(wagon)
    wagons.append(wagon)
    if sum(wagons) > locomotive_power:
        average = sum(wagons) // len(wagons)
        dict = {}
        for w in wagons:
            i = 0
            while True:
                if average == w + i or average == w - i:
                    element, count = w, i
                    dict[element] = count
                    break
                i += 1
        for el in sorted(dict.items(), key=lambda kv: kv[1]):
            wagons.remove(el[0])
            break
    wagon = input()

for wagon in reversed(wagons):
    print('{0}'.format(wagon), end=' ')
print('{0}'.format(locomotive_power))
