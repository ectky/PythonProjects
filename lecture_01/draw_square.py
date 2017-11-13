import turtle
user_input = input("Please enter a number: ")
length = int(user_input)

turtle.speed('slow')
turtle.color('green')
turtle.forward(length)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(length)

turtle.done()
