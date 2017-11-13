n = int(input())

min1 = 1000000000.0
min2 = 1000000000.0
max1 = -1000000000.0
max2 = -1000000000.0
sum1 = 0.0
sum2 = 0.0

for i in range(1, n+1):
    num = float(input())
    if i%2 != 0:
        sum1 += num
        min1 = min(min1, num)
        max1 = max(max1, num)
    else:
        sum2 += num
        min2 = min(min2, num)
        max2 = max(max2, num)


print("OddSum={0},".format(sum1))
if min1 == 1000000000.0:
    print("OddMin=No,")
else:
    print("OddMin={0},".format(min1))
if max1 == -1000000000.0:
    print("OddMax=No,")
else:
    print("OddMax={0},".format(max1))

print("EvenSum={0},".format(sum2))
if min2 == 1000000000.0:
    print("EvenMin=No,")
else:
    print("EvenMin={0},".format(min2))
if max2 == -1000000000.0:
    print("EvenMax=No,")
else:
    print("EvenMax={0},".format(max2))
