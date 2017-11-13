projection = input()
rows = int(input())
columns = int(input())

if(projection == "Premiere"):
    print("{0:.2f} leva".format(rows*columns*12))
elif(projection == "Normal"):
    print("{0:.2f} leva".format(rows*columns*7.5))
elif(projection == "Discount"):
    print("{0:.2f} leva".format(rows*columns*5))
