l = [int(item) for item in input().split(' ')]
count = 0

for i in l:
    i = abs(i)
    if i % 2 == 1:
        count += 1

print(count)
