import math
figure = input()

if figure == 'square':
    a = float(input())
    area = a * a
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif figure == 'circle':
    r = float(input())
    area = math.pi * r * r
elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2

print('{0:.3f}'.format(area))
