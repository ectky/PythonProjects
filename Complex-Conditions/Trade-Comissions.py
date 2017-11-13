town = input()
sales = float(input())

comission = -1.0

""""500 < s ≤ 1 000	    1 000 < s ≤ 10 000 	  s > 10 000"""

if(sales >=0 and sales <= 500):
    if(town == 'Sofia'):
        comission = 0.05
    elif(town == 'Varna'):
        comission = 0.045
    elif(town == 'Plovdiv'):
        comission = 0.055

elif(sales > 500 and sales <= 1000):
    if(town == 'Sofia'):
        comission = 0.07
    elif(town == 'Varna'):
        comission = 0.075
    elif(town == 'Plovdiv'):
        comission = 0.08

elif(sales > 1000 and sales <= 10000):
    if(town == 'Sofia'):
        comission = 0.08
    elif(town == 'Varna'):
        comission = 0.1
    elif(town == 'Plovdiv'):
        comission = 0.12

elif(sales > 10000):
    if(town == 'Sofia'):
        comission = 0.12
    elif(town == 'Varna'):
        comission = 0.13
    elif(town == 'Plovdiv'):
        comission = 0.145

if(comission == -1):
    print('error')
else:
    print("{0:.2f}".format(sales*comission))
