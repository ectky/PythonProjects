l = [float(i) for i in input().split(' ')]

var = len(l)
cnt = 2
checked = True

while checked:
    checked = False
    for i in range(var-cnt):
        if l[i] == l[i+1]:
            l[i] = l[i] * 2
            l.pop(i+1)
            cnt += 1
            checked = True
            break

for i in l:
    print(i, end=' ')
