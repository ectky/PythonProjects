l = [i for i in input().split(' ')]
l = [i for i in l.split(',')]
l = [i for i in l.split(';')]
l = [i for i in l.split(':')]
l = [i for i in l.split('.')]
l = [i for i in l.split('!')]
l = [i for i in l.split('(')]
l = [i for i in l.split('"')]
l = [i for i in l.split('\'')]
l = [i for i in l.split('\\')]
l = [i for i in l.split('/')]
l = [i for i in l.split('[')]
l = [i for i in l.split(']')]

lowercase = []
lower = 0
uppercase = []
upper = 0
mixedcase = []

for i in l:
    for j in i:
        if j > 'a' and j < 'z':
            lower += 1
        elif j > 'A' and j < 'Z':
            upper += 1
    if lower == len(i):
        lowercase += [i]
    elif upper == len(i):
        uppercase += [i]
    else:
        mixedcase += [i]

print(lowercase)
print(uppercase)
print(mixedcase)
