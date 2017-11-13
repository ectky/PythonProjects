def raise2power(number, power):
    raised = 1
    for i in range(power):
        raised *= number
    return raised


def print_raised(raised):
    if len(str(raised)) == 7:
        print(raised)
    elif len(str(raised)) > 17:
        print('%.4f' % raised)
    else:
        print('%.f' % raised)
    return

number = float(input())
power = int(input())
raised = raise2power(number,power)
print_raised(raised)
