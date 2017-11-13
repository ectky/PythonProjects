fruit = input().lower()
day_of_week = input().lower()
quantity = float(input())

weekday = day_of_week == 'monday' or day_of_week == 'tuesday' or day_of_week == 'wednesday' or day_of_week == 'thursday' or day_of_week == 'friday'
weekend = day_of_week == "saturday" or day_of_week == 'sunday'
price = -1.0

if(weekday):
    if(fruit == "banana"):
        price = quantity * 2.5
    elif(fruit == "apple"):
        price = quantity *  1.2
    elif(fruit == "orange"):
        price = quantity *  0.85
    elif(fruit == "grapefruit"):
        price = quantity *  1.45
    elif(fruit == "kiwi"):
        price = quantity *  2.7
    elif(fruit == "pineapple"):
        price = quantity *  5.5
    elif(fruit == "grapes"):
        price = quantity *  3.85
elif(weekend):
    if(fruit == "banana"):
        price = quantity *  2.7
    elif(fruit == "apple"):
        price = quantity *  1.25
    elif(fruit == "orange"):
        price = quantity *  0.90
    elif(fruit == "grapefruit"):
        price = quantity *  1.60
    elif(fruit == "kiwi"):
        price = quantity *  3
    elif(fruit == "pineapple"):
        price = quantity *  5.6
    elif(fruit == "grapes"):
        price = quantity *  4.2

if(price >= 0):
    print('{0:.2f}'.format(price))
else:
    print('Error')




