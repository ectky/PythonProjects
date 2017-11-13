import re
pattern = r'TO: [A-Z]+; MESSAGE: .+;'
private_key = input()
message = input()
list_of_messages = []
keys = []

for num in private_key:
    keys.append(int(num))

while message != 'END':
    if re.match(pattern, message):
        list_of_messages.append(message)
    message = input()


for message in sorted(list_of_messages):
    encrypted = ''
    index = 0
    for char in message:
        encrypted += chr(ord(char) + keys[index % len(keys)])
        index += 1
    print(encrypted)
