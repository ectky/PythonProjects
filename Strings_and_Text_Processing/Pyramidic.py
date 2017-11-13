n = int(input())
list = []

for ind in range(n):
    string = input()
    list.append(string)

count = -1
dictionary = {}

cnt = 1
for i in range(len(list)):
    for char in list[i]:
        for item in list[i:]:
            if item.find(char * cnt) != -1:
                count += 2
                cnt += 2
                dictionary[char] = count
                continue
            else:
                cnt = 1
                count = -1
                break

maximal = -1000000000000
key = ''

for x, value in dictionary.items():
    if value > maximal:
        maximal = value
        key = x

count = 1
for y in range(n):
    while count <= maximal:
        print(key * count)
        count += 2
