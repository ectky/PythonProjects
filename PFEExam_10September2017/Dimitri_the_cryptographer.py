corr_symbol = input()
table = {}
first_table = {}
second_table = {}
third_table = {}
i = 0
new_message = ''

while True:
    if i == 3:
        break
    elif corr_symbol == 'STOP':
        first_table = table
        table = {}
        i += 1
        corr_symbol = input()
    elif corr_symbol == 'HALT':
        second_table = table
        table = {}
        i += 1
        corr_symbol = input()
    elif corr_symbol == 'END':
        third_table = table
        table = {}
        i += 1
        corr_symbol = input()
    else:
        corr_symbol = corr_symbol.split(' -> ')
        table[corr_symbol[0]] = corr_symbol[1]
        corr_symbol = input()


message = corr_symbol
messager = ''

for index in range(len(message)):
    if message[index] in first_table:
        messager += first_table[message[index]]
    else:
        messager += message[index]

for index in range(len(messager)):
    if index % 2 == 0:
        if messager[index] in second_table:
            new_message += second_table[messager[index]]
        else:
            new_message += messager[index]
    else:
        new_message += messager[index]

messager = ''
for index in range(len(new_message)):
    if index % 3 == 0:
        if new_message[index] in third_table:
            messager += third_table[new_message[index]]
        else:
            messager += new_message[index]
    else:
        messager += new_message[index]

print(messager)


