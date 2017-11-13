class Rectangle:
    def __init__(self, top, left, height, width):
        self._top = top
        self._left = left
        self._height = height
        self._width = width
        self._set_right()
        self._set_bottom()

    def _set_right(self):
        self._right = self._top + self._height

    def _set_bottom(self):
        self._bottom = self._left + self._width


def is_inside(r1, r2):
    condition = (r1._left >= r2._left and
                r1._right <= r2._right and
                r1._top >= r2._top and
                r1._bottom <= r2._bottom)
    return condition


def read_rectangle(inp):
    inp = [int(item) for item in inp.split(' ')]
    return Rectangle(inp[0], inp[1], inp[2], inp[3])

inp1 = input()
r1 = read_rectangle(inp1)
inp2 = input()
r2 = read_rectangle(inp2)

if is_inside(r1, r2):
    print('Inside')
else:
    print('Not inside')
