num = int(input())
studentsbook = {}
unique_names = []

for i in range(num):
    line = input().split(' ')
    name, mark = line[0], line[1]

    if name in studentsbook:
        studentsbook[name].append(mark)
    else:
        studentsbook[name] = [mark]
        unique_names.append(name)

import statistics

for i in unique_names:
    print('{} -> {} (avg: {:.2f})'.format(i, ' '.join(studentsbook[i]), statistics.mean(map(float, studentsbook[i])))) #sum(map(float, studentsbook[i])) / len(studentsbook[i])))
