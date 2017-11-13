l = [int(i) for i in input().split(' ')]
n = int(input())
count = len(l)

while count != 0:
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            helper = l[i]
            l[i] = l[i+1]
            l[i+1] = helper
    count -= 1

for i in range(n):
    print(l[i], end=' ')
