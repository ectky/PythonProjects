import turtle
turtle.speed('fastest')
side=int(input("Please enter length of side: "))

for i in range(8):
    for j in range(8):
        if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
            turtle.begin_fill()
        for s in range(4):
            turtle.forward(side)
            turtle.left(90)
        if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
            turtle.end_fill()
        turtle.forward(side)
    turtle.penup()
    turtle.goto(0,side*(i+1))
    turtle.pendown()

turtle.exitonclick()
