import turtle

user_counter=input("Please enter a number: ")
counter = int(user_counter)

g = 134
l = 120
while counter>0:
    turtle.left(g)
    turtle.forward(l)
    counter-=1

turtle.done()
