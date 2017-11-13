l = [int(i) for i in input().split(' ')]
swapped = True

while swapped:
    swapped = False
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            helper = l[i]
            l[i] = l[i+1]
            l[i+1] = helper
            swapped = True

for i in l:
    print(i, end=' ')
