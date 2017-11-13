import math
l = [int(i) for i in input().split(' ')]

l2 = []

for i in l:
    if i >= 0:
        if math.sqrt(i) == int(math.sqrt(i)):
            l2 += [i]

l2.sort(reverse=True)
for i in l2:
    print(i, end=' ')
