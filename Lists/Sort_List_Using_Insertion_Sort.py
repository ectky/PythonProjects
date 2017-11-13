l = [int(i) for i in input().split(' ')]

for i in range(len(l)):
    j = i
    while j > 0 and l[j-1] > l[j]:
        helper = l[j]
        l[j] = l[j-1]
        l[j-1] = helper
        j -= 1

for i in l:
    print(i, end=' ')
