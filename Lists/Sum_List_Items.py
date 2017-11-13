n = int(input())

l = []
sum = 0

for i in range(n):
    l += [int(input())]

for i in l:
    sum += i

print(sum)
