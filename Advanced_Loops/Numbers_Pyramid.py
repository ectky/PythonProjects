n = int(input())

num = 0

for i in range(1, 1000000000000000000000000000):
    for j in range(1, i+1):
        num += 1
        if num <= n:
            print(num, end=' ')
        else:
            break
    print()
    if(num > n):
        break
