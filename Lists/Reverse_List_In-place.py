l = [int(i) for i in input().split(' ')]

for i in range(len(l)//2):
    helper = l[i]
    l[i] = l[-1-i]
    l[-1-i] = helper

for i in l:
    print(i, end=' ')
