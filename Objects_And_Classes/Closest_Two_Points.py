class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def read_point(points):
    points = [int(item) for item in points.split(' ')]
    x = points[0]
    y = points[1]
    return Point(x, y)

from math import sqrt


def calc_distace(p1, p2):
    a = abs(p1.x - p2.x)
    b = abs(p1.y - p2.y)
    c2 = pow(a, 2) + pow(b, 2)
    c = sqrt(c2)
    return c

def find_closest_points(points):
    min = 1000000000000000000
    point1 = Point(0, 0)
    point2 = Point(0, 0)
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                if min > calc_distace(p1, p2):
                    min = calc_distace(p1, p2)
                    point1 = p1
                    point2 = p2
    return min, point1, point2


n = int(input())
points = []

for i in range(n):
    point = read_point(input())
    points.append(point)

distance, p1, p2 = find_closest_points(points)
print('{:.3f}'.format(distance))
print('({}, {})'.format(p1.x, p1.y))
print('({}, {})'.format(p2.x, p2.y))
