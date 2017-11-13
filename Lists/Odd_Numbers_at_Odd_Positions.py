l = [int(item) for item in input().split(' ')]
count = 0

for i in range(len(l)):
    if i % 2 == 1 and (l[i] % 2 == 1 or l[i] % 2 == -1):
        print('Index {0} -> {1}'.format(i, l[i]))
