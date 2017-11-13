l = [item for item in input().split(' ')]
l2 = [l[len(l) - 1]]

for i in range(len(l) - 1):
    l2 += [l[i]]

for i in l2:
    print(i, end=' ')

