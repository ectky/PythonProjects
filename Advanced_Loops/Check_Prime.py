import math
n = int(input())

prime = True

if n < 2 :
    prime = False
else:
    num = round(math.sqrt(n))

    for i in range(2, num + 1):
        if n % i == 0:
            prime = False

if prime:
    print('Prime')
else:
    print('Not Prime')
