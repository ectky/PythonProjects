from math import sqrt


class Box:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.set_width()
        self.set_height()

    def set_width(self):
        self.width = int(Point.calc_distance(self.upper_left, self.upper_right)) #+ Point.calc_distance(self.bottom_left, self.bottom_right)

    def set_height(self):
        self.height = int(Point.calc_distance(self.upper_left, self.bottom_left)) #+ Point.calc_distance(self.upper_right, self.bottom_right)

    def calculate_perimeter(self):
        return int(2 * self.width + 2 * self.height)

    def calculate_area(self):
        return int(self.width * self.height)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_distance(self, p2):
        a = abs(self.x - p2.x)
        b = abs(self.y - p2.y)
        c2 = pow(a, 2) + pow(b, 2)
        c = sqrt(c2)
        return c


def read_point(string):
    string = string.split(':')
    return Point(int(string[0]), int(string[1]))


def read_box(string):
    string = string.split(' | ')
    upper_left = read_point(string[0])
    upper_right = read_point(string[1])
    bottom_left = read_point(string[2])
    bottom_right = read_point(string[3])
    return Box(upper_left, upper_right, bottom_left, bottom_right)

string = input()
while string != 'end':
    box = read_box(string)
    print('Box: {}, {}'.format(box.width, box.height))
    perimeter = box.calculate_perimeter()
    print('Perimeter: {}'.format(perimeter))
    area = box.calculate_area()
    print('Area: {}'.format(area))
    string = input()
