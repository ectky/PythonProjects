banned = [i for i in input().split(', ')]
text = input()

for item in banned:
    text = text.replace(item, '*' * len(item))

print(text)
