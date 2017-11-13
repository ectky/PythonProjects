l = [int(i) for i in input().split(' ')]

result = l[:1]
l.pop(0)
while len(l) != 0:
    curr_index = len(result) - 1
    while curr_index >= 0 and l[0] < result[curr_index]:
        curr_index -= 1
    result.insert(curr_index + 1, l[0])
    l.pop(0)


for i in result:
    print(i, end=' ')
