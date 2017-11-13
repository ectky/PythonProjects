n = int(input())

space = n-1
star = 1

for i in range(n):
    print(' ' * space + '* ' * star)
    space -= 1
    star += 1

space += 2
star -= 2

for i in range(n-1):
    print(' ' * space + '* ' * star)
    space += 1
    star -= 1
