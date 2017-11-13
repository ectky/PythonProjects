num = int(input())

continents = {}
unique = []

for i in range(num):
    line = input().split(' ')
    continent, country, city = line[0], line[1], line[2]
    if continent in continents:
        if country in continents[continent]:
            if city in continents[continent][country]:
                continue
            else:
                continents[continent][country].append(city)
        else:
            continents[continent][country] = [city]
    else:
        continents[continent] = {country: [city]}
        unique.append(continent)

for cont in unique:
    print('{}:'.format(cont))
    for count in continents[cont]:
        print('  {} -> {}'.format( count, ', '.join(continents[cont][count])))

