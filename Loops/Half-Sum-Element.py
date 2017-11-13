n = int(input())

max = int(input())
sum = 0

for i in range(1, n):
    num = int(input())
    if num > max:
        sum += max
        max = num
    else:
        sum += num

if max == sum:
    print('Yes\nSum = {0}'.format(sum))
else:
    print('No\nDiff = {0}'.format(abs(sum-max)))
