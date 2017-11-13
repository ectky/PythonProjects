command = input()
solutions = {}
certificates = {}
contests = {}
contests2 = {}

while command != 'QUIT':
    if 'ADD SOLUTION' in command:
        command = command.split(' ')
        user = command[2]
        contest = command[3]
        task = command[4]
        solution_id = command[5]
        points = float(command[6])

        if solution_id in solutions:
            print('Solution already exists')
        else:
            if contest in contests:
                if user in contests2[contest]:
                    contests2[contest][user].append((task, points))
                else:
                    contests2[contest][user] = [(task, points)]
                contests[contest][user] = points
            else:
                contests[contest] = {user: points}
                contests2[contest] = {user: [(task, points)]}
            solutions[solution_id] = [user, contest, task, points]
    elif 'CERTIFICATE ' in command:
        command = command.split(' ')
        user, contest = command[2], command[3]
        if command[0] == 'ADD':
            if user in certificates:
                if contest in certificates[user]:
                    print('Certificate already exists')
                else:
                    certificates[user].append(contest)
            else:
                certificates[user] = [contest]
        else:
            if user in certificates:
                if contest not in certificates[user]:
                    print('Certificate not found')
                elif contest not in contests2:
                    print(0)
                elif user in contests2[contest]:
                    # contests2 = {'3': {'Asami': [('0', 33.0)]}}
                    keys = []
                    total = 0.0
                    index = 0
                    while index < len(contests2[contest][user]):
                        key, maximal = contests2[contest][user][index]
                        if key not in keys:
                            keys.append(key)
                            for tupl in contests2[contest][user]:
                                task, power = tupl
                                if task == key:
                                    if maximal < power:
                                        maximal = power
                            total += maximal
                        index += 1
                    print(total)
                else:
                    print(0)
            else:
                print('Certificate not found')
    else:
        command = command.split(' ')
        if command[1] == 'SOLUTION':
            solution_id = command[2]
            if solution_id in solutions:
                print('User: {0}, Contest: {1}, Task: {2}, Points: {3}'.format(solutions[solution_id][0],
                                                                               solutions[solution_id][1],
                                                                               solutions[solution_id][2],
                                                                               solutions[solution_id][3]))
            else:
                print('Solution not found')
        elif command[1] == 'CERTIFICATES':
            user = command[2]
            if user in certificates:
                print(','.join(sorted(certificates[user])))
            else:
                print('User not found')
        else:
            users = []
            contest = command[2]
            total_users = dict()
            if contest in contests:
                for user in contests[contest]:
                    temp = {}
                    for x in contests2[contest][user]:
                        task = x[0]
                        points = x[1]
                        if task in temp:
                            if temp[task] < points:
                                temp[task] = points
                        else:
                            temp[task] = points
                    total_users[user] = -sum(temp.values()), user
                contester = sorted(total_users.keys(), key=lambda x: total_users[x])
                for user in contester:
                    users.append(user)
                print(','.join(users))
            else:
                print('Contest not found')
    command = input()
