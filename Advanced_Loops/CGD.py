a = int(input())
b = int(input())

t = 0

while (b != 0):
    t = b
    b = a % b
    a = t

print(a)
