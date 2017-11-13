def get_area(side, height):
    return side * height / 2


a = float(input())
ha = float(input())

if len(str(get_area(a, ha))) in range(8, 12):
    print(get_area(a, ha))
else:
    print('%g' %get_area(a, ha))

