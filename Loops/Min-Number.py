n = int(input())
Min = int(input())

for i in range(1, n):
    num = int(input())
    Min = min(Min, num)
print(Min)
