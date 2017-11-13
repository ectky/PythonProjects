hours = int(input())
minutes = int(input())

newmins = minutes + 15

if newmins >= 60:
    hours+=1
    newmins -= 60

if newmins < 10:
    mins = '0' + str(newmins)
else:
    mins = str(newmins)

if hours == 24:
    hour = '0'
else:
    hour = str(hours)

print(hour + ':' + mins)
