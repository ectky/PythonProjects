n = int(input())

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0

for i in range(n):
    num = int(input())

    if num < 200:
         f1 += 1
    elif 200 <= num <= 399:
        f2 += 1
    elif 400 <= num <= 599:
        f3 += 1
    elif 600 <= num <= 799:
        f4 += 1
    elif num >= 800:
        f5 += 1

p1 = f1 / n * 100
p2 = f2 / n * 100
p3 = f3 / n * 100
p4 = f4 / n * 100
p5 = f5 / n * 100

print('{0:.2f}%\n{1:.2f}%\n{2:.2f}%\n{3:.2f}%\n{4:.2f}%\n'.format(p1,p2,p3,p4,p5))
