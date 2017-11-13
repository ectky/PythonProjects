command = input()
programmer = command.split(' ')[1]
queue =[programmer]

while len(queue) > 0:
    command = input()
    if command == 'NEXT':
        print(queue[0])
        queue.pop(0)
    elif command == 'SKIP':
        queue.pop(0)
    elif command == 'CLEANUP':
        curr_queue = []
        for programmer in queue:
            if len(programmer) % 2 != 0:
                curr_queue.append(programmer)
            else:
                print(programmer)
        queue = curr_queue
    elif command == 'CLEANDOWN':
        curr_queue = []
        for i in range(len(queue)):
            if i % 2 == 1 and len(queue[i]) % 2 == 0:
                pass
            else:
                curr_queue.append(queue[i])
        queue = curr_queue
    else:
        command = command.split(' ')
        if command[0] == 'ADD':
            queue.append(command[1])
        else:
            try:
                queue.remove(command[1])
            except:
                continue
