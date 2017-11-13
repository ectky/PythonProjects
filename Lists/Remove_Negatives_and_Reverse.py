l = [int(i) for i in input().split(' ')]

l2 = []

for i in l:
    if i > 0:
        l2 += [i]

for i in range(len(l2)//2):
    helper = l2[i]
    l2[i] = l2[-1-i]
    l2[-1-i] = helper

if len(l2) > 0:
    for i in l2:
        print(i, end=' ')
else:
    print('empty')
