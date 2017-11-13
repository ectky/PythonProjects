import math
n = int(input())

minus = 0
star = 0

if n%2 == 0:
    star = 2
    minus = (n - star)//2
    for i in range(n//2):
        print('-' * minus + '*' * star + '-' * minus)
        star += 2
        minus = (n - star)//2
    for i in range(n//2):
        print('|' + '*' * (n-2) + '|')

else:
    star = 1
    minus = (n - star)//2
    for i in range(math.ceil(n/2)):
        print('-' * minus + '*' * star + '-' * minus)
        star += 2
        minus = (n - star)//2
    for i in range(math.floor(n/2)):
        print('|' + '*' * (n-2) + '|')
