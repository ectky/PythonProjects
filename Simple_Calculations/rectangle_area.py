import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

upper_side =  math.fabs(x1 - x2)
right_side =  math.fabs(y2 - y1)
area = upper_side * right_side
perimeter = upper_side * 2 + right_side * 2

print(area)
print(perimeter)

