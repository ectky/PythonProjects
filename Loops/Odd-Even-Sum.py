n = int(input())

sum1 = 0
sum2 = 0

for i in range(1, n+1):
    num = int(input())
    if i%2 == 0:
        sum1 += num
    else:
        sum2 += num

if sum1 == sum2:
    print("Yes\nSum = {0}".format(sum2))
else:
    print("No\nDiff = {0}".format(abs(sum1-sum2)))
