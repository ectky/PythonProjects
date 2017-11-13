import math
n = int(input())

space = n
star = 2*n

print('*' * star + ' ' * space + '*' * star)

for i in range(2, n):
    if i == math.ceil(n/2):
        print('*' + '/' * (star - 2) + '*' + '|' * n + '*' + '/' * (star - 2) + '*')
    else:
        print('*' + '/' * (star - 2) + '*' + ' ' * n + '*' + '/' * (star - 2) + '*')


print('*' * star + ' ' * space + '*' * star)
