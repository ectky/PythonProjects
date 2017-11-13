l = [i for i in input().split('|')]

l3 = []

for j in range(len(l)-1, -1, -1):
    l2 = [i for i in l[j].split(' ')]
    for i in l2:
        if i != '':
            l3 += [int(i)]

print(l3)
