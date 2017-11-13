l = [float(i) for i in input().split(' ')]
multiplier = float(input())

l2 = []

for i in l:
    l2 += [i * multiplier]

for i in l2:
    if len(str(i)) in range(8,12):
        print(i, end=' ')
    else:
        print('%g' %i, end=' ')
