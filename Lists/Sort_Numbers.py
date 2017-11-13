l = [float(i) for i in input().split(' ')]

l = sorted(l)

for i in range(len(l) - 1):
    print(l[i], end=' <= ')
print(l[-1])
