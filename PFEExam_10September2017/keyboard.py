cond = int(input())
message = input()

l1 = 'qwertyuiop[]asdfghjkl;\'zxcvbnm,./ =1234567890?\n-'
l2 = ',уеишщксдзц;ьяаожгтнвмчюйъэфхпрлб =1234567890?\n-'
l3 = 'явертъуиопшщюасдфгхйкл;зьцжбнм,./'

if cond == 1:
    for i in range(len(message)):
        print(l1[l2.index(message[i])], end='')
else:
    for i in range(len(message)):
        print(l2[l1.index(message[i])], end='')

print()
