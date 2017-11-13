w = float(input())
h = float(input())

w *= 100
h *= 100
h -= 100
desks = h // 70
rows = w // 120
places = desks * rows - 3

print("{0:.0f}".format(places))



