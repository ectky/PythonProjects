n = int(input())
Max=int(input())

for i in range(1, n):
    num = int(input())
    Max = max(Max, num)

print(Max)
