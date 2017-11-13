n = int(input())

sum1 = 0
sum2 = 0

for i in range(1, n+1):
    num = int(input())
    sum1 += num

for j in range(1, n+1):
    num = int(input())
    sum2 += num

if sum1 == sum2:
    print("Yes, sum = {0}".format(sum2))
else:
    print("No, diff = {0}".format(abs(sum1-sum2)))
