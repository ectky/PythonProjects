n = int(input())

Sum = 0

while n != 0:
    Sum += n % 10
    n //= 10

print(Sum)
