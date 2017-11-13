string = input().lower().split(' ')

dict = {}
unique = []

for i in string:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        unique.append(i)

ans = list()

for key in unique:
    if dict[key] % 2 == 1:
        ans.append(key)

print(', '.join(ans))
