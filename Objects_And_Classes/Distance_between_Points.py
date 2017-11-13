class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def read_point(points):
    points = [int(item) for item in points.split(' ')]
    x = points[0]
    y = points[1]
    return Point(x, y)

import math


def calc_distace(p1, p2):
    a = abs(p1.x - p2.x)
    b = abs(p1.y - p2.y)
    c2 = pow(a, 2) + pow(b, 2)
    c = math.sqrt(c2)
    return c


points1 = input()
point1 = read_point(points1)
points2 = input()
point2 = read_point(points2)
print('{}'.format(calc_distace(point1, point2)))


