command = input()
dict = {}
removed = set()
before = 0

while command != 'ANSWER ME':
    if 'ORDER' in command:
        command = command.split(' ')
        name1, name2 = command[1], command[2]
        dict[name2] = name1
    elif 'REMOVE' in command:
        command = command.split(' ')
        name = command[1]
        removed.add(name)
    command = input()


person = 'Pesho'
for key in dict:
    if key == person:
        if key not in removed:
            person = key
            before += 1
print(before)
