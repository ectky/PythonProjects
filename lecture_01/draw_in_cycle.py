import turtle

user_degrees = input("Enter a number for degrees: ")
degrees = int(user_degrees)
user_length = input("Enter a number for length: ")
length = int(user_length)

turtle.speed('slowest')
turtle.color('yellow')

while (length>0):
    turtle.forward(length)
    turtle.left(degrees)

turtle.done()
