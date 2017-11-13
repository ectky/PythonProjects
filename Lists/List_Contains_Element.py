l = [int(i) for i in input().split(' ')]
n = int(input())

contains = False

for i in l:
    if i == n:
        contains = True

print('yes' if contains else 'no')

