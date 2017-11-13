first = int(input())
second = int(input())
third = int(input())
sum = first + second + third

mins = str(sum//60)

if sum % 60 < 10:
    secs = '0' + str(sum % 60)
else:
    secs = str(sum % 60)

print(mins + ':' + secs)
