n = int(input())

unique_names = []

for i in range(n):
    name = input()
    if name not in unique_names:
        unique_names.append(name)

for item in unique_names:
    print(item)
