import re
train = input()
pattern = r'(<\[[^a-zA-Z0-9]*?\]\.)+(\.\[[a-zA-Z0-9]*\]\.)*$'
list = []

while train != 'Traincode!':
    if re.match(pattern, train):
        list.append(train)
    train = input()

print('\n'.join(list))
