n = int(input())

space = n
star = 0

for i in range(n+1):
    print(' ' * space + '*' * star + ' | ' + '*' * star)
    space -= 1
    star += 1
