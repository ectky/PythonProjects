n = int(input())


def draw_middle(n):
    for i in range(n-2):
        print('-' + "\/" * (n-1) + '-')


def draw_outline(n):
    print("-" * 2*n)


def draw_square(n):
    draw_outline(n)
    draw_middle(n)
    draw_outline(n)


draw_square(n)
