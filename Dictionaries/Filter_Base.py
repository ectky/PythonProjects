string = input()
age = {}
unique_age = []
salary = {}
unique_salary = []
position = {}
unique_position = []


while string != 'filter base':
    list = [i for i in string.split(' -> ')]
    name = list[0]

    try:
        employee_age = int(list[1])
        age[name] = employee_age
        unique_age.append(name)
    except:
        try:
            employee_salary = float(list[1])
            salary[name] = employee_salary
            unique_salary.append(name)
        except:
            employee_position = list[1]
            position[name] = employee_position
            unique_position.append(name)
    string = input()

command = input()

if command == 'Age':
    for key in unique_age:
        print('Name: {}\nAge: {}\n===================='.format(key, age[key]))
elif command == 'Salary':
    for key in unique_salary:
        print('Name: {}\nSalary: {:.2f}\n===================='.format(key, salary[key]))
elif command == 'Position':
    for key in unique_position:
        print('Name: {0}\nPosition: {1}\n===================='.format(key, position[key]))


