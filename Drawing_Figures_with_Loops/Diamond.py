import math
n = int(input())

minus = 0
star = 0
middle_minus = 0

if n == 1:
    print('*')
elif n%2 == 0:
    star = 2
    minus = (n - star)//2
    print('-' * minus + '*' * star + '-' * minus)

    middle_minus = 2
    star = 1
    minus -= 1
    for i in range(n//2 - 1):
        print('-' * minus + '*' * star + '-' * middle_minus + '*' * star + '-' * minus)
        minus -= 1
        middle_minus += 2

    minus+=2
    middle_minus -= 4
    for i in range(n//2 - 1):
        print('-' * minus + '*' * star + '-' * middle_minus + '*' * star + '-' * minus)
        minus += 1
        middle_minus -= 2
else:
    star = 1
    minus = (n - star)//2
    print('-' * minus + '*' * star + '-' * minus)

    middle_minus = 1
    minus -= 1
    for i in range(n//2):
        print('-' * minus + '*' * star + '-' * middle_minus + '*' * star + '-' * minus)
        minus -= 1
        middle_minus += 2

    minus += 2
    middle_minus -= 4
    for i in range(n//2 - 1):
        print('-' * minus + '*' * star + '-' * middle_minus + '*' * star + '-' * minus)
        minus += 1
        middle_minus -= 2

    star = 1
    minus = (n - star)//2
    print('-' * minus + '*' * star + '-' * minus)
