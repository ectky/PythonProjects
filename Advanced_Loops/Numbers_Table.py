n = int(input())

num = 0

for i in range(n):
    for j in range(n):
        num = i + j + 1
        if num <= n:
            print(num, end=' ')
        else:
            print(2*n - num, end=' ')
    print()


