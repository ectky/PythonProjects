n = int(input())

f0 = 1
f1 = 1
sum = 0

if n <= 1:
    print(1)
else:
    for i in range(n-1):
        sum = f0 + f1
        f0 = f1
        f1 = sum
    print(sum)



