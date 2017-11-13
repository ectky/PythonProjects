
hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

distance  = (hour_exam - hour_arrival) * 60 + minute_exam - minute_arrival

if distance < 0:
    print('Late')
    if distance > - 60:
        print('{0} minutes after the start'.format(abs(distance)))
    elif distance <= -60:
        distance = abs(distance)
        hours = distance // 60
        minutes = distance - 60 * (hours)
        if minutes < 10:
            print('{0}:0{1} hours after the start'.format(hours, minutes))
        else:
            print('{0}:{1} hours after the start'.format(hours, minutes))
elif distance <= 30:
    print('On time')
    print('{0} minutes before the start'.format(distance))
else:
    print('Early')
    if distance < 60:
        print('{0} minutes before the start'.format(distance))
    elif distance >= 60:
        hours = distance // 60
        minutes = distance - 60 * (hours)
        if minutes < 10:
            print('{0}:0{1} hours before the start'.format(hours, minutes))
        else:
            print('{0}:{1} hours before the start'.format(hours, minutes))





