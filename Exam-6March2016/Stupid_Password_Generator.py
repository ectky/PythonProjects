n = int(input())
l = int(input())

for i in range(1, n):
    for j in range(1, n):
        for k in range(ord('a'), ord('a') + l):
            for m in range(ord('a'), ord('a') + l):
                for o in range(1, n+1):
                    if o > i and o > j:
                        print('{0}{1}{2}{3}{4}'.format(i, j, chr(k) ,chr(m), o) , end=' ')


