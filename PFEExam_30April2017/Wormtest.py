length = int(input())
width = float(input())

length *= 100
try:
    remainder = length % width

    if remainder == 0 or width == 0:
        print('{:.2f}'.format(length * width))
    else:
        percentage = (length / width) * 100
        print('{:.2f}%'.format(percentage))
except:
    print('{:.2f}'.format(length * width))
