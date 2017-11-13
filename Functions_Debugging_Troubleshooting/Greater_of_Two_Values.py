def type_of_input(type, a):
    if type == 'int':
        a = int(a)
    elif type == 'string':
        a = str(a)
    elif type == 'char':
        a = ord(a)
    return a


def get_greater_value(value1, value2):
    if value1 > value2:
        if type == 'char':
            print(chr(value1))
        else:
            print(value1)
    else:
        if type == 'char':
            print(chr(value2))
        else:
            print(value2)

type = input()
value1 = input()
value1 = type_of_input(type, value1)
value2 = input()
value2 = type_of_input(type, value2)
get_greater_value(value1, value2)

