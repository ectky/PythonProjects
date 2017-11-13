class User:
    def __init__(self, username, recieved_messages):
        self.username = username
        self.recieved_messages = recieved_messages

class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


def read_user(string):
    return User(string[1], {})


def read_message(string):
    if string[0] in users:
        if string[2] in users:
            message = Message(string[3], string[0])
            if string[0] not in users[string[2]].recieved_messages:
                users[string[2]].recieved_messages[string[0]] = [string[3]]
            else:
                users[string[2]].recieved_messages[string[0]].append(string[3])
            return 1
        else:
            return 'error'
    else:
        return 'error'

users = {}
l_users = []
string = input()
while string != 'exit':
    string = string.split(' ')
    if len(string) == 2:
        user = read_user(string)
        users[user.username] = user
        l_users.append(user.username)
    else:
        result = read_message(string)
        if result != 1:
            string = input()
            continue
    string = input()


convo = input().split(' ')
user1 = convo[0]
user2 = convo[1]

if user1 in users[user2].recieved_messages and\
        user2 in users[user1].recieved_messages:
    i = 0
    while len(users[user2].recieved_messages[user1]) > i or len(users[user1].recieved_messages[user2]) > i:
        if len(users[user2].recieved_messages[user1]) > i:
            print('{}: {}'.format(user1, users[user2].recieved_messages[user1][i]))
        if len(users[user1].recieved_messages[user2]) > i:
            print('{} :{}'.format(users[user1].recieved_messages[user2][i], user2))
        i += 1
else:
    print('No messages')
