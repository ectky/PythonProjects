l = [int(i) for i in input().split(' ')]
l.sort()
i = 0

while i < len(l):
    num = l[i]
    count = 1
    while i + count < len(l) and l[i + count] == num:
        count += 1
    i = i + count
    print('{0} -> {1}'.format(num, count))
