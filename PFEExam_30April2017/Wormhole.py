wormholes = [int(item) for item in input().split(' ')]
i, steps = 0, 0

while i < len(wormholes):
    if wormholes[i] == 0:
        steps += 1
        i += 1
    else:
        helper = i
        i = wormholes[i]
        wormholes[helper] = 0

print(steps)

