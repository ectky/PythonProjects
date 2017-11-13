class Exercises:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems

def read_input(string):
    list = [item for item in string.split(' -> ')]
    problems = list[3].split(', ')
    return  Exercises(list[0], list[1], list[2], problems)

string = input()


while string != 'go go go':
    counter = 1
    exercise = read_input(string)
    print('Exercises: {}'.format(exercise.topic))
    print('Problems for exercises and homework for the "{}" course @ SoftUni.'.format(exercise.course_name))
    print('Check your solutions here: {}'.format(exercise.judge_contest_link))
    for problem in exercise.problems:
        print('{}. {}'.format(counter, problem))
        counter += 1
    string = input()
