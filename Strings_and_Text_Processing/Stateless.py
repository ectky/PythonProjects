state = input()
list = []

while state != 'collapse':
    fiction = input()
    while len(fiction) != 0:
        state = state.replace(fiction, '')
        fiction = fiction[1:len(fiction)-1]
    if len(state) == 0:
        list.append('(void)')
    else:
        state = state.strip()
        list.append(state)
    state = input()

for i in list:
    print(i)


