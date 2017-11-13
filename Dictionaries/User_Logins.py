user_input = input()
dict = {}
unique = {}
unique2 = []
unsuccessful = 0

while user_input != 'login':
    string = [i for i in user_input.split(' -> ')]
    username = string[0]
    password = string[1]
    dict[username] = password
    user_input = input()

user_input = input()
while user_input != 'end':
    string2 = [item for item in user_input.split(' -> ')]
    username = string2[0]
    password = string2[1]
    if username in dict:
        unique2.append(username)
        if dict[username] == password:
            print('{}: logged in successfully'.format(username))
        else:
            print('{}: login failed'.format(username))
            unsuccessful += 1
        user_input = input()
    else:
        print('{}: login failed'.format(username))
        unsuccessful += 1
        user_input = input()

print('unsuccessful login attempts: {}'.format(unsuccessful))
